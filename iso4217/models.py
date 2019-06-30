class Currency(object):
    def __init__(
        self, entity, currency, alphabetic_code, numeric_code, minor_unit, fund
    ):
        self._entities = [entity]
        self.name = currency
        self.code = alphabetic_code
        self.num = self._cast_to_int(numeric_code)
        self.decimal_digits = self._cast_to_int(minor_unit)
        # If fund is numeric means that it is a fund code
        # https://www.currency-iso.org/en/home/tables/table-a2.html
        self.fund = fund.isnumeric()

    def _cast_to_int(self, value):
        """ Returns value integer representation or negative one if not an integer """
        return int(value) if value.isnumeric() else -1

    @property
    def entities(self):
        return self._entities

    @entities.setter
    def entities(self, entity):
        self._entities.append(entity)

    @entities.deleter
    def entities(self, entity):
        self._entities.remove(entity)

