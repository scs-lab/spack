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
#     spack install rpclib
#
# You can edit this file again by typing:
#
#     spack edit rpclib
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Symbios(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.example.com"
    git      = "https://github.com/scs-lab/symbios.git"

    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']
    version('master', branch='master')
    depends_on('gcc@9.3.0', when='@master')
    depends_on('mpich@3.3.2', when='@master')
    depends_on('rpclib@2.2.1', when='@master')
    depends_on('rapidjson@1.1.0', when='@master')
    depends_on('boost@1.74.0', when='@master')
    depends_on('openblas@0.3.10', when='@master')
    depends_on('dlib@19.17', when='@master')
    depends_on('hcl@0.0.4', when='@master')
    depends_on('redis-plus-plus@1.1.2', when='@master')
    depends_on('mongo-cxx-driver@3.5.1', when='@master')
    depends_on('redis-server', when='@master')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = ['-DCMAKE_INSTALL_PREFIX={}'.format(self.prefix),
                '-DCMAKE_INSTALL_INCLUDEDIR={}/include'.format(self.prefix)]
        return args
