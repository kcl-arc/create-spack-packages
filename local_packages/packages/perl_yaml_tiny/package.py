# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.perl import PerlPackage

from spack.package import *


class PerlYamlTiny(PerlPackage):
    """YAML::Tiny - Read/Write YAML files with as little code as possible"""

    homepage = "https://metacpan.org/pod/YAML::Tiny"
    url = "https://cpan.metacpan.org/authors/id/E/ET/ETHER/YAML-Tiny-1.73.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("1.76", sha256="a8d584394cf069bf8f17cba3dd5099003b097fce316c31fb094f1b1c171c08a3")
    version("1.75", sha256="de1b13affad57ae8493e755adef5b0ce0fd028956ea8c6faba7df8bbe181d646", url="https://cpan.metacpan.org/authors/id/E/ET/ETHER/YAML-Tiny-1.75.tar.gz")
    version("1.74", sha256="7b38ca9f5d3ce24230a6b8bdc1f47f5b2db348e7f7f9666c26f5955636e33d6c")
    version("1.73", sha256="bc315fa12e8f1e3ee5e2f430d90b708a5dc7e47c867dba8dce3a6b8fbe257744")