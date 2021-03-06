#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Lot of setup code copied and mofified from xarray (Apache License)

import os
import re
import sys
import warnings
import subprocess

from setuptools import setup, find_packages


MAJOR = 0
MINOR = 1
MICRO = 0
ISRELEASED = False
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)
QUALIFIER = ''

DISTNAME = 'spyfit'
LICENSE = 'GPLv3'
AUTHOR = 'Benoit Bovy'
AUTHOR_EMAIL = 'bbovy@ulg.ac.be'
URL = 'https://github.com/girpas-ulg/spyfit'
CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'License :: OSI Approved :: GPLv3 License',
    'Operating System :: OS Independent',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Topic :: Scientific/Engineering',
]

INSTALL_REQUIRES = ['xarray >= 0.7.2']
TESTS_REQUIRE = ['pytest >= 2.7.1']

if sys.version_info[:2] < (2, 7):
    TESTS_REQUIRE += ["unittest2 == 0.5.1"]

DESCRIPTION = "Python tools for FTIR retrievals"
with open('README.rst') as readme_file:
    LONG_DESCRIPTION = readme_file.read()

# code to extract and write the version copied from pandas
FULLVERSION = VERSION
write_version = True

if not ISRELEASED:
    FULLVERSION += '.dev'

    pipe = None
    for cmd in ['git', 'git.cmd']:
        try:
            pipe = subprocess.Popen(
                [cmd, "describe", "--always", "--match", "v[0-9]*"],
                stdout=subprocess.PIPE)
            (so, serr) = pipe.communicate()
            if pipe.returncode == 0:
                break
        except:
            pass

        if pipe is None or pipe.returncode != 0:
            # no git, or not in git dir
            if os.path.exists('spyfit/version.py'):
                warnings.warn("WARNING: Couldn't get git revision, "
                              "using existing spyfit/version.py")
                write_version = False
            else:
                warnings.warn("WARNING: Couldn't get git revision, "
                              "using generic version string")
        else:
            # have git, in git dir, but may have used a shallow clone
            # (travis does this)
            rev = so.strip()
            # makes distutils blow up on Python 2.7
            if sys.version_info[0] >= 3:
                rev = rev.decode('ascii')

            if not rev.startswith('v') and re.match("[a-zA-Z0-9]{7,9}", rev):
                # partial clone, manually construct version string
                # this is the format before we started using git-describe
                # to get an ordering on dev version strings.
                rev = "v%s.dev-%s" % (VERSION, rev)

            # Strip leading v from tags format "vx.y.z" to get th version
            # string
            FULLVERSION = rev.lstrip('v')

else:
    FULLVERSION += QUALIFIER


def write_version_py(filename=None):
    cnt = """\
version = '%s'
short_version = '%s'
"""
    if not filename:
        filename = os.path.join(
            os.path.dirname(__file__), 'spyfit', 'version.py')

    a = open(filename, 'w')
    try:
        a.write(cnt % (FULLVERSION, VERSION))
    finally:
        a.close()

if write_version:
    write_version_py()


setup(name=DISTNAME,
      version=FULLVERSION,
      license=LICENSE,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      classifiers=CLASSIFIERS,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      install_requires=INSTALL_REQUIRES,
      tests_require=TESTS_REQUIRE,
      url=URL,
      packages=find_packages(),
      py_modules=[],
      package_data={})
