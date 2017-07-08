import pytest

# content of test_assert1.py
def f():
    return 3

@pytest.mark.env("good")
def test_function():
    assert f() == 3
