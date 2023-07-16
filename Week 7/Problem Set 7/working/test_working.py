from working import convert
import pytest

def test():
    with pytest.raises(ValueError) : convert("13:00 AM to 9:00 PM")
    with pytest.raises(ValueError) : convert("12:61 AM to 9:00 PM")
    with pytest.raises(ValueError) : convert("12:00 AM - 9:00 PM")
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"