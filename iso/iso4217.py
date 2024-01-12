from iso.utils import CollectionFinder

_currencies_indexes = ["code", "num"]
Currencies = CollectionFinder(_currencies_indexes, "4217.csv", "Currency")

__all__ = ["Currencies"]
