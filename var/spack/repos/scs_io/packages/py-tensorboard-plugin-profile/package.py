# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class PyTensorboardPluginProfile(Package):

    homepage = "https://pypi.python.org/project/tensorboard-plugin-profile"
    url      = "https://files.pythonhosted.org/packages/06/d9/7a31911763113dfbe4ae3b30f4aeb73d3f0a3979d3cca3a398d7975e9439/tensorboard_plugin_profile-2.3.0.tar.gz"

    version('2.3.0', sha256='7fea73dd591297a0d75604e9be61c35c693ead4ecfce1df4bb6f0e3d33677e0f')
    depends_on('bazel@0.26.1:', type='build')
    depends_on('py-setuptools@36.2.0:', type='build')
    depends_on('python@3.8:', type=('build', 'run'))
    depends_on('py-wheel', type='build')

    extends('python')

    phases = ['setup', 'build', 'install']

    def setup_build_environment(self, env):
        tmp_path = '/tmp/spack/tb-plugin'
        mkdirp(tmp_path)
        env.set('TEST_TMPDIR', tmp_path)

    def setup(self, spec, prefix):
        builddir = join_path(self.stage.source_path, 'spack-build')
        mkdirp(builddir)
        filter_file(r'dest=.*',
                    'dest="{0}"'.format(builddir),
                    'tensorboard_plugin_profile/pip_package/build_pip_package.sh')
        filter_file(r'pip install .*',
                    ''.format(builddir),
                    'tensorboard_plugin_profile/pip_package/build_pip_package.sh')
        filter_file(r'command \-v .*',
                    ''.format(builddir),
                    'tensorboard_plugin_profile/pip_package/build_pip_package.sh')
        filter_file(r'virtualenv venv',
                    ''.format(builddir),
                    'tensorboard_plugin_profile/pip_package/build_pip_package.sh')

    def build(self, spec, prefix):
        tmp_path = env['TEST_TMPDIR']
        bazel('--nohome_rc',
              '--nosystem_rc',
              '--output_user_root=' + tmp_path,
              'run',
              '--verbose_failures',
              '--subcommands=pretty_print',
              'tensorboard_plugin_profile/pip_package:build_pip_package')

    def install(self, spec, prefix):
        with working_dir('spack-build/release'):
            setup_py('install', '--prefix={0}'.format(prefix),
                     '--single-version-externally-managed', '--root=/')
