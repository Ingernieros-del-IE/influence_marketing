import pytest

def test_addition():
    assert 1 + 1 == 2
    
def test_subtraction():
    assert 5 - 2 == 3
    
def test_multiplication():
    assert 3 * 4 == 12
    
def test_division():
    assert 10 / 2 == 5
    
def test_string_concatenation():
    assert "hello" + " " + "world" == "hello world"