from numb3rs import validate

def test():
    assert validate("cat") == False
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.4") == True
    assert validate("1.2.3.4.5") == False
    assert validate("512.124.0.12") == False
    assert validate("123.321.123.123") == False
    assert validate("123.123.321.123") == False
    assert validate("123.123.123.321") == False
