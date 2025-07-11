import pytest

from calculator import square, correct_square

def test_positive():
    assert correct_square(2) == 4
    assert correct_square(3) == 9


def test_negative():
    assert correct_square(-3) == 9
    assert correct_square(-2) == 4


def test_zero():
    assert correct_square(0) == 0


def test_str():
    with pytest.raises(TypeError):
        correct_square("cat")