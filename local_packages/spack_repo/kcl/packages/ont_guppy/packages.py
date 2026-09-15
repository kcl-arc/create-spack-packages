# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
from spack import *


class OntGuppy(Package, CudaPackage):
    """
    Guppy is a data processing toolkit that contains the Oxford Nanopore Technologies' production\
    basecalling algorithms and several bioinformatic post-processing features.
    \n
    ============================= IMPORTANT ===============================\n
    The use of guppy is restricted to users registered with Oxford Nanopore Technologies.
    https://community.nanoporetech.com/downloads
    Please email the CREATE support Team before access can be granted.\n
    =======================================================================."""

    homepage = "https://community.nanoporetech.com/protocols/Guppy-protocol/v/1/guppy-software-overview"
    manual_download = True

    version('6.4.6', sha256='a633b2f0712781ff303a4c8fecb08d5e5603c755d6c445a6181ab11930f5bd63')

    variant("cuda", default=True)
    depends_on('cuda', when='+cuda')

    def url_for_version(self, version):
        return "file:///software/local_software/ont-guppy/ont-guppy_{}_linux64.tar.gz".format(version)

    @run_after('install')
    def fix_eula_filename(self):
        if self.version == Version('6.4.6'):
            with working_dir(self.prefix.bin):
                # Replace spaces in filename
                os.rename('Guppy End User License Agreement 17Feb22.pdf', 'Guppy_End_User_License_Agreement_17Feb22.pdf')

    def install(self, spec, prefix):
        install_tree(".", prefix)

    def setup_run_environment(self, env):
        if self.version == Version('6.4.6'):
            # Set environment variables that can be used to extend the printed modulefile information.
            env.set('ONT_GUPPY_FULL_VERSION', 'Version 6.4.6+ae70e8f, minimap2 version 2.24-r1122')
            env.set('ONT_GUPPY_EULA_LICENSE', join_path(self.prefix.bin, 'Guppy_End_User_License_Agreement_17Feb22.pdf'))
