import pytest
from jar import Jar


def test_init():
    with pytest.raises(ValueError) : jar = Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(1)
    assert jar.size == 1
    with pytest.raises(ValueError) : jar.deposit(500)


def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError) : jar.withdraw(1)
