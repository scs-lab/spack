# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class MongoCxxDriver(CMakePackage):
    """C++ Driver for MongoDB"""

    homepage = "http://www.mongocxx.org"
    url      = "https://github.com/mongodb/mongo-cxx-driver/archive/r3.2.0.tar.gz"

    version('3.2.0',     sha256='e26edd44cf20bd6be91907403b6d63a065ce95df4c61565770147a46716aad8c')
    depends_on('libbson@1.16.2:')
    depends_on('mongo-c-driver@1.9.2:')
    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = ['-DBUILD_VERSION={}'.format(self.version)]
        return args
    def set_include(self,env,path):
        env.prepend_path('C_INCLUDE_PATH', path) 
        env.append_flags('CFLAGS', '-I{}'.format(path)) 
        env.prepend_path('CPLUS_INCLUDE_PATH', path) 
        env.append_flags('CXXFLAGS', '-I{}'.format(path)) 
    def set_lib(self,env,path):
        env.prepend_path('LIBRARY_PATH', path) 
        env.append_flags('LDFLAGS', '-L{}'.format(path)) 
    def set_flags(self,env):
        self.set_include(env,'{}/include/mongocxx/v_noabi'.format(self.prefix))
        self.set_include(env,'{}/include/bsoncxx/v_noabi'.format(self.prefix))
        self.set_lib(env,'{}/lib'.format(self.prefix))
        self.set_lib(env,'{}/lib64'.format(self.prefix))
    def setup_dependent_environment(self, spack_env, run_env, dependent_spec):
        self.set_flags(spack_env)
    def setup_run_environment(self, env):
        self.set_flags(env) 
