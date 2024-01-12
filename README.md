# Snatsch - ISO_3166, ISO_4217

A lightweight python library to retrieve countries and currencies based on ISO_3166-1 and ISO_4217 standards. This library was created despite of many others existing onces because it is lightweight, simple and easy to use.

References:

    - https://en.wikipedia.org/wiki/ISO_3166-1
    - https://www.iso.org/obp/ui/#iso:code:3166:DO
    - https://en.wikipedia.org/wiki/ISO_3166-2:DO
    - https://en.wikipedia.org/wiki/ISO_4217

## Getting Started

```bash
pip install snatsch-iso
```

## Usage

All ISO collections are parsed and structure on a standard way:

- Collection.get_all(): retrieve a list of instances
- Collection.search_keys(): provides a list of all possible keys that can be used for `search_by`
- Collection.search_by(): get a list of instances or a single instance that match the search criteria.

To retrieve information about any of the iso collection you can follow these examples:

```python
from iso import iso4217

# get a list of all Currencies
iso4217.Currencies.get_all()
[Currency(code='AED', num='784', d='2', currency='United Arab Emirates dirham', countries='United Arab Emirates'),
 Currency(code='AFN', num='971', d='2', currency='Afghan afghani', countries='Afghanistan'),
 Currency(code='ALL', num='8', d='2', currency='Albanian lek', countries='Albania'),
 Currency(code='AMD', num='51', d='2', currency='Armenian dram', countries='Armenia'),
 Currency(code='ANG', num='532', d='2', currency='Netherlands Antillean guilder', countries='Curaçao (CW),  Sint Maarten (SX)'),
 Currency(code='AOA', num='973', d='2', currency='Angolan kwanza', countries='Angola'),
 Currency(code='ARS', num='32', d='2', currency='Argentine peso', countries='Argentina'),
 Currency(code='AUD', num='36', d='2', currency='Australian dollar', countries='Australia,  Christmas Island (CX),  Cocos (Keeling) Islands (CC),  Heard Island and McDonald Islands (HM),  Kiribati (KI),  Nauru (NR),  Norfolk Island (NF),  Tuvalu (TV)'),
 Currency(code='AWG', num='533', d='2', currency='Aruban florin', countries='Aruba'),
 Currency(code='AZN', num='944', d='2', currency='Azerbaijani manat', countries='Azerbaijan'),
 . . .]

 # get possible search keys
iso4217.Currencies.search_keys()
['code', 'num']

# get a Currency
iso4217.Currencies.search_by(code="BDT")
Currency(code='BDT', num='50', d='2', currency='Bangladeshi taka', countries='Bangladesh')

iso4217.Currencies.search_by(num="50")
Currency(code='BDT', num='50', d='2', currency='Bangladeshi taka', countries='Bangladesh')
```

To retrieve information about a countries:

```python
from iso import iso3166

# get a list of all Countries
iso3166.Countries.get_all()
[Country(name='Afghanistan', alpha2_code='AF', alpha3_code='AFG', num_code='4'),
 Country(name='Åland Islands', alpha2_code='AX', alpha3_code='ALA', num_code='248'),
 Country(name='Albania', alpha2_code='AL', alpha3_code='ALB', num_code='8'),
 Country(name='Algeria', alpha2_code='DZ', alpha3_code='DZA', num_code='12'),
 Country(name='American Samoa', alpha2_code='AS', alpha3_code='ASM', num_code='16'),
 Country(name='Andorra', alpha2_code='AD', alpha3_code='AND', num_code='20'),
 Country(name='Angola', alpha2_code='AO', alpha3_code='AGO', num_code='24'),
 Country(name='Anguilla', alpha2_code='AI', alpha3_code='AIA', num_code='660'),
 Country(name='Antarctica', alpha2_code='AQ', alpha3_code='ATA', num_code='10'),
 Country(name='Antigua and Barbuda', alpha2_code='AG', alpha3_code='ATG', num_code='28'),
 Country(name='Argentina', alpha2_code='AR', alpha3_code='ARG', num_code='32'),
 Country(name='Armenia', alpha2_code='AM', alpha3_code='ARM', num_code='51'),
 Country(name='Aruba', alpha2_code='AW', alpha3_code='ABW', num_code='533'),
 Country(name='Australia', alpha2_code='AU', alpha3_code='AUS', num_code='36'),
 Country(name='Austria', alpha2_code='AT', alpha3_code='AUT', num_code='40'),
 Country(name='Azerbaijan', alpha2_code='AZ', alpha3_code='AZE', num_code='31'),
 . . .]

# get all dominican republic subdivisions
iso3166.DOSubdivisions.get_all()
[Subdivision(code='DO-01', subdivision_name='Distrito Nacional (Santo Domingo)', subdivision_category='district', parent_subdivision='DO-40'),
 Subdivision(code='DO-02', subdivision_name='Azua', subdivision_category='province', parent_subdivision='DO-41'),
 Subdivision(code='DO-03', subdivision_name='Baoruco', subdivision_category='province', parent_subdivision='DO-38'),
 Subdivision(code='DO-04', subdivision_name='Barahona', subdivision_category='province', parent_subdivision='DO-38'),
 Subdivision(code='DO-05', subdivision_name='Dajabón', subdivision_category='province', parent_subdivision='DO-34'),
 Subdivision(code='DO-06', subdivision_name='Duarte', subdivision_category='province', parent_subdivision='DO-33'),
 Subdivision(code='DO-07', subdivision_name='Elías Piña', subdivision_category='province', parent_subdivision='DO-37'),
 Subdivision(code='DO-08', subdivision_name='El Seibo', subdivision_category='province', parent_subdivision='DO-42'),
 Subdivision(code='DO-09', subdivision_name='Espaillat', subdivision_category='province', parent_subdivision='DO-35'),
 Subdivision(code='DO-10', subdivision_name='Independencia', subdivision_category='province', parent_subdivision='DO-38'),
 Subdivision(code='DO-11', subdivision_name='La Altagracia', subdivision_category='province', parent_subdivision='DO-42'),
 Subdivision(code='DO-12', subdivision_name='La Romana', subdivision_category='province', parent_subdivision='DO-42'),
 Subdivision(code='DO-13', subdivision_name='La Vega', subdivision_category='province', parent_subdivision='DO-36'),
 . . .]

# get all subdivisions that have a parent subdivision
iso3166.DOSubdivisions.search_by(parent_subdivision="DO-33")
[Subdivision(code='DO-06', subdivision_name='Duarte', subdivision_category='province', parent_subdivision='DO-33'),
 Subdivision(code='DO-14', subdivision_name='María Trinidad Sánchez', subdivision_category='province', parent_subdivision='DO-33'),
 Subdivision(code='DO-19', subdivision_name='Hermanas Mirabal', subdivision_category='province', parent_subdivision='DO-33'),
 Subdivision(code='DO-20', subdivision_name='Samaná', subdivision_category='province', parent_subdivision='DO-33')]
```

## Tests

Run this command in the root of the project:

```bash
PYTHONPATH=${PWD} pytest -v tests
```
