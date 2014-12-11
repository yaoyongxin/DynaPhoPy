from distutils.core import setup, Extension
import numpy, os

include_dirs_numpy = [numpy.get_include()]

correlation = Extension('correlation',
                        extra_compile_args=['-std=c99'],
                        include_dirs = include_dirs_numpy,
                        sources=['Extensions/correlation.c'])

derivative  = Extension('derivative',
                        extra_compile_args=['-std=c99'],
                        include_dirs = include_dirs_numpy,
                        sources=['Extensions/derivative.c'])

mem = Extension('mem',
                extra_compile_args=['-std=c99'],
                include_dirs = include_dirs_numpy,
                sources=['Extensions/mem.c'])


setup(name='DynaPhoPy',
      version='0.9',
      description='DynaPhoPy extensions',
      author='Abel Carreras',
      url='https://github.com/abelcarreras/DynaPhoPy',
      author_email='abelcarreras83@gmail.com',
      packages=['Classes','Functions'],
      scripts=['dynaphopy.py'],
      ext_modules=[correlation, derivative, mem])



try:
    os.remove('Extensions/correlation.so')
    os.remove('Extensions/derivative.so')
    os.remove('Extensions/mem.so')


except:
    print('Overwriting files')

for src_path in ('lib/python/correlation.so','lib/python/derivative.so', 'lib/python/mem.so'):

    os.symlink(
        os.path.relpath(
            src_path,
            'Extensions/'
        ),
        os.path.join('Extensions', os.path.basename(src_path))
    )

