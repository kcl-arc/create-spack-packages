# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import glob
import os

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Kraken2(Package):
    """Kraken2 is a system for assigning taxonomic labels to short DNA
    sequences, usually obtained through metagenomic studies."""

    homepage = "https://ccb.jhu.edu/software/kraken2/"
    url = "https://github.com/DerrickWood/kraken2/archive/v2.1.1.tar.gz"

    maintainers("rberg2")

    license("MIT")
    version("2.17.1", sha256="4dc64ead045b5ae9180731c260046aa37b6642244be085a9ba9b15db78ab442d")
    version("2.17", sha256="69380e7c22e314245cbe61b2a69d6719c95edadd80ad171577c1e681927c7b88")
    version("2.14", sha256="75ffbf82bd13232ec8d39990f48454c6f7d98ceb589af80a60c7e9ed046e7f18")
    version("2.1.6", sha256="5bbd79392ff7c530124986dfdfe126bf638477db94fb7a901ec2daf9261707f3")
    version("2.1.5", sha256="6feb9b1e0840a574598b84a3134a25622e5528ac6d0f4c756cdab629275d8f42")
    version("2.1.3", sha256="5269fa14adfb02e38c2da2e605e909a432d76c680d73e2e0e80e27ccd04d7c69")
    version("2.1.2", sha256="e5f431e8bc3d5493a79e1d8125f4aacbad24f9ea2cc9657b66da06a32bef6ff3")
    version("2.1.1", sha256="8f3e928cdb32b9e8e6f55b44703d1557b2a5fc3f30f63e8d16e465e19a81dee4")
    version("2.1.0", sha256="c2a3f6acd3fff0e298aff41a486700e8984854e47226c9595d528f44b01f71b2")
    version(
        "2.0.9-beta", sha256="0287cf4df4b5d5511a9132d9ab37a8d76864bae445579efb9cb76db7e9c09eba"
    )
    version(
        "2.0.8-beta", sha256="f2a91fc57a40b3e87df8ac2ea7c0ff1060cc9295c95de417ee53249ee3f7ad8e"
    )
    version(
        "2.0.7-beta", sha256="baa160f5aef73327e1a79e6d1c54b64b2fcdaee0be31b456f7bc411d1897a744"
    )
    version(
        "2.0.6-beta", sha256="d77db6251179c4d7e16bc9b5e5e9043d25acf81f3e32ad6eadfba829a31e1d09"
    )

    depends_on("cxx", type="build")  # generated
    depends_on("c", type="build")
    depends_on("perl", type=("build", "run"))
    depends_on("rsync", type=("run"))
    depends_on("wget", type=("run"))

    def patch(self):
        if self.spec.satisfies("@:2.1.0"):
            for header in ["src/hyperloglogplus.h", "hyperloglogplus.h"]:
                if os.path.exists(header):
                    filter_file(
                        "#include<unordered_set>",
                        "#include<unordered_set>\n#include <cstdint>\n#include <limits>\n#include <iterator>",
                        header,
                    )

    def install(self, spec, prefix):
        installer = Executable("./install_kraken2.sh")
        installer(self.stage.source_path)
        mkdirp(prefix.bin)
        files = glob.iglob("*")
        for file in files:
            if os.path.isfile(file):
                install(file, prefix.bin)