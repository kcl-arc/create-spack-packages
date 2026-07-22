# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Susiex(MakefilePackage):
    """
    SuSiEx is a C++ based command line tool that performs cross-ancestry fine-mapping using GWAS summary statistics and LD reference panels.
    The method is built on the Sum of Single Effects (SuSiE) model:
    Wang, G., Sarkar, A., Carbonetto, P. & Stephens, M. A simple new approach to variable selection in regression, with application to genetic fine mapping.
    J. R. Stat. Soc. Series B Stat. Methodol. 82, 1273–1300 (2020). https://doi.org/10.1111/rssb.12388
    """

    homepage = "https://github.com/getian107/SuSiEx"
    url = "https://github.com/getian107/SuSiEx/archive/refs/tags/v1.1.2.tar.gz"
    build_directory = "src"

    maintainers("harrysharma1")

    license("MIT", checked_by="harrysharma1")

    version("1.1.2", sha256="87bb8bb6dcc73dce00e9be694e5eadc106b070eb2e05b71244a1d5a7fcde07d2")
    version("1.1.1", sha256="f2c212e524ef0c87423b60a4404e2a56143ff5843d89275692a591b6a959cab1")
    version("1.1.0", sha256="b67dca665e05b1e2a715033c29ad1485b8b3408edcf758d6f5f31a3bd202662c")

    patch("isnan_data.patch", when="@1.1.0")
    patch("isnan_model.patch", when="@1.1.0")

    def install(self, spec, prefix):
        install_tree("bin", prefix.bin)
        install_tree("examples", join_path(prefix, "examples"))
        install_tree("utilities", join_path(prefix, "utilities"))