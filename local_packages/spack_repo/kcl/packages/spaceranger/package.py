# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Spaceranger(Package):
    """Space Ranger is a set of analysis pipelines that process 10x Genomics Visium
    data with brightfield or fluorescence microscope images, allowing users to map
    the whole transcriptome in a variety of tissues.
       \n
       ============================= IMPORTANT ===============================\n
       The use of spaceranger is restricted to users who own a 10x instrument
       and have registered for a download at
       https://support.10xgenomics.com/single-cell-gene-expression/software/downloads/latest
       Proof must be provided to the CREATE Support Team before access can be granted.
       Please email the relevant details via the ticket.\n
       =======================================================================
    """

    homepage = "https://www.10xgenomics.com/support/software/space-ranger/latest"
    manual_download = True

    version("3.0.0", sha256="2806951004828394a4ffd9087e68126c1e8c52fb98368e43d509b0049c3a9e4b")

    def url_for_version(self, version):
        return "file:///software/local_software/spaceranger/spaceranger-{0}.tar.gz".format(version)

    def install(self, spec, prefix):
        install_tree(join_path(self.stage.source_path, '.'), prefix)

    def setup_run_environment(self, env):
        env.prepend_path('PATH', self.prefix)
