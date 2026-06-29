# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.perl import PerlPackage

from spack.package import *


class PerlTemplateToolkit(PerlPackage):
    """Template - Front-end module to the Template Toolkit."""

    homepage = "https://metacpan.org/pod/Template"
    url = "https://cpan.metacpan.org/authors/id/A/AB/ABW/Template-Toolkit-3.101.tar.gz"

    maintainers("ChristopherChristofi")

    version("3.102", sha256="d161c89dee9b213a7c55709ea782e2dd5923dbd1215b9576612889e6e74a2e06", url="https://cpan.metacpan.org/authors/id/T/TO/TODDR/Template-Toolkit-3.102.tar.gz")
    version("3.101", sha256="d2a32dd6c21e4b37c6a93df8087ca9e880cfae613a3e5efaea307b0bdcaedb58")

    depends_on("perl-extutils-makemaker", type=("build"))
    depends_on("perl-appconfig@1.56:")
    depends_on("perl-pathtools@0.8:")
    depends_on("perl-file-temp@0.12:")
    depends_on("perl-test-leaktrace", type=("build", "test"))

    def configure_args(self):
        args = ["TT_QUIET=y", "TT_ACCEPT=y"]
        return args