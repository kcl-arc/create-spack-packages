# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class XplorNih(Package):
    """XPLOR-NIH is a structure determination program.

    Note: A manual download is required for XPLOR-NIH.
    Spack will search your current directory for the download file.
    Alternatively, add this file to a mirror so that Spack can find it.
    For instructions on how to set up a mirror, see
    https://spack.readthedocs.io/en/latest/mirrors.html"""

    homepage = "https://nmr.cit.nih.gov/xplor-nih/"
    # manual_download = True

    version("3.11.1", md5="7be143d87a3405ae56c9cc6f59228b9b")
    version("3.8", md5="9cd295cadb3843651a5819125b63b31a")

    depends_on("python", type=("build", "run"))

    def url_for_version(self, version):
        return "file:///software/local_software/xplor/xplor-nih-{0}-Linux_x86_64.tar.gz".format(version)

    def install(self, spec, prefix):
        install_tree(self.stage.source_path, prefix.bin)