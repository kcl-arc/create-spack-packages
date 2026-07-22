# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Maeparser(CMakePackage):
    """Parser for Schrodinger Maestro files"""

    homepage = "https://github.com/schrodinger/maeparser"
    url = "https://github.com/schrodinger/maeparser/archive/refs/tags/v1.3.0.tar.gz"

    maintainers("RMeli")

    license("MIT")

    version("1.3.3", sha256="78e7571a779ea4952e752ecef57c62fb26463947e29ef7f4b31b11988d88ca07")
    version("1.3.2", sha256="431ae029957534324b59eb3974486f3cad97d06e9bacd88ec94dc598046dfcd3")
    version("1.3.1", sha256="a8d80f67d1b9be6e23b9651cb747f4a3200132e7d878a285119c86bf44568e36")
    version("1.3.0", sha256="fa8f9336de1e5d1cabec29a6da04547b1fb040bb32ba511ff30b4a14097c751c")
    version("1.2.4", sha256="c62d5846c85a2982cfa8895ffbed8a6ce57678d936ddfebf429546fab4b0a36d")
    version("1.2.3", sha256="ca2e2dead8a1fdd74b624ca0f0c4dde205d0b8abbbfdd62de0786f2d3f6f291c")
    version("1.2.2", sha256="e65dec4dd8b2c633d9c43711eccd6dfa3c4df6383ec32aeffd21a96d465f5fe7")
    version("1.2.1", sha256="5469a8b42616d8239ff00041058209d98abc759818c985135883328be85306ac")
    version("1.2", sha256="411f48a4ae794174b8ffa0230a3b426142f7fcb0a418feb30074a142182a87ab")
    version("1.1", sha256="acd592a599f1daa045255b1f11d138b91b8e1070ca4048428da3fb9ff25d0198")


    variant(
        "shared",
        default=True,
        description="Build maeparser as a shared library (turn off for a static one)",
    )

    depends_on("c", type="build")
    depends_on("cxx", type="build")  # generated

    depends_on("boost +iostreams +filesystem +test")
    depends_on("zlib-api")

    def cmake_args(self):
        args = [self.define_from_variant("MAEPARSER_BUILD_SHARED_LIBS", "shared")]
        return args
