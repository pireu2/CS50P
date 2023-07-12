import fuel
import pytest

def test_fuel():
    assert fuel.convert("3/4") == 75
    with pytest.raises(ValueError) : fuel.convert("4/3")
    with pytest.raises(ZeroDivisionError) : fuel.convert("4/0")
    with pytest.raises(ValueError) : fuel.convert("cat/dog")
    assert fuel.convert("99/100") == 99
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(25) == "25%"