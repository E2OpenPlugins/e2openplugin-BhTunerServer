from distutils.core import setup, Extension

pkg = 'Extensions.BhTunerServer'
setup (name='enigma2-plugin-extensions-bhtunerserver',
       version='0.1',
       license='GPLv2',
       url='https://github.com/E2OpenPlugins/e2openplugin-BhTunerServer',
       description='Allow stream from current box tuners',
       long_description='Allow stream from current box tuners',
       author='meo',
       author_email='lupomeo@hotmail.com',
       packages=[pkg],
       package_dir={pkg: 'plugin'},
      )
