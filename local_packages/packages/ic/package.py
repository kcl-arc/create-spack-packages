# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Ic(Package):
    """
    ic is a set of programs designed to produce a single html page visual summary of one or more imputed data sets from the most common imputation programs.
    """

    homepage = "https://www.chg.ox.ac.uk/~wrayner/tools/Post-Imputation.html"
    url = "https://www.chg.ox.ac.uk/~wrayner/tools/ic.v1.0.9.zip"

    maintainers("harrysharma1")

    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="harrysharma1")

    version("1.0.9", sha256="39de6c55cb3f6c2a382fd8e33d369d357ea55ef2ed0861c6025abfda0fb45153")
    version("1.0.8", sha256="fb5cb7a38f51651f3ab1db9548aa8df54114f882e784023777907a6b627538ac", url="https://www.chg.ox.ac.uk/~wrayner/tools/ic.v1.0.8.zip")
    version("1.0.6", sha256="c5762fd594288d6f223fa21bb3bdc39842cafb676dad9bc3842a6fdfb620124c", url="https://www.chg.ox.ac.uk/~wrayner/tools/ic.v1.0.6.zip")
    version("1.0.5", sha256="f1babec8753b47ede41c9a14ff5c2c7fd9c223d1de011fddefe0acf0db3c7c4e", url="https://www.chg.ox.ac.uk/~wrayner/tools/ic.v1.0.5.zip")
    version("1.0.4", sha256="c90fd369988dffc0ec29da7e02ec36e2a4eead615c4a5cf3a593c1accde15443", url="https://www.chg.ox.ac.uk/~wrayner/tools/ic.v1.0.4.zip")
    version("1.0.3", sha256="230c827a83f2b390beee02c8d07cc316c2ea807594d0822648b00e2b89f2b6a5", url="https://www.chg.ox.ac.uk/~wrayner/tools/ic.v1.0.3.zip")
    version("1.0.2", sha256="c9f8c076af66c2060330b09e69fc977771a64b21ea3a9d0fd68d85d9ee882913", url="https://www.chg.ox.ac.uk/~wrayner/tools/ic.v1.0.2.zip")

    depends_on('perl', type='run')
    depends_on('perl-gd', type='run')
    depends_on('perl-gdgraph', type='run')

    @run_before("install")
    def filter_icscript(self):
        # filter replace which perl in main script
        FileFilter("ic.pl").filter("#!/usr/bin/perl", "#!/usr/bin/env perl")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        mv = which("mv")
        # rename program executable
        mv("ic.pl", "ic")
        install("ic", prefix.bin)

    def setup_run_environment(self, env):
        # add main ic script to path
        env.prepend_path("PATH", self.prefix)