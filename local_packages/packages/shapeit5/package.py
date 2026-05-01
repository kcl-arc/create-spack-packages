# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import os

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Shapeit5(MakefilePackage):
    """
    SHAPEIT5 is a software package to estimate haplotypes in large genotype datasets (WGS and SNP array).
    """

    homepage = "https://odelaneau.github.io/shapeit5/"
    url = "https://github.com/odelaneau/shapeit5/archive/refs/tags/v5.1.1.tar.gz"
    git = "https://github.com/odelaneau/shapeit5.git"

    maintainers("harrysharma1")

    license("MIT", checked_by="harrysharma1")

    version(
        "5.1.1",
        tag = "v5.1.1",
        submodules = True,
    )
    version(
        "5.1.0",
        tag = "v5.1.0",
        submodules = True,
    )
    version(
        "1.0.0",
        tag = "v1.0.0",
        submodules = True,
    )

    depends_on("htslib")
    depends_on("boost +iostreams +program_options")
    depends_on("bzip2")
    depends_on("xz")
    depends_on("curl")
    depends_on("openssl")
    depends_on("libdeflate")

    def edit(self, spec, prefix):
        if spec.satisfies("@5.1.1:"):
            projects = ["ligate", "phase_common", "phase_rare", "simulate", "switch"]
        else:
            projects = ["ligate", "phase_common", "phase_rare", "switch"]

        htslib_src = spec["htslib"].prefix
        htslib_inc = htslib_src.include
        htslib_lib = "{0}/libhts.a".format(htslib_src.lib)

        boost_inc = spec["boost"].prefix.include
        boost_lib_io = "{0}/libboost_iostreams.a".format(spec["boost"].prefix.lib)
        boost_lib_po = "{0}/libboost_program_options.a".format(spec["boost"].prefix.lib)

        openssl_lib = spec["openssl"].libs.directories[0]

        dyn_libs = " ".join([
            "-lz",
            "-lpthread",
            "{0}/libbz2.a".format(spec["bzip2"].prefix.lib),
            "{0}/liblzma.a".format(spec["xz"].prefix.lib),
            "{0}/libcurl.so".format(spec["curl"].prefix.lib),
            "{0}/libcrypto.so".format(openssl_lib),
            "{0}/libssl.so".format(openssl_lib),
            "{0}/libdeflate.so".format(spec["libdeflate"].prefix.lib),
        ])


        for project in projects:
            makefile = FileFilter("{0}/makefile".format(project))

            makefile.filter(r"^.*: HTSLIB_INC=.*", "HTSLIB_INC={0}".format(htslib_inc))
            makefile.filter(r"^.*: HTSLIB_LIB=.*", "HTSLIB_LIB={0}".format(htslib_lib))

            makefile.filter(r"^.*: BOOST_INC=.*", "BOOST_INC={0}".format(boost_inc))
            makefile.filter(r"^.*: BOOST_LIB_IO=.*", "BOOST_LIB_IO={0}".format(boost_lib_io))
            makefile.filter(r"^.*: BOOST_LIB_PO=.*", "BOOST_LIB_PO={0}".format(boost_lib_po))

            makefile.filter(r"^DYN_LIBS=.*",      "DYN_LIBS={0}".format(dyn_libs))
            makefile.filter(r"^.*: DYN_LIBS=.*",  "DYN_LIBS={0}".format(dyn_libs))


    def patch(self):
        for header in [
            "phase_common/src/models/haplotype_segment_single.h",
            "phase_common/src/models/haplotype_segment_double.h",
        ]:
            filter_file(r"\bisnan\b", "std::isnan", header)
            filter_file(r"\bisinf\b", "std::isinf", header)

    def build(self, spec, prefix):
        if spec.satisfies("@5.1.1:"):
            projects = ["ligate", "phase_common", "phase_rare", "simulate", "switch"]
        else:
            projects = ["ligate", "phase_common", "phase_rare", "switch"]

        for project in projects:
            with working_dir(project):
                make()

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        for project in ["ligate", "phase_common", "phase_rare", "switch", "convert"]:
            proj_bin = join_path(project, "bin")
            if os.path.isdir(proj_bin):
                install_tree(proj_bin, prefix.bin)

        install_tree('test', join_path(self.prefix, 'test'))
        install_tree('docs', join_path(self.prefix, 'docs'))
        if spec.satisfies("@5.0:"):
            install_tree('resources/maps', join_path(prefix, 'maps'))
        else:
            install_tree('maps', join_path(self.prefix, 'maps'))