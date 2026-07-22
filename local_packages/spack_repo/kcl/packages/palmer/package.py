# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Palmer(MakefilePackage):
    """
    PALMER detects non-reference mobile element insertions (LINE, Alu, SVA, HERVK) and other insertions (for example, NUMTs and HPV) from long-read sequencing and assembled contigs.
    """

    homepage = "https://github.com/WeichenZhou/PALMER"
    url = "https://github.com/WeichenZhou/PALMER/archive/refs/tags/V2.0.1.tar.gz"

    maintainers("harrysharma1")

    license("MIT", checked_by="harrysharma1")

    version("2.0.1", sha256="7c24c2480247bd287d915ca512a76705de1a6f8d9ef462b1cfeb34dba6bc43dd")
    version("1.6", sha256="838d8af6cecf50e585c7c598b3550d31661d453c57bb7cbc8ffe0e1d4388d7cb")
    version("1.3.0", sha256="31df88a7582a5ca51bea39ae6d3337163134fc590d9973ede066e2399dbcadcd")


    depends_on("htslib")
    depends_on("blast-plus@2.10:")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("PALMER", prefix.bin)