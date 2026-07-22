# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Regenie(Package):
    """Mbatchou, J., Barnard, L., Backman, J. et al. Computationally efficient whole-genome regression for
    quantitative and binary traits. Nat Genet 53, 1097–1103 (2021)"""

    homepage = "https://github.com/rgcgithub/regenie"

    version("3.2.4",
            sha256="8ba436a3c4af58fb4b64bf39e130c7211610ab71366437b7c3c86c15f1dd5584",
            url="https://github.com/rgcgithub/regenie/releases/download/v3.2.4/regenie_v3.2.4.gz_x86_64_Linux.zip"
            )


    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        if spec.version == Version("3.2.4"):
            install("regenie_v3.2.4.gz_x86_64_Linux", prefix.bin)
