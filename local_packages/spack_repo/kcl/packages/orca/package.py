# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import os

from spack import *


class Orca(Package):
    """ORCA is an ab initio quantum chemistry program package that contains modern electronic 
    structure methods including density functional theory, many-body perturbation, coupled cluster, 
    multireference methods, and semi-empirical quantum chemistry methods. Its main field of 
    application is larger molecules, transition metal complexes, and their spectroscopic properties. 
    ORCA is developed in the research group of Frank Neese. The free version is available only 
    for academic use at academic institutions. """

    homepage = "https://orcaforum.kofo.mpg.de/app.php/portal"
    manual_download = True

    version('6.0.1', sha256='5e9b49588375e0ce5bc32767127cc725f5425917804042cdecdfd5c6b965ef61',
             url="file:///software/local_software/orca/orca_6_0_1_linux_x86-64_shared_openmpi416.tar.xz")
    version('5.0.4', sha256='c4ea5aea60da7bcb18a6b7042609206fbeb2a765c6fa958c5689d450b588b036',
             url="file:///software/local_software/orca/orca_5_0_4_linux_x86-64_shared_openmpi411.tar.xz")
    version('5.0.3', sha256='9894c8c1fce3f4cd2bc7ac2291200c52235c692ca8bd7c7414ce587fb1c48902',
             url="file:///software/local_software/orca/orca_5_0_3_linux_x86-64_openmpi411.tar.xz")

    depends_on('openmpi@4.1.1', when='@5.0.3:5.0.4', type='run')
    depends_on('openmpi@4.1.6', when='@6.0.1', type='run')
    depends_on("libevent", type="run")
    # depends_on("libpciaccess", type="run")

    # def url_for_version(self, version):
    #     if version.string == "5.0.3":
    #         openmpiversion = "411"
    #     return "file:///software/local_software/orca/orca_{0}_linux_x86-64_openmpi{1}.tar.xz".format(version.underscore, openmpiversion)

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install_tree('.', prefix.bin)


    def setup_run_environment(self, env):
        env.prepend_path('PATH', self.prefix)
        env.prepend_path("LD_LIBRARY_PATH", self.prefix.bin)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["libevent"].prefix.lib)
        # env.prepend_path("LD_LIBRARY_PATH", self.spec["libpciaccess"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["openmpi"].prefix.lib)
