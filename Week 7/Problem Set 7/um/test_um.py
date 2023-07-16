from um import count

def test():
    assert count("Um, thanks for the album.") == 1
    assert count("yummy") == 0
    assert count("Um, thanks, um...") == 2
    assert count("um?") == 1