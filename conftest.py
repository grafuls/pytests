import pytest

def pytest_addoption(parser):
    parser.addoption("-E", action="store", metavar="TYPE",
        help="only run tests matching the type of TYPE.")

def pytest_configure(config):
    config.addinivalue_line("markers",
        "_type(TYPE): mark test to only run by type")

def pytest_runtest_setup(item):
    envmarker = item.get_marker("_type")
    if envmarker is not None:
        envname = envmarker.args[0]
        if envname != item.config.getoption("-E"):
            pytest.skip("test requires type %r" % envname)
            
