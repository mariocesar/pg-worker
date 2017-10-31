import os
import sys

from setuptools import setup, find_packages

ROOT = os.path.realpath(os.path.join(os.path.dirname(
    sys.modules['__main__'].__file__)))

sys.path.insert(0, os.path.join(ROOT, 'src'))


setup(
    name='pgworker',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': [
            'pgworker = pgworker.runner:main'
        ]
    }
)
