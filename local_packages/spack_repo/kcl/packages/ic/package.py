# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Ic(Package):
    """
    ic is a set of programs designed to produce a single html page visual summary of one or more imputed data sets from the most common imputation programs.
    """

    homepage = "https://www.strand.org.uk/tools/index.html"

    maintainers("harrysharma1")

    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="harrysharma1")

    version("1.0.11", sha256="719010e4fa6aa6088da4eeba9f38010fbd3ec1efbf7b3edf8d5a755f8a1bed18")
    version("1.0.10", sha256="0fd8f627731a23c9dbdc8568b497f9d6378e980bbd5a569aabe1e064958fa333")
    version("1.0.9", sha256="39de6c55cb3f6c2a382fd8e33d369d357ea55ef2ed0861c6025abfda0fb45153")
    version("1.0.8", sha256="fb5cb7a38f51651f3ab1db9548aa8df54114f882e784023777907a6b627538ac")

    depends_on('perl', type='run')
    depends_on('perl-gd', type='run')
    depends_on('perl-gdgraph', type='run')

    def url_for_version(self, version):
        # 1.0.10+ are published with an uppercase "IC" prefix
        prefix = "IC" if version >= Version("1.0.10") else "ic"
        return "https://www.strand.org.uk/tools/{0}.v{1}.zip".format(prefix, version)

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