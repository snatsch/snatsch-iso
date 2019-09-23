# Snatsch - ISO 4217

A lightweight python library to retrieve currencies based on ISO 4217 standard. This library was created despite of many others existing onces because it is lightweight, simple and easy to use.

References:

    - https://en.wikipedia.org/wiki/ISO_4217
    - https://www.currency-iso.org/en/home/tables/table-a1.html

## Getting Started

```bash
pip install snatsch-iso4217
```

## Usage

To get a list of all available currencies:

```python
import iso4217

# get a list of all alphabetic codes
iso4217.get_list_of_currencies()
```

To check if a currency code is valid:

```python
import iso4217

# is the alphabetic code valid?
iso4217.is_valid_currency("DOP")
```

To retrieve information about a currency:

```python
import iso4217

# get a currency
currency = iso4217.get_currency("DOP")

# how is the currency called?
currency.name

# where is the currency used?
currency.entities

# which is it's numeric code?
currency.num

# which is it's alphabetic code?
currency.code

# how many digits after decimal point?
currency.decimal_digits

# is the currency a fund?
currency.fund

# or check everything at once
currency.__dict__
```

## Tests

Run this command in the root of the project:

```bash
PYTHONPATH=${PWD} pytest -v tests
```
