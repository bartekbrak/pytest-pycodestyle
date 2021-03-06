This is a quick fork of https://bitbucket.org/pytest-dev/pytest-pep8 to 
make it use the newest version of pep8, which is now named pycodestyle. 

See:
- https://github.com/PyCQA/pycodestyle/issues/466
- https://bitbucket.org/pytest-dev/pytest-pep8/issues/15/pep8-changed-name-to-pycodestyle


I also converted to git from git://repo.or.cz/fast-export.git.
I did not contact the authors. I am not the author of this code, Holger 
Krekel and Ronny Pfannschmidt are. They seemt o have abandoned the code 
and I need it fast. The original MIT License seems to allow this. 

I plan to upload it to pypi and provide reasonable maintenance. 
I plan to contact the authors soon.

The changes are minimal, I will not change word pep8 everywhere, I will
change it in enough places to make this work.

---



.. image:: https://drone.io/bitbucket.org/pytest-dev/pytest-pep8/status.png
   :target: https://drone.io/bitbucket.org/pytest-dev/pytest-pep8/latest
.. image:: https://pypip.in/v/pytest-pep8/badge.png
   :target: https://pypi.python.org/pypi/pytest-pep8

py.test plugin for efficiently checking PEP8 compliance 
=======================================================

Usage
-----

install via::

    pip install pytest-pep8

if you then type::

    py.test --pep8
    
every file ending in ``.py`` will be discovered and pep8-checked, 
starting from the command line arguments. 

.. warning::

    Running pep8 tests on your project is likely to cause a lot of 
    issues.  This plugin allows to configure on a per-project and
    per-file basis which errors or warnings to care about, see
    pep8ignore_.  As a preliminary advise, if you have 
    projects where you don't want to care at all about pep8 checks, 
    you can put configure it like this::

        # content of setup.cfg (or pytest.ini)
        [pytest]
        pep8ignore = * ALL


A little example 
----------------

If you have a pep8-violating file like this::

    # content of myfile.py
 
    somefunc( 123,456)

you can run it with the plugin installed::

    $ py.test --pep8
    =========================== test session starts ============================
    platform linux2 -- Python 2.7.6 -- py-1.4.30 -- pytest-2.7.2
    rootdir: /tmp/doc-exec-2, inifile: 
    plugins: pep8, cache
    collected 1 items
    
    myfile.py F
    
    ================================= FAILURES =================================
    ________________________________ PEP8-check ________________________________
    /tmp/doc-exec-2/myfile.py:2:10: E201 whitespace after '('
    somefunc( 123,456)
             ^
    /tmp/doc-exec-2/myfile.py:2:14: E231 missing whitespace after ','
    somefunc( 123,456)
                 ^
    
    ========================= 1 failed in 0.00 seconds =========================

For the meaning of (E)rror and (W)arning codes, see the error
output when running against your files or checkout `pep8.py
<https://github.com/jcrocholl/pep8/blob/master/pep8.py>`_.

Let's not now fix the PEP8 errors::

    # content of myfile.py
    somefunc(123, 456)

and run again::

    $ py.test --pep8
    =========================== test session starts ============================
    platform linux2 -- Python 2.7.6 -- py-1.4.30 -- pytest-2.7.2
    rootdir: /tmp/doc-exec-2, inifile: 
    plugins: pep8, cache
    collected 1 items
    
    myfile.py .
    
    ========================= 1 passed in 0.00 seconds =========================

the pep8 check now is passing. Moreover, if
you run it once again (and report skip reasons)::

    $ py.test --pep8 -rs 
    =========================== test session starts ============================
    platform linux2 -- Python 2.7.6 -- py-1.4.30 -- pytest-2.7.2
    rootdir: /tmp/doc-exec-2, inifile: 
    plugins: pep8, cache
    collected 1 items
    
    myfile.py s
    ========================= short test summary info ==========================
    SKIP [1] /home/hpk/p/pytest-pep8/pytest_pep8.py:65: file(s) previously passed PEP8 checks
    
    ======================== 1 skipped in 0.00 seconds =========================

you can see that the pep8 check was skipped because
the file has not been modified since it was last checked.
As the pep8 plugin uses the 
`pytest-cache plugin <http://pypi.python.org/pypi/pytest-cache>`_
to implement its caching, you can use its ``--clearcache`` option to 
remove all pytest caches, among them the pep8 related one, which 
will trigger the pep8 checking code to run once again::

    $ py.test --pep8 --clearcache
    =========================== test session starts ============================
    platform linux2 -- Python 2.7.6 -- py-1.4.30 -- pytest-2.7.2
    rootdir: /tmp/doc-exec-2, inifile: 
    plugins: pep8, cache
    collected 1 items
    
    myfile.py .
    
    ========================= 1 passed in 0.00 seconds =========================

.. _pep8ignore:

Configuring PEP8 options per project and file
---------------------------------------------

You may configure PEP8-checking options for your project
by adding an ``pep8ignore`` entry to your ``setup.cfg``
or ``setup.cfg`` file like this::

    # content of setup.cfg
    [pytest]
    pep8ignore = E201 E231

This would globally prevent complaints about two whitespace issues.
Rerunning with the above example will now look better::

    $ py.test -q  --pep8
    .
    1 passed in 0.00 seconds

If you have some files where you want to specifically ignore 
some errors or warnings you can start a pep8ignore line with 
a glob-pattern and a space-separated list of codes::

    # content of setup.cfg
    [pytest]
    pep8ignore = 
        *.py E201
        doc/conf.py ALL

So if you have a conf.py like this::

    # content of doc/conf.py

    func (  [1,2,3]) #this line lots pep8 errors :)

then running again with the previous example will show a single
failure and it will ignore doc/conf.py alltogether::

    $ py.test --pep8 -v # verbose shows what is ignored
    =========================== test session starts ============================
    platform linux2 -- Python 2.7.6 -- py-1.4.30 -- pytest-2.7.2 -- /home/hpk/venv/clean/bin/python
    cachedir: /tmp/doc-exec-2/.cache
    rootdir: /tmp/doc-exec-2, inifile: setup.cfg
    plugins: pep8, cache
    collecting ... collected 1 items
    
    myfile.py PASSED
    
    ========================= 1 passed in 0.01 seconds =========================

Note that doc/conf.py was not considered or imported.

If you'ld like to have longer lines than 79 chars (which is the default for the
pep8 checker), you can configure it like this::

    # content of setup.cfg
    [pytest]
    pep8maxlinelength = 99

Running PEP8 checks and no other tests
--------------------------------------

You can also restrict your test run to only perform "pep8" tests
and not any other tests by typing::

    py.test --pep8 -m pep8

This will only run test items with the "pep8" marker which this
plugins adds dynamically.

Notes
-----

The repository of this plugin is at http://bitbucket.org/pytest-dev/pytest-pep8

For more info on py.test see http://pytest.org

The code is partially based on Ronny Pfannschmidt's pytest-codecheckers plugin.
