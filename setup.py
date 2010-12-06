"""
py.test plugin for checking PEP8 source code compliance using the pep8 module.

Usage
---------

install via::

    easy_install pytest-pep8 # or
    pip install pytest-pep8

and then type::

    py.test --pep8
    
to activate source code checking. Every file ending in ``.py`` will checked
and you can restrict it like this::

    py.test --pep8 mysourcedir # or
    py.test --pep8 mysourcedir/somefile.py

Notes
-------------

The repository of this plugin is at http://bitbucket.org/hpk42/pytest-pep8

For more info on py.test see http://pytest.org

The code is partially based on Ronny Pfannschmidt's pytest-codecheckers plugin.
"""

from setuptools import setup
setup(
    name='pytest-pep8',
    description='pytest plugin to check source code against PEP8 requirements',
    long_description=__doc__,
    version="0.5",
    author='Holger Krekel and Ronny Pfannschmidt',
    author_email='holger.krekel@gmail.com',
    url='http://bitbucket.org/hpk42/pytest-pep8/',
    py_modules=['pytest_pep8'],
    entry_points={'pytest11': [ 'pep8 = pytest_pep8'],},
    install_requires=['pytest>=2.0', 'pep8', ],
)
