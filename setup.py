import os
import numpy
from setuptools import setup
from numpy.distutils.core import Extension
from Cython.Build import cythonize


def readme():
    with open('readme.md') as readme_file:
        return readme_file.read()

os.environ["CC"] = "clang"

configuration = {
    'name' : 'Deep Recursive Embedding',
    'version': '1.0.0',
    'description' : 'Deep Recursive Embedding for High-Dimensional Data',
    'long_description' : readme(),
    'classifiers' : [
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Programming Language :: C',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        "License :: OSI Approved :: MIT License",
    ],
    'keywords' : 'Dimensionality Reduction t-SNE UMAP Representation Learning',
    'url' : 'https://github.com/zuxinrui/DRE',
    'author' : 'Xinrui Zu',
    'author_email' : 'zuxinrui95@gmail.com',
    'license' : 'LICENSE',
    'packages' : ['dre'],
    'install_requires' : ['scikit-learn >= 0.16',
                          'numba >= 0.34',
                          'torch >= 1.0',
                          'cython >= 0.10'],
    'ext_modules' : cythonize('dre/_utils.pyx'),
    'include_dirs' : [numpy.get_include()],
    }

setup(**configuration)
