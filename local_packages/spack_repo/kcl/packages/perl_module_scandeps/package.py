# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.perl import PerlPackage

from spack.package import *


class PerlModuleScandeps(PerlPackage):
    """Module::ScanDeps - Recursively scan Perl code for dependencies"""

    homepage = "https://metacpan.org/pod/Module::ScanDeps"
    url = "https://cpan.metacpan.org/authors/id/R/RS/RSCHUPP/Module-ScanDeps-1.31.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("1.37", sha256="1f5e119cade1466c39c71e5bc35a8d4f4e672635db03d79a5a0dcf08c4e2b5a3")
    version("1.35", sha256="e5beb3adf55be3dab71f9a1416d4bad57b14e5e05c96370741b9d8f96a51b612")
    version("1.34", sha256="cac530e5cfc413e067797c7d237c6c5cd32915c3d9faee5d94035c8f3a8550eb")
    version("1.33", sha256="55bde24e3b966ebe261e10bdc6720259d331e63a4d2fc086ce551987a5bbbb4c")
    version("1.32", sha256="7ab3556ccaa812298da33f0a0515037cd513b9e72c42a76d2c2e4d28832215f0")
    version("1.31_004", sha256="0cd422f14b1cc9b8455c70d4343261099f19b23dd428cbfad9fda9213a352b7e")
    version("1.31_003", sha256="b3f3931f901dde7fa86131a67007aa959ef07ad5c94811754e736ab7849132cf")
    version("1.31_002", sha256="02e59242a045bee19738598e14174e540e6bdbd43ad5bf8ea16d32c33042aeb6")
    version("1.31_001", sha256="d0fa6dd23f4a3cc0ce96e0d9d24233ad168fe6492a075ea9f613585511eb34d9")
    version("1.31", sha256="fc4d98d2b0015745f3b55b51ddf4445a73b069ad0cb7ec36d8ea781d61074d9d")