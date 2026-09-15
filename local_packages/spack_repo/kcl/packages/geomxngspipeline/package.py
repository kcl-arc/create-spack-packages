# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Geomxngspipeline(Package):
    """The GeoMx NGS Pipeline is used to process FASTQ sequencing files from Nanostring
    GeoMx libraries to produce digital count conversion (.dcc) files.
    """

    homepage = "https://nanostring.com/products/geomx-digital-spatial-profiler/geomx-dsp-overview/"

    maintainers = ['lzalewski']
    manual_download = True

    version('2.3.3.10', sha256='318dc6f7d9fc7e9204b92e14914320b16c967aecb8dc292518aacffd94837f1a')

    # The binary geomxngspipeline together with agreement_cli.txt and agreement_cli_yes
    # files have to be put in a tarball geomxngspipeline_2.3.3.10.tgz before the
    # installation can continue, .e.g.
    # tar -czvf geomxngspipeline_2.3.3.10.tgz agreement_cli.txt agreement_cli_yes geomxngspipeline
    def url_for_version(self, version):
        return "file:///software/local_software/geomxngspipeline/geomxngspipeline_{0}.tgz".format(version)

    def install(self, spec, prefix):
        install_tree(join_path(self.stage.source_path,'.'), prefix)

    def setup_run_environment(self, env):
        env.prepend_path('PATH', self.prefix)
