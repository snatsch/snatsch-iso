import pytest
from iso4217.utils import get_currency, is_valid_currency


def test_get_currency():
    assert get_currency("DOP")


def test_get_currency_with_invalid_currency():
    assert get_currency("BLA") is None


def test_is_valid_currency():
    assert is_valid_currency("DOP") == True


def test_is_valid_currency_with_invalid_currency():
    assert is_valid_currency("BLA") == False
