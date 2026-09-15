# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import os

from spack.package import *


class Crest(Package):
    """Conformer-Rotamer Ensemble Sampling Tool based on the xtb
    Semiempirical Extended Tight-Binding Program Package"""

    homepage = "https://github.com/crest-lab/crest"
    url = 'https://github.com/crest-lab/crest/releases/download/v2.11.2/crest.zip'

    version('3.0.2', sha256='8e5bd18b06f99741ebd7bb71b3a996295f391b2f076aaeab739740f709e9554d',
            url='https://github.com/crest-lab/crest/releases/download/v3.0.2/crest-gnu-12-ubuntu-latest.tar.xz')
    version('2.12', sha256='c55e0f075a6223317b33a5f0fae593ce0ad55c1229c382937b0a0c2dcaf72ef6')
    version('2.11.2', sha256='8889dd8bba344cf5c5b3b7d16ab01d6d0429ce02c307b92ba6459a0840b25fc6')
    version('2.11.1', sha256='ef8769d62b4062d22f3739fe524f0f924208516b05935b747252b29b45f6f64b',
            url='https://github.com/crest-lab/crest/releases/download/v2.11.1/crest-binary-2.11.1.zip')

    # Dependencies
    depends_on('xtb@6.4.1:', type=('build', 'run'))

    def install(self, spec, prefix):
        install_tree('.', self.prefix)

    def setup_run_environment(self, env):
        env.prepend_path('PATH', join_path(self.prefix))
