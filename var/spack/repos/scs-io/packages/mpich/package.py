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
