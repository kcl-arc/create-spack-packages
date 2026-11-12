# rcmb/packages/campari/package.py
import os
import shutil
import glob

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack.package import *


class Campari(AutotoolsPackage):
    """CAMPARI: Monte Carlo and MD simulation/analysis package
    (ABSINTH implicit solvent). Single executable driven by a key-file."""

    homepage = "https://campari.sourceforge.net"
    url = "https://downloads.sourceforge.net/project/campari/campari/campari_v4_12202020.zip"

    # Fill with: spack checksum campari 4_12202020 5_04192024
    # V5: uncomment after `sha256sum campari_v5_04192024.tar.bz2`
    # version("5_04192024", sha256="<fill in>",
    #         url="https://downloads.sourceforge.net/project/campari/campari/campari_v5_04192024.tar.bz2")
    version("4_12202020", sha256="bc627fb286b5461a5c68aa3e1a551ecd81016495163685800163c734f7c4f1bd", preferred=True,
            url="https://downloads.sourceforge.net/project/campari/campari/campari_v4_12202020.zip")

    variant("mpi", default=True, description="MPI build (replica exchange etc.)")
    variant("openmp", default=True, description="OpenMP threads build")
    variant("netcdf", default=True, description="NetCDF I/O and camp_ncminer")
    variant("lapack", default=True, description="LAPACK/BLAS (P-SHAKE, PCA)")
    variant("mpif08", default=True, description="Use mpi_f08 module (disable if MPI lacks it)")
    variant("python", default=True, description="Python for helper/key-file builder scripts")

    depends_on("c", type="build")        # embedded XDR is C
    depends_on("fortran", type="build")
    depends_on("gmake", type="build")

    depends_on("fftw@3 precision=double")
    depends_on("fftw+openmp", when="+openmp")
    depends_on("mpi", when="+mpi")
    depends_on("netcdf-fortran", when="+netcdf")
    depends_on("lapack", when="+lapack")
    depends_on("blas", when="+lapack")
    depends_on("python@3:", type="run", when="+python")
    depends_on("automake", type="build")
    depends_on("m4", type="build")       # source/xdr/Makefile runs m4 to generate libxdrf.c
    # The bundled XDR library includes <rpc/rpc.h>; glibc dropped Sun RPC
    # (AlmaLinux 10 has no /usr/include/rpc), libtirpc provides it.
    depends_on("libtirpc")
    
    # added november 12 to avoid copying automake auxiliary files from /usr/share/automake-*/ to the source tree
    @run_before("configure")
    def patch_automake_auxiliary_path(self):
        """Use Spack's Automake auxiliary files instead of /usr/share."""

        automake_share = join_path(
            self.spec["automake"].prefix,
            "share",
        )

        candidates = glob.glob(
            join_path(automake_share, "automake-*")
        )

        if not candidates:
            raise InstallError(
                "Could not find Automake auxiliary directory under "
                f"{automake_share}"
            )

        automake_aux = candidates[0]

        configure_script = join_path(
            self.stage.source_path,
            "source",
            "configure",
        )

        with open(configure_script, "r") as f:
            content = f.read()

        # Literal text in configure: doit="$CP /usr/share/automake-*/$cni ..."
        # (a plain shell glob, no backslash before the '*').
        old = "/usr/share/automake-*/$cni"
        new = f"{automake_aux}/$cni"

        if old not in content:
            raise InstallError(
                "Could not find the expected hardcoded Automake path "
                f"in {configure_script}"
            )

        content = content.replace(old, new)

        with open(configure_script, "w") as f:
            f.write(content)

        tty.msg(f"Using Automake auxiliary files from: {automake_aux}")

    @run_before("configure")
    def fix_date_and_time_kind(self):
        """utilities.f90 passes an integer(8) VALUES array to DATE_AND_TIME.
        That is Fortran 2018; configure adds -std=f2008, so gfortran rejects it.
        Read into a default-kind array and copy, keeping the kind-8 seed maths."""
        src = join_path(self.stage.source_path, "source", "utilities.f90")
        filter_file(
            "integer(KIND=8) dts(8)",
            "integer(KIND=8) dts(8)\n  integer dts4(8)",
            src,
            string=True,
        )
        filter_file(
            "call Date_and_Time(rc(1),rc(2),rc(3),dts)",
            "call Date_and_Time(rc(1),rc(2),rc(3),dts4)\n    dts = dts4",
            src,
            string=True,
        )

    configure_directory = "source"
    build_directory = "source"   # configure route builds in-tree

    @property
    def build_targets(self):
        # XDRCFLAGS is empty in the generated Makefile and becomes CFLAGS in
        # source/xdr/Makefile; a command-line value also reaches that sub-make.
        tirpc_inc = join_path(self.spec["libtirpc"].prefix.include, "tirpc")
        # 'all' always includes camp_ncminer, which only links with NetCDF
        # (undefined ncdm_makeio_ otherwise). Build just the variants requested.
        s = self.spec
        targets = ["campari"]
        if s.satisfies("+openmp"):
            targets.append("campari_threads")
        if s.satisfies("+mpi"):
            targets.append("campari_mpi")
            if s.satisfies("+openmp"):
                targets.append("campari_mpi_threads")
        if s.satisfies("+netcdf"):
            targets.append("camp_ncminer")
            if s.satisfies("+openmp"):
                targets.append("camp_ncminer_threads")
        return targets + [f"XDRCFLAGS=-I{tirpc_inc}"]

    def setup_build_environment(self, env):
        if self.spec.satisfies("+mpi"):
            env.set("FC", self.spec["mpi"].mpifc)
            env.set("MPIFC", self.spec["mpi"].mpifc)

    def configure_args(self):
        s = self.spec
        args = [
            f"--with-fftw3={s['fftw'].prefix}",
            f"--exec-prefix={self.prefix}",
            f"--bindir={self.prefix.bin}",
            f"--libdir={self.prefix.lib}",
        ]
        args.append("--enable-mpi=yes" if s.satisfies("+mpi") else "--enable-mpi=no")
        if s.satisfies("+mpi ~mpif08"):
            args.append("--disable-mpif08")
        if s.satisfies("~openmp"):
            args.append("--enable-threads=no")
        if s.satisfies("+netcdf"):
            args.append(f"--with-netcdf4={s['netcdf-fortran'].prefix}")
        # CAMPARI's default GNU performance flags are "-march=native -funroll-loops":
        # -march=native ties the binary to the build node's CPU. Drop it; Spack's
        # compiler wrapper already adds the flags for the spec's target.
        args.append("--enable-performance-code=-funroll-loops")
        # LIBS is linked into every CAMPARI binary. libtirpc supplies the xdr_*
        # functions the bundled XDR library calls.
        libs = s["libtirpc"].libs
        if s.satisfies("+lapack"):
            # --with-blas/--with-lapack=<dir> only add -L$(dirname <dir>) and then
            # try -lblas/-lopenblas/-lmkl..., which misses MKL (-lmkl_rt etc.).
            # Put the exact libraries in LIBS: configure's first probe (no extra
            # -l) then succeeds.
            libs = s["lapack"].libs + s["blas"].libs + libs
        else:
            args += ["--with-lapack=no", "--with-blas=no"]
        args.append(f"LIBS={libs.ld_flags}")
        # GCC >= 10 is strict about argument mismatches in legacy Fortran
        if s.satisfies("%gcc@10:"):
            args.append("--with-trailing-user-fcflags=-fallow-argument-mismatch")
        return args

    @run_after("install")
    def install_share(self):
        # Parameter files (abs3.2_opls.prm etc.) referenced by FMCSC_PARAMETERS,
        # plus data/examples/tools if present in this release
        root = self.stage.source_path
        share = join_path(self.prefix.share, "campari")
        for d in ("params", "data", "examples", "tools", "doc"):
            src = join_path(root, d)
            if os.path.isdir(src):
                install_tree(src, join_path(share, d))
        # Fallback: if `make install` didn't populate bin/, copy build outputs
        if not os.path.isdir(self.prefix.bin) or not os.listdir(self.prefix.bin):
            for archdir in find(join_path(root, "bin"), "*", recursive=False):
                if os.path.isdir(archdir):
                    install_tree(archdir, self.prefix.bin)

    def setup_run_environment(self, env):
        env.set("CAMPARI_HOME", join_path(self.prefix.share, "campari"))
        env.set("CAMPARI_PARAMS", join_path(self.prefix.share, "campari", "params"))