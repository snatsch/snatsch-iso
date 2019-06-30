from .main import currencies


def get_currency(alphabetic_code):
    return currencies.get(alphabetic_code)


def is_valid_currency(alphabetic_code):
    currency = get_currency(alphabetic_code)
    return currency is not None


def get_list_of_currencies():
    return list(currencies.keys())
