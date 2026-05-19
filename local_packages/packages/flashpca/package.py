# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class Flashpca(Package):
    """
    FlashPCA performs fast principal component analysis (PCA) of single nucleotide polymorphism (SNP) data, similar to smartpca
    from EIGENSOFT (http://www.hsph.harvard.edu/alkes-price/software/) and shellfish (https://github.com/dandavison/shellfish).
    FlashPCA is based on the https://github.com/yixuan/spectra/ library.
    """

    homepage = "https://github.com/gabraham/flashpca"
    url = "https://github.com/gabraham/flashpca/releases/download/v2.0/flashpca_x86-64.gz"

    maintainers("harrysharma1")

    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("GPL-3.0", checked_by="harrysharma1")

    version("2.0", sha256="87f523e8d64a447797f4ca50e09725245d80c108e8283bf632bfb3e71fbb3d02")

    @run_before("install")
    def fix_filename(self):
        with working_dir(self.stage.source_path):
            os.rename("flashpca_x86-64", "flashpca")
            os.chmod("flashpca", 775)

    def install(self, spec, prefix):
       mkdirp(prefix.bin)
       install_tree(join_path(self.stage.source_path,'.'), prefix.bin)