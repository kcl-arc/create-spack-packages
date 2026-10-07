# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMlDtypes(PythonPackage):
    """A stand-alone implementation of several NumPy dtype extensions
    used in machine learning libraries."""

    homepage = "https://github.com/jax-ml/ml_dtypes"
    pypi = "ml_dtypes/ml_dtypes-0.3.1.tar.gz"
    git = "https://github.com/jax-ml/ml_dtypes.git"
    submodules = True

    license("Apache-2.0")

    version("0.5.1", tag="v0.5.1", commit="560866cfbb44990c9c68b82e878bf8ee7972a595")
    version("0.4.0", tag="v0.4.0", commit="9fc7e6773acb66fa496ed8d476a008a489a4da49")
    version("0.3.1", tag="v0.3.1", commit="bbeedd470ecac727c42e97648c0f27bfc312af30")
    version("0.2.0", tag="v0.2.0", commit="5b9fc9ad978757654843f4a8d899715dbea30e88")

    depends_on("cxx", type="build")

    depends_on("python@3.9:", when="@0.3:", type=("build", "link", "run"))
    depends_on("py-numpy@1.21:", type=("build", "link", "run"))
    # https://github.com/jax-ml/ml_dtypes/pull/143
    depends_on("py-numpy@:1", when="@:0.3", type=("build", "link", "run"))
    # Build dependencies are overconstrained, older versions work just fine
    depends_on("py-pybind11", when="@:0.3.1", type=("build", "link"))
    depends_on("py-setuptools", type="build")

    # ml_dtypes 0.5.x bundles Eigen 7bf2968, whose AVX512-FP16 code (enabled by
    # -march=sapphirerapids) doesn't compile with GCC 13+. Backport of Eigen 8025683:
    # https://gitlab.com/libeigen/eigen/-/issues/2835
    # filter_file, not a .patch: this header has CRLF line endings.
    @when("@0.5")
    def patch(self):
        header = "third_party/eigen/Eigen/src/Core/arch/AVX512/PacketMathFP16.h"
        filter_file(
            "static_cast<_Float16>(from)", "numext::bit_cast<_Float16>(from)", header, string=True
        )
        filter_file(
            "_mm512_add_ph(_mm512_set1_ph(a),",
            "_mm512_add_ph(pset1<Packet32h>(a),",
            header,
            string=True,
        )
        filter_file("_mm512_set1_ph(0.0)", "_mm512_setzero_ph()", header, string=True)
