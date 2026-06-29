# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class BoltLmm(MakefilePackage):
    """
    The BOLT-LMM software package consists of two main algorithms, the BOLT-LMM algorithm for mixed model association testing,
    and the BOLT-REML algorithm for variance components analysis (i.e., partitioning of SNP-heritability and estimation of genetic correlations).
    """

    homepage = "https://storage.googleapis.com/broad-alkesgroup-public/BOLT-LMM/BOLT-LMM_manual.html"
    url = "https://storage.googleapis.com/broad-alkesgroup-public/BOLT-LMM/downloads/old/BOLT-LMM_v2.4.tar.gz"
    build_directory = "src"

    maintainers("harrysharma1")

    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("GPL-3.0", checked_by="harrysharma1")


    version("2.5", sha256="a5fdc49f79f42aa007282d9080e5b97c6ef2aab25ace2af306f432c44eedebca", url="https://storage.googleapis.com/broad-alkesgroup-public/BOLT-LMM/downloads/BOLT-LMM_v2.5.tar.gz")
    version("2.4.1", sha256="65f13a51277a0834e03911a9e98c9325be95d1d896a3e7b8d2aa759776a78aa6", url="https://storage.googleapis.com/broad-alkesgroup-public/BOLT-LMM/downloads/old/BOLT-LMM_v2.4.1.tar.gz")
    version("2.4", sha256="1fcb9acfe5aaf226770722dcb08649d8c171ca9cf8a09253801c70b7e9cadf3c")

    depends_on("cxx", type="build")

    depends_on("openblas")
    depends_on("boost+iostreams+program_options")
    depends_on("nlopt")
    depends_on("zstd")

    def edit(self, spec, prefix):
        makefile = FileFilter("src/Makefile")

        makefile.filter(r"CC\s*=\s*icpc", "CC = g++")
        makefile.filter(
            r"BOOST_INSTALL_DIR\s*=.*",
            "BOOST_INSTALL_DIR = {0}".format(spec["boost"].prefix)
        )
        makefile.filter(
            r"NLOPT_INSTALL_DIR\s*=.*",
            "NLOPT_INSTALL_DIR = {0}".format(spec["nlopt"].prefix)
        )
        makefile.filter(
            r"-L\$\{NLOPT_INSTALL_DIR\}/\.libs",
            "-L{0}".format(spec["nlopt"].prefix.lib)
        )
        makefile.filter(
            r"-Wl,-rpath,\$\{NLOPT_INSTALL_DIR\}/\.libs",
            "-Wl,-rpath,{0}".format(spec["nlopt"].prefix.lib)
        )
        makefile.filter(
            r"LLAPACK = -llapack -lgfortran",
            "LLAPACK = -L{0} -lopenblas -lgfortran".format(spec["openblas"].prefix.lib)
        )
        makefile.filter(r"INTELROOT\s*=.*", "INTELROOT =")
        makefile.filter(r"MKLROOT\s*=.*", "MKLROOT =")
        makefile.filter(r"ZLIB_STATIC_DIR\s*=.*", "ZLIB_STATIC_DIR =")
        makefile.filter(r"LIBSTDCXX_STATIC_DIR\s*=.*", "LIBSTDCXX_STATIC_DIR =")
        makefile.filter(r"GLIBC_STATIC_DIR\s*=.*", "GLIBC_STATIC_DIR =")

        if spec.satisfies("@2.5"):
            makefile.filter(
                r"ZSTD_DIR\s*=.*",
                "ZSTD_DIR = {0}".format(spec["zstd"].prefix)
            )
            makefile.filter(
                r"CPATHS \+= -I\$\{ZSTD_DIR\}",
                "CPATHS = -I{0}".format(spec["zstd"].prefix.include)
            )
            makefile.filter(
                r"LPATHS \+= -L\$\{ZSTD_DIR\}",
                "LPATHS = -L{0}".format(spec["zstd"].prefix.lib)
            )

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("src/bolt", prefix.bin)