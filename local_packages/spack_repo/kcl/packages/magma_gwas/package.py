# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage
from spack.package import *


class MagmaGwas(MakefilePackage):
    """
    MAGMA is a tool for gene analysis and generalised gene-set analysis of GWAS data.
    It can be used to analyse both raw genotype data as well as summary SNP p-values from
    a previous GWAS or meta-analysis.
    """

    homepage = "https://cncr.nl/research/magma/"
    url = "https://vu.data.surf.nl/public.php/dav/files/1OOi7bxLWef0GwY/?accept=zip"

    maintainers("harrysharma1")

    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="harrysharma1")

    version("1.10", sha256="c744c662204e6888f007b1db2c54d608545f2e71a73e5b42bf43102597c178af", extension="zip")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("magma", prefix.bin)