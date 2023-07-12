from twttr import shorten

def test_big_vowels():
    assert shorten("AEIOUBCD") == "BCD"

def test_small_vowels():
    assert shorten("aeioubcd") == "bcd"

def test_numbers():
    assert shorten("1234") == "1234"

def test_punctuation():
    assert shorten("!?.,") == "!?.,"