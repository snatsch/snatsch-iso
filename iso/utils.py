import os
from csv import DictReader
from collections import namedtuple


def convert_csv_to_dict(filepath: str, tuple_name: str, search_column: str):
    with open(filepath, "r") as fh:
        fieldnames = fh.readline().strip().split(",")
        tuple_object = namedtuple(tuple_name, fieldnames)
        objects = {}
        for record in DictReader(fh, fieldnames):
            objects[record[search_column]] = tuple_object(**record)
        return objects


def get_source_data_file(filename: str):
    path = os.path.abspath(os.path.dirname(__file__))
    return f"{path}/data/{filename}"
