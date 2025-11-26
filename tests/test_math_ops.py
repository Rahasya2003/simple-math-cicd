from src.math_ops import add,sub,multiply

def test_add():
    assert add(2,3)==5

def test_sub():
    assert sub(5,2)==3

def test_multiply():
    assert multiply(3,4)==12
