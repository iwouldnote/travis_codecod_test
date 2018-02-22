import pytest
from main import Number, Text


def test_upper():
    text = Text('test string')
    assert text.upper() == 'TEST STRING'


@pytest.mark.parametrize('value', [30, 20, 28, 100, 500,
                                   2800020, 10, 2, 8,
                                   100000000])
def test_even(value):
    number = Number(value)
    assert number.is_even()


@pytest.mark.parametrize('value', [15, 7, 33, 999999,
                                   111, 101, 31, 95,
                                   777, 9999999999])
def test_odd(value):
    number = Number(value)
    assert not number.is_even()


@pytest.mark.parametrize('value', [1, 500, 293, 2839,
                                   19191991919, 292,
                                   0, 19, 3, 999])
def test_increase_by_one(value):
    number = Number(value)
    old_value = number.number
    number.increase_by_one()
    assert number.number == old_value + 1
