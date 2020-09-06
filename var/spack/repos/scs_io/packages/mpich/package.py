# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install mpich
#
# You can edit this file again by typing:
#
#     spack edit mpich
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Mpich(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "http://www.mpich.org/static/downloads/3.3.2/mpich-3.3.2.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('3.3.2', sha256='4bfaf8837a54771d3e4922c84071ef80ffebddbb6971a006038d91ee7ef959b9')
    depends_on('gcc@9.3.0', when='@3.3.2:')
    # FIXME: Add dependencies if required.
    # depends_on('foo')
    provides('mpi')
    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = ['--enable-fast=03',
                '--enable-shared',
                '--enable-romio',
                '--enable-threads',
                '--disable-fortran',
                '--disable-fc',
                '--enable-onsig',
                '--enable-debuginfo',
                '--enable-g=handle',
                '--enable-debuginfo']
        return args
    def setup_build_environment(self, env):
        env.unset('F90')
        env.unset('F90FLAGS')

        # https://bugzilla.redhat.com/show_bug.cgi?id=1795817
        if self.spec.satisfies('%gcc@10:'):
            env.set('FFLAGS', '-fallow-argument-mismatch')

    def setup_run_environment(self, env):
        # Because MPI implementations provide compilers, they have to add to
        # their run environments the code to make the compilers available.
        # For Cray MPIs, the regular compiler wrappers *are* the MPI wrappers.
        # Cray MPIs always have cray in the module name, e.g. "cray-mpich"
        external_modules = self.spec.external_modules
        if external_modules and 'cray' in external_modules[0]:
            env.set('MPICC', spack_cc)
            env.set('MPICXX', spack_cxx)
            env.set('MPIF77', spack_fc)
            env.set('MPIF90', spack_fc)
        else:
            env.set('MPICC', join_path(self.prefix.bin, 'mpicc'))
            env.set('MPICXX', join_path(self.prefix.bin, 'mpic++'))
            env.set('MPIF77', join_path(self.prefix.bin, 'mpif77'))
            env.set('MPIF90', join_path(self.prefix.bin, 'mpif90'))

    def setup_dependent_build_environment(self, env, dependent_spec):
        self.setup_run_environment(env)

        env.set('MPICH_CC', spack_cc)
        env.set('MPICH_CXX', spack_cxx)
        env.set('MPICH_F77', spack_f77)
        env.set('MPICH_F90', spack_fc)
        env.set('MPICH_FC', spack_fc)

    def setup_dependent_package(self, module, dependent_spec):
        spec = self.spec

        # For Cray MPIs, the regular compiler wrappers *are* the MPI wrappers.
        # Cray MPIs always have cray in the module name, e.g. "cray-mpich"
        external_modules = spec.external_modules
        if external_modules and 'cray' in external_modules[0]:
            spec.mpicc = spack_cc
            spec.mpicxx = spack_cxx
            spec.mpifc = spack_fc
            spec.mpif77 = spack_f77
        else:
            spec.mpicc = join_path(self.prefix.bin, 'mpicc')
            spec.mpicxx = join_path(self.prefix.bin, 'mpic++')

            if '+fortran' in spec:
                spec.mpifc = join_path(self.prefix.bin, 'mpif90')
                spec.mpif77 = join_path(self.prefix.bin, 'mpif77')

        spec.mpicxx_shared_libs = [
            join_path(self.prefix.lib, 'libmpicxx.{0}'.format(dso_suffix)),
            join_path(self.prefix.lib, 'libmpi.{0}'.format(dso_suffix))
        ]
