# Exemplary conversion function

import pytest
from conversion import convert_to_binary


@pytest.mark.parametrize("number, expected", [(0, "0"), (1, "1"), (100, "1100100")])
def test_valid_numbers(number, expected):
    assert convert_to_binary(number) == expected


def test_out_of_range():
    with pytest.raises(ValueError):
        convert_to_binary(-1)
    with pytest.raises(ValueError):
        convert_to_binary(101)


def test_non_integer():
    with pytest.raises(TypeError):
        convert_to_binary(10.5)
