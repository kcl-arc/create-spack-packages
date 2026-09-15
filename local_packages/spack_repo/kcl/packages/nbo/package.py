# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Nbo(Package):
    """The Natural Bond Orbital (NBO) program NBO 7.0 is a discovery tool for chemical insights from complex wavefunctions.
    ============================= IMPORTANT ===============================\n
       Cite this program [NBO 7.0.10 (8-Feb-2021)] as:\n
       NBO 7.0.  E. D. Glendening, J. K. Badenhoop, A. E. Reed,
       J. E. Carpenter, J. A. Bohmann, C. M. Morales, P. Karafiloglou,
       C. R. Landis, and F. Weinhold, Theoretical Chemistry Institute,
       University of Wisconsin, Madison, WI (2018)\n
       =======================================================================
       """

    homepage = "https://nbo6.chem.wisc.edu/"
    manual_download = True

    version("7.0", sha256="83ffa9891f45d4befbdfc3481d9107583958f2265b3a0c92f6bb7b00510e86a4")

    depends_on("tcsh")

    def url_for_version(self, version):
        return "file:///software/local_software/nbo/nbo{0}-bin-linux-x64.tar.gz".format(version)

    def install(self, spec, prefix):
        install_tree(".", prefix)

        tcsh = which("tcsh")
        
        f = FileFilter(join_path(self.prefix, "gennbo"))
        f.filter("/bin/tcsh", str(tcsh))
        f.filter('setenv NBOBIN ./bin', 'setenv NBOBIN {0}'.format(self.prefix.bin))

        testf = FileFilter(join_path(self.prefix, "tests/gennbo/gennbo"))
        testf.filter("/bin/tcsh", str(tcsh))
        testf.filter('setenv NBOBIN ../../bin', 'setenv NBOBIN {0}'.format(self.prefix.bin))

    def setup_run_environment(self, env):
        env.prepend_path('PATH', self.prefix)
