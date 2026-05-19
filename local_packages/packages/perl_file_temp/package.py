# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.perl import PerlPackage

from spack.package import *


class PerlFileTemp(PerlPackage):
    """File::Temp - return name and handle of a temporary file safely."""

    homepage = "https://metacpan.org/pod/File::Temp"
    url = "https://cpan.metacpan.org/authors/id/E/ET/ETHER/File-Temp-0.2311.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("0.2312", sha256="6fa961d955cf84d5b87f2f219a723cf77cb44b79282793f6819ccb19e8d0b884", url="https://cpan.metacpan.org/authors/id/E/ET/ETHER/File-Temp-0.2312.tar.gz")
    version("0.2311", sha256="2290d61bf5c39882fc3311da9ce1c7f42dbdf825ae169e552c59fe4598b36f4a")