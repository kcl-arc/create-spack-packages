# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import os

from spack.package import *

class Gurobi(Package):
    """Gurobi Optimizer"""

    homepage = "http://www.gurobi.com"
    manual_download = True

    maintainers = ['terryarter']
    url = "file:///software/local_software/gurobi/gurobi9.5.2_linux64.tar.gz".format(os.getcwd())

    version('9.5.2', sha256='95d8ca18b7f86116ba834a27fd6228c5b1708ae67927e7ea0e954c09374a2d0f')

    def install(self, spec, prefix):
        install_tree('.', self.prefix)

    def setup_run_environment(self, env):
      env.prepend_path('PATH', join_path(self.prefix, 'linux64/bin'))
      env.prepend_path('LD_LIBRARY_PATH', join_path(self.prefix, 'linux64/lib'))
      env.prepend_path('LIBRARY_PATH', join_path(self.prefix, 'linux64/lib'))
      env.prepend_path('INCLUDE', join_path(self.prefix, 'linux64/include'))
      env.prepend_path('INCLUDE_PATH', join_path(self.prefix, 'linux64/include'))
      env.prepend_path('C_INCLUDE_PATH', join_path(self.prefix, 'linux64/include'))
      env.prepend_path('CPLUS_INCLUDE_PATH', join_path(self.prefix, 'linux64/include'))

      env.set('GRB_LICENSE_FILE', join_path('/software/licenses/gurobi', 'gurobi.lic'))
