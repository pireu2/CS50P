import pytest
import project


def test_main():
    with pytest.raises(ValueError) : project.main()
