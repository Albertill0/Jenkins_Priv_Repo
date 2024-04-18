from distutils.core import setup, Extension

setup(name='mimodulo',
      version='1.0',
      ext_modules=[Extension('mimodulo', ['mimodulo.c'])])
