import pytest
import utils 
import conversion


@pytest.mark.parametrize("number, expected", [(0, "0"), (1, "1"), (100, "1100100")])
def test_valid_numbers(number, expected):
    assert conversion(number) == expected


def test_out_of_range():
    with pytest.raises(ValueError):
        conversion(-1)
    with pytest.raises(ValueError):
        conversion(101)


def test_non_integer():
    with pytest.raises(TypeError):
        conversion(10.5)
