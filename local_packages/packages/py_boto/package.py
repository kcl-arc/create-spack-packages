# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyBoto(PythonPackage):
    """Boto is a Python package that provides interfaces to
    Amazon Web Services."""

    homepage = "https://github.com/boto/boto"
    url = "https://github.com/boto/boto/archive/2.49.0.tar.gz"

    license("MIT")

    version("2.49.0", sha256="3dbefd4f4542f85a323d4f54601f31ed4d362fc87945245f32e4a85029513314")

    # boto 2.49.0 is legacy and fails to build with modern Python/setuptools
    # combinations used in this stack (e.g. python@3.14 + setuptools@80).
    depends_on("python@2.6:3.11", type=("build", "run"))
    depends_on("py-setuptools@:57", type="build")