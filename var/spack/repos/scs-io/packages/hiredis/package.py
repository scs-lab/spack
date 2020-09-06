# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Hiredis(MakefilePackage):
    """Hiredis is a minimalistic C client library for the Redis database."""

    homepage = "https://github.com/redis/hiredis"
    git      = "https://github.com/redis/hiredis.git"

    version('1.0.0',branch='v1.0.0')

    def install(self, spec, prefix):
        make('PREFIX={0}'.format(prefix), 'install')
