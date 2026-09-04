# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class FastqTools(AutotoolsPackage):
    """
    This package provides a number of small and efficient programs to perform common tasks with high throughput sequencing data in the FASTQ format.
    All of the programs work with typical FASTQ files as well as gzipped FASTQ files.
    """

    homepage = "https://github.com/dcjones/fastq-tools"
    url = "https://github.com/dcjones/fastq-tools/archive/refs/tags/v0.8.3.tar.gz"

    maintainers("teachers-uk-net", "terryarter")

    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("MIT", checked_by="harrysharma1")

    version("0.8.3", sha256="0cd7436e81129090e707f69695682df80623b06448d95df483e572c61ddf538e")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
    depends_on('pcre')
    depends_on('zlib-api')


    def autoreconf(self, spec, prefix):
        autoreconf("--install", "--verbose")