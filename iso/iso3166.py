from iso.utils import CollectionFinder

# all countries
_countries_indexes = ["alpha2_code", "alpha3_code", "num_code"]
Countries = CollectionFinder(_countries_indexes, "3166_1.csv", "Country")

# dominican republic subdivisions
_DO_subdivisions_indexes = ["code", "subdivision_category", "parent_subdivision"]
DOSubdivisions = CollectionFinder(
    _DO_subdivisions_indexes, "3166_2_DO.csv", "Subdivision"
)

__all__ = ["Countries", "DOSubdivisions"]
