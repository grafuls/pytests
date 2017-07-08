# content of test_assert1.py
def f():
    import ipdb;ipdb.set_trace()
    return 3

def test_function():
    assert f() == 4
