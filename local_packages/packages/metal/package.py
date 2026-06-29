# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage, CMakeBuilder
from spack_repo.builtin.build_systems.makefile import MakefilePackage, MakefileBuilder

import os
from spack.package import *

class Metal(MakefilePackage, CMakePackage):
    """METAL is a tool for the meta-analysis of genome-wide association studies"""

    homepage = "https://genome.sph.umich.edu/wiki/METAL"
    url = "https://github.com/statgen/METAL/archive/refs/tags/2020-05-05.tar.gz"

    license("BSD-3-Clause")

    version(
        "2020-05-05", sha256="0ffa2419ca2ab43766e7e6e8c97822c8ce1f5b6233fb5f992d1b1be1955fede7"
    )
    version("2018-08-28", sha256="a6f0d91583d18483e1edaaab6271ca851397d1c612b25865a44141bea70b7580")
    version("2017-12-21", sha256="cbb7336c0cfbec087ae76ec1dbaee33a7cb5c5327006f233176e1ed3ab99f033")
    version("2011-03-25", url= "https://csg.sph.umich.edu/abecasis/Metal/download/generic-metal-2011-03-25.tar.gz", sha256="c301456c85a613980c522b47ef2669b81c3afd426bd5a52ac0f5a90e180460ae")

    build_system(
        conditional("cmake", when="@2017-12-21:"),
        conditional("makefile", when="@:2011-03-25"),
        default="makefile",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("gmake", type="build", when="build_system=makefile")
    depends_on("cmake@3.1:", type="build", when="build_system=cmake")
    depends_on("zlib-ng")

class CMakeBuilder(CMakeBuilder):
    @run_after("install")
    def mv_binary(self):
        with working_dir(self.build_directory):
            install_tree("bin", self.prefix.bin)

class MakefileBuilder(MakefileBuilder):
    def edit(self, pkg, spec, prefix):
        cxx = os.environ.get("CXX", "g++")
        makefile = FileFilter("Makefile")
        makefile.filter(r"^\s*CXX\s*=.*", "CXX = {0} -std=c++11".format(cxx))

    def install(self, pkg, spec, prefix):
        make()
        prefix_arg = "INSTALLDIR={}".format(prefix.bin)
        make("install", prefix_arg)

    def setup_run_environment(self, env):
        env.prepend_path('PATH', self.prefix)