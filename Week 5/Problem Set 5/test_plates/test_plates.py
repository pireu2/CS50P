from plates import is_valid

def test_plates():
    assert is_valid("44444") == False
    assert is_valid("44a44") == False
    assert is_valid("1234567") == False
    assert is_valid("a") == False
    assert is_valid("AAA22A") == False
    assert is_valid("AAA222") == True
    assert is_valid("CS05") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS.50") == False