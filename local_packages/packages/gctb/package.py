# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Gctb(Package):
    """
    GCTB is a software tool that comprises a family of Bayesian linear mixed models for complex trait analyses using genome-wide SNPs.
    It was developed to simultaneously estimate the joint effects of all SNPs and the genetic architecture parameters for a complex trait,
    including SNP-based heritability, polygenicity and the joint distribution of effect sizes and minor allele frequencies.
    Version 2.0 or above of the GCTB software includes summary-data-based versions of the individual-level data Bayesian linear mixed models previsouly implemented.
    """

    homepage = "https://cnsgenomics.com/software/gctb/"
    url = "https://gctbhub.cloud.edu.au/software/gctb/download/gctb_2.5.5_Linux.zip"

    maintainers("harrysharma")

    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("MIT", checked_by="harrysharma1")

    version("2.5.5", sha256="ccc2752e1bc0d4a210bd9592d07c44468891677f8b2d5fc0a37aa2119c24c61f")
    version("2.04.3", sha256="562727d9ae830a02dfe32e576686d5ae72dd41617f30415b6759c5daa75f4468", url="https://cnsgenomics.com/software/gctb/download/gctb_2.04.3_Linux.zip")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        if spec.version == Version("2.04.3"):
            install("gctb_2.04.3_Linux/gctb", prefix.bin)
        if spec.version == Version("2.5.5"):
            install("gctb_2.5.5_Linux/gctb", prefix.bin)