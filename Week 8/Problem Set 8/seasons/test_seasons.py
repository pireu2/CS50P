import pytest
from seasons import convert

def test():
    assert convert("2022-07-17") == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert("2021-07-17") == "One million, fifty-one thousand, two hundred minutes"
    with pytest.raises(SystemExit) : convert("2022 07 17")
    with pytest.raises(ValueError) : convert("2022-21-01")
    with pytest.raises(ValueError) : convert("2022-12-54")