# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.perl import PerlPackage
from spack_repo.builtin.packages.boost.package import Boost

from spack.package import *


class PerlLibbi(PerlPackage):
    """
    LibBi is used for state-space modelling and Bayesian inference on high-performance computer hardware, including multi-core CPUs, many-core GPUs (graphics processing units) and distributed-memory clusters.
    The staple methods of LibBi are based on sequential Monte Carlo (SMC), also known as particle filtering.
    These methods include particle Markov chain Monte Carlo (PMCMC) and SMC2. Other methods include the extended Kalman filter and some parameter optimisation routines.
    LibBi consists of a C++ template library, as well as a parser and compiler, written in Perl, for its own modelling language.
    """

    homepage = "https://libbi.org"
    url = "https://github.com/lawmurray/LibBi/archive/1.4.5.tar.gz"

    maintainers("harrysharma1")

    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="harrysharma")

    version("1.4.5", sha256="af2b6d30e1502f99a3950d63ceaf7d7275a236f4d81eff337121c24fbb802fbe")

    depends_on("cxx", type="build")

    variant('mpi', default=False, description='enable MPI support')

    depends_on("perl-module-install", type="build")
    depends_on("perl-extutils-makemaker", type="build")
    depends_on("thrust@1.6:", type=("build", "run"))
    depends_on("netcdf-c@4.2:", type=("run", "build"))
    depends_on("qrupdate", type=("run", "build"))
    depends_on("gsl", type=("run", "build"))
    depends_on("boost@1.43:", type=("run", "build"))
    depends_on(Boost.with_default_variants)
    depends_on("boost+mpi+serialization@1.43:", type=("build", "run"), when="+mpi")
    depends_on("mpi", type=("build", "run"), when="+mpi")
    depends_on("openblas")
    depends_on("lapack")
    depends_on("perl-template-toolkit", type=("build", "run"))
    depends_on("perl-graph", type=("build", "run"))
    depends_on("perl-math-symbolic", type=("build", "run"))
    depends_on("perl-carp-assert", type=("build", "run"))
    depends_on("perl-parse-yapp", type=("build", "run"))
    depends_on("perl-parselex", type=("build", "run"))
    depends_on("perl-file-slurp", type=("build", "run"))
    depends_on("perl-file-sharedir", type=("build", "run"))
    depends_on("perl-getopt-argvfile", type=("build", "run"))
    depends_on("perl-parsetemplate", type=("build", "run"))
    depends_on("perl-parse-recdescent", type=("build", "run"))
    depends_on("perl-class-inspector", type=("build", "run"))