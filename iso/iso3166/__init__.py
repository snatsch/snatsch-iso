from iso.utils import get_source_data_file, convert_csv_to_dict

filename = "3166_1.csv"
filepath = get_source_data_file(filename)
object_name = "Country"
index_column = "alpha2_code"

countries = convert_csv_to_dict(filepath, object_name, index_column)
