import pytest

from hello import get_greeting

def test_default():
    assert get_greeting() == "Hello, world"


def test_argument():
    assert get_greeting("Denys") == "Hello, Denys"
