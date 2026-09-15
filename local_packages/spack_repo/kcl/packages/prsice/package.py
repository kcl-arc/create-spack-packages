# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import os

from spack import *

class Prsice(Package):
    """PRSice (pronounced 'precise') is a software package for calculating, applying, 
    evaluating and plotting the results of polygenic risk scores (PRS). PRSice can run 
    at high-resolution to provide the best-fit PRS as well as provide results calculated 
    at broad P-value thresholds, illustrating results corresponding to either, can thin 
    SNPs according to linkage disequilibrium and P-value ("clumping"), and can be applied 
    across multiple traits in a single run.

    Based on a permutation study we estimate a significance threshold of P = 0.001 for 
    high-resolution PRS analyses - the work on this is included in our Bioinformatics 
    paper on PRSice.

    PRSice is a software package written in R and C++. PRSice runs as a command-line 
    program with a variety of user-options and is freely available for download below, 
    compatible for Unix/Linux/Mac OS """

    homepage = "https://github.com/choishingwan/PRSice"
    manual_download = True

    maintainers = ['terryarter']
    #url = "file://{0}/PRSice_linux_{1}.zip".format(os.getcwd(), version)

    version('2.3.5', sha256='25a143edcf966225abf7b716aeff04b9386317973a981e3f1cc533ae48d6cae7')


    def url_for_version(self, version):
        return "file:///software/local_software/PRSice/PRSice_linux_{1}.zip".format(os.getcwd(), version)

    def install(self, spec, prefix):
        install_tree('.', self.prefix)

    def setup_run_environment(self, env):
      env.prepend_path('PATH', join_path(self.prefix, 'bin'))
