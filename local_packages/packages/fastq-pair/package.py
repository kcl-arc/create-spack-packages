# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class FastqPair(CMakePackage):
    """
    Rewrite paired end fastq files to make sure that all reads have a mate and to separate out singletons.
    """

    homepage = "https://edwards.flinders.edu.au/sorting-and-paring-fastq-files/"
    url = "https://github.com/linsalrob/fastq-pair/archive/refs/tags/v1.0.tar.gz"

    maintainers("harrysharma1")

    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("MIT", checked_by="harrysharma1")

    version("1.0", sha256="74fd5bae4d85cc02245ff1b03f31fa3788c50966d829b107076a806ae061da3b")
    depends_on('cmake@3.6', type='build')