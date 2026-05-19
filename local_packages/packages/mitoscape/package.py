# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Mitoscape(Package):
    """
    A big-data, machine-learning workflow for obtaining mtDNA sequence from NGS data.
    """

    homepage = "https://github.com/larryns/MitoScape"
    url = "https://github.com/larryns/MitoScape/releases/download/v1.0/MitoScape-1.0.jar"

    maintainers("harrysharma1")

    license("Apache-2.0", checked_by="harrysharma1")

    version("1.0", sha256="03bc59ea2affcfc07ab4dd48c11c52b20d5ac8f15ebcf25b6d4bafeff434785a", expand=False)

    depends_on("java@8", type="run")

    @property
    def jar_mitoscape(self):
        return join_path(self.prefix, "lib", "MitoScape-1.0.jar")

    def install(self, spec, prefix):
        mkdirp(prefix.lib)
        install("MitoScape-1.0.jar", prefix.lib)

    def setup_run_environment(self, env):
        env.set("JAVA_HOME", self.spec["java"].prefix)
        env.set("MITOSCAPE_JAR", self.jar_mitoscape)