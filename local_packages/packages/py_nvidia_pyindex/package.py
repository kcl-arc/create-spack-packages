# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyNvidiaPyindex(PythonPackage):
    """
    This package adds the address of the NVIDIA Private Python Package Index to the user’s environment.
    """

    homepage = "https://pypi.org/project/nvidia-pyindex/"
    pypi = "nvidia-pyindex/nvidia-pyindex-1.0.9.tar.gz"

    maintainers("harrysharma1")

    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("Apache-2.0", checked_by="harrysharma1")

    version("1.0.9", sha256="22300a8d5aff35b047830f790a737437402d96e0794037102e796edbceb2fec6")

    depends_on("py-setuptools", type=("build", "run"))