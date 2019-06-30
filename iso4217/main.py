import os
from csv import DictReader
from iso4217.models import Currency


def convert_csv_to_dict(file):
    # list of currencies
    # https://www.currency-iso.org/en/home/tables/table-a1.html
    with open(file, "r") as fh:
        content_as_dict = DictReader(
            fh,
            fieldnames=[
                "entity",
                "currency",
                "alphabetic_code",
                "numeric_code",
                "minor_unit",
                "fund",
            ],
        )

        return create_dict_of_currencies(content_as_dict)


def create_dict_of_currencies(data):
    currencies = {}
    for entry in data:
        alphabetic_code = entry["alphabetic_code"]
        if alphabetic_code in currencies:
            currencies[alphabetic_code].entities = entry["entity"]
            continue
        currencies[alphabetic_code] = Currency(**entry)

    return currencies


def main():
    path = os.path.abspath(os.path.dirname(__file__))
    file = f"{path}/data/data.csv"
    return convert_csv_to_dict(file)


currencies = main()
