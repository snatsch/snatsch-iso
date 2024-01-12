from iso.utils import convert_csv_to_dict, CollectionFinder


def test_convert_csv_to_dict():
    filename = "4217.csv"
    object_name = "Currency"
    index_column = "code"

    currencies = convert_csv_to_dict(filename, object_name, index_column)
    assert isinstance(currencies, dict)


def test_collection_finder():
    filename = "4217.csv"
    object_name = "Currency"
    code = "BDT"

    collection = CollectionFinder(["code"], filename, object_name)
    currencies = collection.get_all()
    currency = collection.search_by(code=code)

    assert isinstance(currencies, list)
    assert len(currencies) == 179
    assert currency.code == code
