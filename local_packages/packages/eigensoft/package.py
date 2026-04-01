# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Eigensoft(MakefilePackage):
    """
    The EIGENSOFT package combines functionality from our population genetics methods
    (Patterson et al. 2006) and our EIGENSTRAT stratification correction method
    (Price et al. 2006). The EIGENSTRAT method uses principal components analysis to
    explicitly model ancestry differences between cases and controls along continuous axes
    of variation; the resulting correction is specific to a candidate marker’s variation
    in frequency across ancestral populations, minimizing spurious associations while
    maximizing power to detect true associations. The EIGENSOFT package has a built-in
    plotting script and supports multiple file formats and quantitative phenotypes.
    """


    homepage = "https://hsph.harvard.edu/research/price-lab/software/"
    url = "https://github.com/DReichLab/EIG/archive/refs/tags/v8.0.0.tar.gz"

    maintainers("harrysharma1")

    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("BSD-3-Clause", checked_by="harrysharma1")

    version("8.0.0", sha256="e3459e8ac0134da369910454854eae5c7b261e8816318ccbd2d371b4c6c35741")
    version("7.2.1", sha256="f09a46ec4b83c5062ec71eaca48a78f2373f1666fe23cbf17757150a679c8650")
    version("7.2.0", sha256="6234f368867223e095c60625e6e2c54a87e99c84f380c4b9623a142586aa5a83")

    depends_on('gsl')
    depends_on('openblas')
    depends_on('lapack')

    def build(self, spec, prefix):
        gsl = spec['gsl']
        openblas = spec['openblas']
        include = join_path(self.stage.source_path, "include")
        with working_dir(join_path(self.stage.source_path, 'src')):
            make(
                "CFLAGS=-I{0} {1} {2}".format(include, gsl.headers.cpp_flags, openblas.headers.cpp_flags),
                "LDFLAGS={0} {1}".format(gsl.libs.search_flags, openblas.libs.search_flags)
            )

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install_tree(join_path(self.stage.source_path, 'bin'), prefix.bin)