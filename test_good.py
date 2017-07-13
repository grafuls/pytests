import pytest

def f():
    return 3

@pytest.mark.type_("good")
def test_function():
    assert f() == 3
