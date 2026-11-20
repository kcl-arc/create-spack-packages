# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Dentist(Package):
    """
    DENTIST (Detecting Errors iN analyses of summary staTISTics) is a quality control (QC) tool for summary-level data from genome-wide association studies (GWASs).
    It leverages the difference between the observed GWAS test-statistic of a variant and its predicted value (using the neighbouring variants and linkage equilibrium (LD)
    data from a reference panel) to remove problematic variants. It can detect genotyping/imputation errors in either the original GWAS or the LD reference samples, allelic
    errors (i.e., the effect alleles of the variants are mislabelled) in the GWAS summary data, as well as heterogeneity between the GWAS and LD reference samples.
    As shown in our paper, DENTIST can significantly improve the performance of the summary-data based conditional and jointly association analysis (COJO; Yang et al. 2012 Nat Genet)
    especially for rare variants. It can also improve the performance of LD score regression (LDSC; Builk-Sulivant et al. 2015 Nat Genet) and SMR-HEIDI (Zhu et al. 2015 Nat Genet).
    We believe that DENTIST can in principle work for all analyses that use GWAS summary data, although this has not been tested extensively.
    Apart from its application to summary data based analyses, DENTIST can also be used in complementary to the conventional QCs in GWAS with individual-level data.
    """

    homepage = "https://github.com/Yves-CHEN/DENTIST"

    maintainers("harrysharma1")

    license("LGPL-3.0", checked_by="harrysharma1")

    version("1.3.0.0", sha256="a0a91c9f50e013a4d5b39e7c5097d83f58784e62d8188520f75839f737616d29")
    version("1.2.0.0", sha256="04834162cdb81c7c8b986f98a1b495a4aa667b14993e2a104e345ac991e00dbf")
    version("1.1.0.0", sha256="5d0e45f4ba826ae4cf588c8bf344712c4fab187a59dbba7e6ba85b4d759fad83")


    depends_on("boost")
    depends_on("eigen")
    depends_on("intel-oneapi-mkl +shared threads=openmp")


    def url_for_version(self, version):
        return "file:///software/local_software/DENTIST/DENTIST_{0}.gz".format(version)

    @run_before("install")
    def fix_filename(self):
        version = str(self.spec.version)
        with working_dir(self.stage.source_path):
            os.rename("DENTIST_{0}".format(version), "DENTIST")
            os.chmod("DENTIST", 0o775)

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install_tree(join_path(self.stage.source_path,'.'), prefix.bin)