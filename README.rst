randomtimezone
==============

Utility (written in Python) that outputs a datetime string in a random timezone in ISO 8601. I wrote this to use
with Git.

Requirements
============
Python 3 and its standard library.

Installation
============
Recommended installation is through PyPi (pip)::

    pip3 install randomtimezone

Building::

    python3 setup.py install


Usage
=====
::

    $ randomtimezone
    2017-10-31T06:06:47+0700
    $ randomtimezone
    2017-10-31T09:06:51+1000
    $ randomtimezone
    2017-10-31T11:51:53+1245


Git::

    git config --global alias.rcommit '!git commit --date="$(randomtimezone)"'
