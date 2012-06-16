
pytest_plugins = "pytester",


def test_version():
    import pytest_pep8
    assert pytest_pep8.__version__


class TestSimple:
    def pytest_funcarg__example(self, request):
        testdir = request.getfuncargvalue("testdir")
        p = testdir.makepyfile("")
        p.write("class AClass:\n    pass\n       \n\n#too many spaces")
        return p

    def test_w293w292(self, testdir, example):
        result = testdir.runpytest("--pep8", )
        result.stdout.fnmatch_lines([
            "*pep*ignore*available*",
            "*W293*",
            "*W292*",
        ])
        assert result.ret != 0

    def test_w293_ignore(self, testdir, example):
        testdir.makeini("""
            [pytest]
            pep8ignore = W293
        """)
        result = testdir.runpytest("--pep8", )
        result.stdout.fnmatch_lines([
            "*pep8*ignore*W293*",
        ])
        assert result.ret != 0

    def test_ignore_w293_w292(self, testdir, example):
        testdir.makeini("""
            [pytest]
            pep8ignore = W292 W293
        """)
        result = testdir.runpytest("--pep8", )
        result.stdout.fnmatch_lines([
            "*pep8*ignore*W292*W293*",
        ])
        assert result.ret == 0


def test_ok_verbose(testdir):
    p = testdir.makepyfile("""
        class AClass:
            pass
    """)
    p = p.write(p.read() + "\n")
    result = testdir.runpytest("--pep8", "--verbose")
    result.stdout.fnmatch_lines([
        "*test_ok_verbose*PEP8-check*",
    ])
    assert result.ret == 0


def test_keyword_match(testdir):
    testdir.makepyfile("""
        def test_hello():
            a=[ 1,123]
            #
    """)
    result = testdir.runpytest("--pep8", "-k pep8")
    result.stdout.fnmatch_lines([
        "*E201*",
        "*1 failed*",
    ])
    assert 'passed' not in result.stdout.str()
