# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Novactf(Package):
    """
    NovaCTF is a freeware for 3D-CTF correction for electron microscopy, as described in this publication:
    Turoňová, B., Schur, F.K.M, Wan, W. and Briggs, J.A.G. Efficient 3D-CTF correction for cryo-electron tomography using NovaCTF improves subtomogram averaging resolution to 3.4 Å.
    (doi.org/10.1016/j.jsb.2017.07.007)
    """

    homepage = "https://github.com/turonova/novaCTF"
    git = "https://github.com/turonova/novaCTF.git"
    maintainers("harrysharma1")

    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("GPL-3.0", checked_by="harrysharma1")

    # version("1.2.3", md5="0123456789abcdef0123456789abcdef")
    version("master", branch="master")
    phases = ["build", "install"]

    depends_on("gmake", type="build")
    depends_on("fftw@3.3.10")

    def build(self, spec, prefix):
        make(
            "includepath={0}".format(spec["fftw"].prefix.include),
            "libpath={0}".format(spec["fftw"].prefix.lib)
        )

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("novaCTF", prefix.bin)