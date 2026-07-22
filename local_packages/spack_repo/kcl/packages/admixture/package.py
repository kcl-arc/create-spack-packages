# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Admixture(Package):
    """
    ADMIXTURE is a software tool for maximum likelihood estimation of individual ancestries
    from multilocus SNP genotype datasets. It uses the same statistical model as STRUCTURE
    but calculates estimates much more rapidly using a fast numerical optimization algorithm.
    """

    homepage = "https://dalexander.github.io/admixture/download.html"
    url = "https://dalexander.github.io/admixture/binaries/admixture_linux-1.3.1.tar.gz"

    maintainers("harrysharma1")

    
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("CC-BY-1.0", checked_by="harrysharma1")

    version("1.3.1", sha256="4ae3bdd48fa057420c4e6e3c22850d37bec816c27dc88a9ccfb79649af6b3f73")
    version("1.3.0", sha256="353e8b170c81f8d95946bf18bc78afda5d6bd32645b2a68658bd6781ff35703c", url="https://dalexander.github.io/admixture/binaries/admixture_linux-1.3.0.tar.gz")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install_tree(self.stage.source_path, prefix.bin)