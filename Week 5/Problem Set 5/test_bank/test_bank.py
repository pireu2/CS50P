from bank import value

def test_bank():
    assert value("Hello") == 0
    assert value("Hello, Newman") == 0
    assert value("How you doing?") == 20
    assert value("What's happening?") == 100