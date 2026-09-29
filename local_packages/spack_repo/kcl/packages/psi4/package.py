# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Psi4(CMakePackage):
    """Psi4 is an open-source suite of ab initio quantum chemistry
    programs designed for efficient, high-accuracy simulations of
    a variety of molecular properties."""

    homepage = "https://www.psicode.org/"
    url = "https://github.com/psi4/psi4/archive/v1.3.2.tar.gz"
    
    license("LGPL-3.0-only")

    version('1.11', sha256='b6b5a4d397ba551d7f3516e5dc0da64bcc5778e3dca7898504293792d1b02bac')
    version('1.3.2', sha256='ed76c67803b6420f35f57a6dd31c47108b9145b8c9fced5c94cdc179f6b5fbf3',
            deprecated=True)

    variant('build_type', default='Release',
            description='The build type to build',
            values=('Debug', 'Release'))

    # Required dependencies
    depends_on('openblas')
    depends_on('lapack')
    depends_on('boost+chrono+filesystem+python+regex+serialization+system+timer+thread')
    depends_on('cmake@3.3:', type='build')
    depends_on('cmake@3.19:', type='build', when='@1.11:')

    depends_on('python@:3.10', when='@1.3.2')
    depends_on('py-numpy@:1.24', type=('build', 'run'), when='@1.3.2')
    depends_on('py-pydantic', type=('build', 'run'), when='@1.3.2')
    depends_on('py-pint', type=('build', 'run'), when='@1.3.2')
    depends_on('py-deepdiff', type=('build', 'run'), when='@1.3.2')

    # psi4@1.11: CMakeLists.txt/codedeps.yaml raised the Python floor to 3.10
    # and require qcelemental/qcengine/optking/qcmanybody, none of which are
    # packaged in Spack. Psi4's own CMake superbuild fetches and pip-installs
    # those four straight from GitHub (each with `pip install --no-deps`), so
    # Spack doesn't supply them directly -- but --no-deps means their own
    # runtime dependencies (below, per their PyPI/setup.py metadata) still
    # have to come from somewhere, or `import qcelemental` etc. fails at
    # runtime once psi4 is installed.
    depends_on('python@3.10:', when='@1.11:')
    depends_on('eigen', when='@1.11:')
    depends_on('py-numpy', type=('build', 'run'), when='@1.11:')
    depends_on('py-scipy', type=('build', 'run'), when='@1.11:')
    depends_on('py-pydantic@2.11:', type=('build', 'run'), when='@1.11:')
    depends_on('py-pydantic-settings', type=('build', 'run'), when='@1.11:')
    depends_on('py-pint@0.24:', type=('build', 'run'), when='@1.11:')
    depends_on('py-pyyaml', type=('build', 'run'), when='@1.11:')
    depends_on('py-msgpack', type=('build', 'run'), when='@1.11:')
    depends_on('py-psutil', type=('build', 'run'), when='@1.11:')
    depends_on('py-py-cpuinfo', type=('build', 'run'), when='@1.11:')
    depends_on('py-packaging', type=('build', 'run'), when='@1.11:')

    # Optional dependencies
    # TODO: add packages for these
    # depends_on('perl')
    # depends_on('erd')
    # depends_on('pcm-solver')
    # depends_on('chemps2')

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on('py-pybind11@3:', type='build', when='@1.11:')
    depends_on('py-pip', type='build', when='@1.11:')
    depends_on('git', type='build', when='@1.11:')

    def patch(self):
        # <eigen3/Eigen/Core> assumes one shared include dir (conda); Spack only
        # puts <eigen>/include/eigen3 on the include path
        if self.spec.satisfies("@1.11:"):
            filter_file("<eigen3/Eigen/Core>", "<Eigen/Core>",
                        "psi4/src/psi4/libmints/matrix.h",
                        "psi4/src/psi4/libfock/SplitJK.h",
                        string=True)

    def cmake_args(self):
        spec = self.spec

        args = [
            '-DBLAS_TYPE={0}'.format(spec['openblas'].name.upper()),
            '-DBLAS_LIBRARIES={0}'.format(spec['openblas'].libs.joined()),
            '-DLAPACK_TYPE={0}'.format(spec['lapack'].name.upper()),
            '-DLAPACK_LIBRARIES={0}'.format(
                spec['lapack'].libs.joined()),
            '-DENABLE_CheMPS2=OFF',
        ]

        # psi4@1.11 dropped the BOOST_INCLUDEDIR/BOOST_LIBRARYDIR cache
        # variables from its top-level CMakeLists.txt; Boost is now located
        # for the bundled Libint2 build purely via CMAKE_PREFIX_PATH, which
        # Spack's CMakePackage already populates from `depends_on('boost')`.
        if spec.satisfies('@:1.9'):
            args += [
                '-DBOOST_INCLUDEDIR={0}'.format(spec['boost'].prefix.include),
                '-DBOOST_LIBRARYDIR={0}'.format(spec['boost'].prefix.lib),
            ]

        return args

    @run_after('install')
    def filter_compilers(self):
        """Run after install to tell the configuration files to
        use the compilers that Spack built the package with.

        If this isn't done, they'll have PLUGIN_CXX set to
        Spack's generic cxx. We want it to be bound to
        whatever compiler it was built with."""

        spec = self.spec
        prefix = spec.prefix

        kwargs = {'ignore_absent': True, 'backup': False, 'string': True}

        cc_files = ['bin/psi4-config']
        cxx_files = ['bin/psi4-config', 'include/psi4/psiconfig.h']
        template = 'share/psi4/plugin/Makefile.template'

        for filename in cc_files:
            filter_file(os.environ['CC'], self.compiler.cc,
                        os.path.join(prefix, filename), **kwargs)

        for filename in cxx_files:
            filter_file(os.environ['CXX'], self.compiler.cxx,
                        os.path.join(prefix, filename), **kwargs)

        # The binary still keeps track of the compiler used to install Psi4
        # and uses it when creating a plugin template
        filter_file('@PLUGIN_CXX@', self.compiler.cxx,
                    os.path.join(prefix, template), **kwargs)

        # The binary links to the build include directory instead of the
        # installation include directory:
        # https://github.com/psi4/psi4/issues/410
        filter_file('@PLUGIN_INCLUDES@', '-I{0}'.format(
            ' -I'.join([
                os.path.join(spec['psi4'].prefix.include, 'psi4'),
                os.path.join(spec['boost'].prefix.include, 'boost'),
                os.path.join(spec['python'].headers.directories[0]),
                spec['lapack'].prefix.include,
                spec['openblas'].prefix.include,
                '/usr/include'
            ])
        ), os.path.join(prefix, template), **kwargs)
