"""
Setup script for randomtimezone
"""

from setuptools import setup
from randomtimezone import __author__, __version__

setup(name='randomtimezone',
      author=__author__,
      version=__version__,
      url='https://github.com/itismadness/randomtimezone',
      description='Generate datetime with a random timezone',
      long_description=open('README.rst').read(),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3 :: Only',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License'
      ],
      entry_points={
          'console_scripts': [
              'randomtimezone = randomtimezone:main'
          ]
      })
