import os
from csv import DictReader
from collections import namedtuple
from typing import NamedTuple, Optional, Union


def convert_csv_to_dict(
    filename: str, tuple_name: str, index_column: str
) -> dict[str, list[NamedTuple]]:
    filepath = _get_source_data_file(filename)
    with open(filepath, "r") as fh:
        fieldnames = fh.readline().strip().split(",")
        tuple_object = namedtuple(tuple_name, fieldnames)
        objects = {}
        for record in DictReader(fh, fieldnames):
            key = record[index_column]
            if key in objects:
                objects[key].append(tuple_object(**record))
            else:
                objects[key] = [tuple_object(**record)]
        return objects


def _get_source_data_file(filename: str) -> str:
    abs_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(abs_path, "data", filename)


class CollectionFinder:
    def __init__(self, indexes: list, filename: str, object_name: str):
        self._indexes = indexes
        self._tuple_name = object_name
        self._objects_by = [
            convert_csv_to_dict(filename, object_name, index_column)
            for index_column in indexes
        ]

    def get_all(self) -> Optional[list[NamedTuple]]:
        return [o[0] for o in self._objects_by[0].values()]

    def search_keys(self):
        return self._indexes

    def search_by(self, **kwargs) -> Optional[Union[NamedTuple, list[NamedTuple]]]:
        search_param = None
        search_value = None

        for key, value in kwargs.items():
            if value and key in self._indexes:
                search_param = key
                search_value = value
                break

        if not all([search_param, search_value]):
            return None

        search_index = self._indexes.index(search_param)
        result = None
        if search_value in self._objects_by[search_index]:
            result = self._objects_by[search_index][search_value]

        if result and len(result) == 1:
            return result[0]
        return result
