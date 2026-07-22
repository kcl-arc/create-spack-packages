# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Cellranger(Package):
    """Cellranger is a set of analysis pipelines that process Chromium single cell data to
    align reads, generate feature-barcode matrices, perform clustering and other secondary
    analysis, and more.

    This package requires the user to accept a license and to download the tarball manually.
    Once downloaded, the file should be placed within a manual mirror or within the current
    directory. For instructions on making a manual mirror, see
    https://spack.readthedocs.io/en/latest/mirrors.html"""

    homepage = "https://www.10xgenomics.com/support/software/cell-ranger/latest"
    manual_download = True
    license_url = "support.10xgenomics.com/license"

    version("10.0.0", sha256="5af205246be97ee0baed52d149f60b3730dc663acaf5ed738c2833d947689859")
    version("9.0.0", sha256="157002eee6a2b4abfb8b74fa74cb751a4c0543150812fc4bac982abc7cdcea88")
    version("8.0.0", sha256="a169e03d89bcbfd9193a3e11e289436b40441380a421032e1724591db61cd690")
    version("7.2.0", sha256="3e9fac03cc33c81a10f6444963e87bf720b2fdee0565d0620f5a4bb47d62a7e3")

    # cellranger is distributed as precompiled binaries that are not compatible with
    # processors without the avx instruction set ...
    conflicts("target=:k10")  # last AMD processor not to support avx
    conflicts("target=:westmere")  # last Intel processor not to support avx
    conflicts("target=:x86_64_v2")  # last generic architecture not to support avx

    def url_for_version(self, version):
        return "file:///software/local_software/cellranger/cellranger-{0}.tar.gz".format(version)

    def install(self, spec, prefix):
        install_tree(".", prefix)