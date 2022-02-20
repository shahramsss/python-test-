import pytest
import unit_test


def test_sum():
    assert unit_test.sum(3 , 9 ) == 12

def test_subtract():
    assert unit_test.subtract(10 ,2) ==8

def test_multiply():
    assert unit_test.multiply(4,5) == 20 

def test_division():
    assert unit_test.division(15 , 3)
    with pytest.raises(ZeroDivisionError):
        unit_test.division(5 , 0)