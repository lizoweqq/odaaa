import pytest
from func import calculate_func

def test_positive_values():
    assert calculate_func(5, 10) == 50

def test_square():
    assert calculate_func(4, 4) == 16

def test_invalid_values():
    with pytest.raises(ValueError):
        calculate_func(-3, 5)
