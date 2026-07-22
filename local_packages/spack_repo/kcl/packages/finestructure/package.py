# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Finestructure(Package):
    """
    fineSTRUCTURE is a fast and powerful algorithm for identifying population structure using dense sequencing data.
    By using the output of ChromoPainter as a (nearly) sufficient summary statistic, it is able to perform model-based
    Bayesian clustering on large datasets, including full resequencing data, and can handle up to 1000s of individuals.
    Full assignment uncertainty is given.
    """

    homepage = "https://people.maths.bris.ac.uk/~madjl/finestructure/index.html"
    url = "https://people.maths.bris.ac.uk/~madjl/finestructure/fs_4.1.1.zip"

    maintainers("teachers_uk_net")

    version("4.1.1", sha256="7af2dd51b02bf117e364f70e76d03920b0cd9ec17111b5be94dd2a5ab906b75e")


    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install_tree(join_path(self.stage.source_path,'.'), prefix.bin)

    @run_after("install")
    def for_linux(self):
        with working_dir(self.prefix.bin):
            symlink("fs_linux_glibc2.3", "fs")