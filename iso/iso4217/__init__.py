from iso.utils import get_source_data_file, convert_csv_to_dict

filename = "4217.csv"
filepath = get_source_data_file(filename)
object_name = "Currency"
index_column = "code"

currencies = convert_csv_to_dict(filepath, object_name, index_column)
