py.test plugin for checking PEP8 source code compliance using the pep8 module.

Usage
---------

install via::

    easy_install pytest-pep8 # or
    pip install pytest-pep8

and then type::

    py.test --pep8
    
to activate source code checking. Every file ending in ``.py`` will be
discovered and checked, starting from the command line arguments::

    py.test --pep8 mysourcedir # or
    py.test --pep8 mysourcedir/somefile.py

If you pass the ``--pep8`` option you will see the current list of
default "ignores", used when invoking the ``pep8.py`` based checking::

    pep8
     

Per-Project PEP8 checking configuration
--------------------------------------------

You can configure PEP8-checking options for your project
by adding an ``pep8options`` entry to your ``pytest.ini``
or ``setup.cfg`` file like this::

    [pytest]
    pep8options = +W293 -E200

For meanings of Error codes refer to http://pypi.python.org/pypi/pep8
and the error message that you get.

Notes
-------------

The repository of this plugin is at http://bitbucket.org/hpk42/pytest-pep8

For more info on py.test see http://pytest.org

The code is partially based on Ronny Pfannschmidt's pytest-codecheckers plugin.

