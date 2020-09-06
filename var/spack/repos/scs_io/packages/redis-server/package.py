# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RedisServer(MakefilePackage):
    """Hiredis is a minimalistic C client library for the Redis database."""

    homepage = "https://github.com/redis/hiredis"
    url      = "https://github.com/redis/redis/archive/6.0.6.tar.gz"

    version('6.0.6',sha256='e7cedb37077be2e4ba6323bb3c6c8da027701b9093ebb2f8d15a0c67e145b7c0')

    def install(self, spec, prefix):
        make('PREFIX={0}'.format(prefix), 'install')
