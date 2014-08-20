#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

import datetime

def international(l):
    nl = []
    for team in l:
        team['international'] = True
        u20 = team.copy()
        u20['name'] = team['name'] + ' U-20'
        u17 = team.copy()
        u17['name'] = team['name'] + ' U-17'
        olympic = team.copy()
        olympic['name'] = team['name'] + ' Olympic'

        nl.extend([team, u20, u17, olympic])

    return nl
        
l = international([
    {
        'name': 'Argentina',
        'founded': datetime.datetime(1893, 2, 21),
        'country': 'Argentina',
        },

    {
        'name': 'Bolivia',
        'founded': 1925,
        'country': 'Bolivia',
        },
    {
        'name': 'Brazil',
        'founded': 1914,
        'country': 'Brazil',
        },
    {
        'name': 'Chile',
        'founded': 1895,
        'country': 'Chile',
        },
    {
        'name': 'Colombia',
        'founded': 1924,
        'country': 'Colombia',
        },
    {
        'name': 'Ecuador',
        'founded': 1925,
        'country': 'Ecuador',
        },

    {
        'name': 'Falkland Islands',
        'founded': 1916,
        'country': 'Falkland Islands',
        },
    {
        'name': 'Paraguay',
        'founded': 1906,
        'country': 'Paraguay',
        },
    {
        'name': 'Peru',
        'founded': 1922,
        'country': 'Peru',
        },
    {
        'name': 'Uruguay',
        'founded': 1900,
        'country': 'Uruguay',
        },
    {
        'name': 'Venezuela',
        'founded': 1926,
        },
    {
        'name': 'Canada',
        'founded': 1912,
        'country': 'Canada',
        },
    {
        'name': 'Mexico',
        'founded': 1927,
        'country': 'Mexico',
        },

    {
        'name': 'United States',
        'founded': 1913,
        'country': 'United States',
        },
    {
        'name': 'Belize',
        'founded': 1980,
        'country': 'Belize',
        },
    {
        'name': 'Costa Rica',
        'founded': 1921,
        'country': 'Costa Rica',
        },
    {
        'name': 'El Salvador',
        'founded': 1935,
        'country': 'El Salvador',
        },
    {
        'name': 'Guatemala',
        'founded': 1919,
        'country': 'Guatemala',
        },
    {
        'name': 'Honduras',
        'founded': 1951,
        'country': 'Honduras',
        },
    {
        'name': 'Nicaragua',
        'founded': 1931,
        'country': 'Nicaragua',
        },
    {
        'name': 'Panama',
        'founded': 1937,
        'country': 'Panama',
        },
    {
        'name': 'Anguilla',
        'founded': 1990,
        'country': 'Anguilla',
        },
    {
        'name': 'Guadeloupe',
        'founded': 1961,
        'country': 'Guadeloupe',
        },
    {
        'name': 'Antigua and Barbuda',
        'founded': 1928,
        'country': 'Antigua and Barbuda',
        },
    {
        'name': 'Aruba',
        'founded': 1932,
        'country': 'Aruba',
        },
    {
        'name': 'Bahamas',
        'founded': 1967,
        'country': 'Bahamas',
        },
    {
        'name': 'Barbados',
        'founded': 1910,
        'country': 'Barbados',
        },
    {
        'name': 'Bermuda',
        'founded': 1928,
        'country': 'Bermuda',
        },
    {
        'name': 'British Virgin Islands',
        'founded': 1974,
        'country': 'British Virgin Islands',
        },
    {
        'name': 'Cayman Islands',
        'founded': 1966,
        'country': 'Cayman Islands',
        },
    {
        'name': 'Cuba',
        'founded': 1924,
        'country': 'Cuba',
        },
    {
        'name': 'Curacao',
        'founded': 2010,
        'country': 'Curacao',
        },
    {
        'name': 'Dominica',
        'founded': 1970,
        'country': 'Dominica',
        },
    {
        'name': 'Dominican Republic',
        'founded': 1953,
        'country': 'Dominican Republic',
        },
    {
        'name': 'French Guiana',
        'founded': 1962,
        'country': 'French Guiana',
        },
    {
        'name': 'Grenada',
        'founded': 1924,
        'country': 'Grenada',
        },

    {
        'name': 'Guyana',
        'founded': 1902,
        'country': 'Guyana',
        },
    {
        'name': 'Haiti',
        'founded': 1904,
        'country': 'Haiti',
        },
    {
        'name': 'Jamaica',
        'founded': 1910,
        'country': 'Jamaica',
        },
    {
        'name': 'Martinique',
        'founded': 1953,
        'country': 'Martinique',
        },
    {
        'name': 'Montserrat',
        'founded': 1973,
        'country': 'Montserrat',
        },
    {
        'name': 'Puerto Rico',
        'founded': 1940,
        'country': 'Puerto Rico',
        },
    {
        'name': 'Saint Kitts and Nevis',
        'founded': 1932,
        'country': 'Saint Kitts and Nevis',
        },
    {
        'name': 'Saint Lucia',
        'founded': 1979,
        'country': 'Saint Lucia',
        },
    {
        'name': 'Saint Martin',
        'founded': 1999,
        'country': 'Saint Martin',
        },
    {
        'name': 'Saint Vincent and the Grenadines',
        'founded': 1979,
        'country': 'Saint Vincent and the Grenadines',
        },
    {
        'name': 'Sint Maarten',
        'founded': 1986,
        'country': 'Sint Maarten',
        },
    {
        'name': 'Suriname',
        'founded': 1920,
        'country': 'Suriname',
        },
    {
        'name': 'Trinidad and Tobago',
        'founded': 1908,
        'country': 'Trinidad and Tobago',
        },
    {
        'name': 'Turks and Caicos',
        'founded': 1996,
        'country': 'Turks and Caicos',
        },
    {
        'name': 'US Virgin Islands',
        'founded': 1989,
        'country': 'US Virgin Islands',
        },
    {
        'name': 'Albania',
        'founded': datetime.datetime(1930, 6, 6),
        'country': 'Albania',
        },
    {
        'name': 'Andorra',
        'founded': 1994,
        'country': 'Andorra',
        },
    {
        'name': 'Armenia',
        'founded': 1992,
        'country': 'Armenia',
        },
    {
        'name': 'Austria',
        'founded': 1904,
        'country': 'Austria',
        },
    {
        'name': 'Azerbaijan',
        'founded': 1992,
        'country': 'Azerbaijan',
        },
    {
        'name': 'Belarus',
        'founded': 1989,
        'country': 'Belarus',
        },
    {
        'name': 'Belgium',
        'founded': 1895,
        'country': 'Belgium',
        },
    {
        'name': 'Bosnia and Herzegovina',
        'founded': 1920,
        'country': 'Bosnia and Herzegovina',
        },
    {
        'name': 'Bulgaria',
        'founded': 1923,
        'country': 'Bulgaria',
        },
    {
        'name': 'Croatia',
        'founded': datetime.datetime(1912, 6, 13),
        'country': 'Croatia',
        },
    {
        'name': 'Cyprus',
        'founded': 1934,
        'country': 'Cyprus',
        },
    {
        'name': 'Czech Republic',
        'founded': 1901,
        'country': 'Czech Republic',
        },
    {
        'name': 'Denmark',
        'founded': 1889,
        'country': 'Denmark',
        },
    {
        'name': 'England',
        'founded': datetime.datetime(1863, 1, 15),
        'country': 'England',
        },
    {
        'name': 'Italy',
        'founded': 1898,
        'country': 'Italy',
        },
    {
        'name': 'Kazakhstan',
        'founded': 1992,
        'country': 'Kazakhstan',
        },
    {
        'name': 'Latvia',
        'founded': 1921,
        'country': 'Latvia',
        },
    {
        'name': 'Liechtenstein',
        'founded': 1934,
        'country': 'Liechtenstein',
        },
    {
        'name': 'Estonia',
        'founded': datetime.datetime(1921, 12, 14),
        'country': 'Estonia',
        },
    {
        'name': 'Faroe Islands',
        'founded': 1979,
        'country': 'Faroe Islands',
        },
    {
        'name': 'Finland',
        'founded': 1907,
        'country': 'Finland',
        },
    {
        'name': 'France',
        'founded': datetime.datetime(1919, 4, 7),
        'country': 'France',
        },
    {
        'name': 'Georgia',
        'founded': 1936,
        'country': 'Georgia',
        },
    {
        'name': 'Germany',
        'founded': datetime.datetime(1900, 1, 28),
        'country': 'Germany',
        },
    {
        'name': 'Greece',
        'founded': 1926,
        'country': 'Greece',
        },
    {
        'name': 'Hungary',
        'founded': 1901,
        'country': 'Hungary',
        },
    {
        'name': 'Iceland',
        'founded': 1947,
        'country': 'Iceland',
        },
    {
        'name': 'Ireland',
        'founded': 1921,
        'country': 'Ireland',
        },
    {
        'name': 'Israel',
        'founded': 1928,
        'country': 'Israel',
        },
    {
        'name': 'Lithuania',
        'founded': 1922,
        'country': 'Lithuania',
        },
    {
        'name': 'Luxembourg',
        'founded': 1908,
        'country': 'Luxembourg',
        },
    {
        'name': 'Romania',
        'founded': 1909,
        'country': 'Romania',
        },
    {
        'name': 'Russia',
        'founded': datetime.datetime(1912, 1, 19),
        'country': 'Russia',
        },
    {
        'name': 'Macedonia',
        'founded': 1949,
        'country': 'Macedonia',
        },
    {
        'name': 'Malta',
        'founded': 1900,
        'country': 'Malta',
        },
    {
        'name': 'Moldova',
        'founded': 1990,
        'country': 'Moldova',
        },
    {
        'name': 'Montenegro',
        'founded': 1931,
        'country': 'Montenegro',
        },
    {
        'name': 'Netherlands',
        'founded': 1889,
        'country': 'Netherlands',
        },

    {
        'name': 'Norway',
        'founded': 1902,
        'country': 'Norway',
        },
    {
        'name': 'Poland',
        'founded': 1919,
        'country': 'Poland',
        },
    {
        'name': 'Portugal',
        'founded': 1916,
        'country': 'Portugal',
        },
    {
        'name': 'Scotland',
        'founded': datetime.datetime(1873, 3, 13),
        'country': 'Scotland',
        },
    {
        'name': 'Switzerland',
        'founded': 1895,
        'country': 'Switzerland',
        },

    {
        'name': 'Turkey',
        'founded': 1923,
        'country': 'Turkey',
        },
    {
        'name': 'Ukraine',
        'founded': datetime.datetime(1991, 12, 13),
        'country': 'Ukraine',
        },
    {
        'name': 'Wales',
        'founded': 1876,
        'country': 'Wales',
        },
    {
        'name': 'Serbia',
        'founded': 1919,
        'country': 'Serbia',
        },
    {
        'name': 'Slovakia',
        'founded': 1938,
        'country': 'Slovakia',
        },
    {
        'name': 'Slovenia',
        'founded': 1920,
        'country': 'Slovenia',
        },
    {
        'name': 'Spain',
        'founded': 1909,
        'country': 'Spain',
        },
    {
        'name': 'Sweden',
        'founded': 1904,
        'country': 'Sweden',
        },
    {
        'name': 'San Marino',
        'founded': 1931,
        'country': 'San Marino',
        },
    {
        'name': 'Gibraltar',
        'founded': 1895,
        'country': 'Gibraltar',
        },
    {
        'name': 'East Germany',
        'founded': 1952,
        'dissolved': 1990,
        'country': 'East Germany',
        },

    {
        'name': 'Saarland',
        'founded': 1950,
        'dissolved': 1956,
        'country': 'Saarland',
        },

    {
        'name': 'U.S.S.R',
        'founded': datetime.datetime(1934, 12, 27),
        'dissolved': 1992,
        'country': 'USSR',
        'next': 'Russia',
        },
    {
        'name': 'Yugoslavia',
        'founded': 1919,
        'dissolved': 1991,
        'country': 'Yugoslavia',
        'next': 'Serbia',
        },
    {
        'name': 'Algeria',
        'founded': 1962,
        'country': 'Algeria',
        },
    {
        'name': 'Ivory Coast',
        'founded': 1960,
        'country': 'Ivory Coast',
        },
    {
        'name': 'Djibouti',
        'founded': 1979,
        'country': 'Djibouti',
        },
    {
        'name': 'Angola',
        'founded': 1979,
        'country': 'Angola',
        },
    {
        'name': 'Benin',
        'founded': 1962,
        'country': 'Benin',
        },
    {
        'name': 'Botswana',
        'founded': 1970,
        'country': 'Botswana',
        },
    {
        'name': 'Burkina Faso',
        'founded': 1960,
        'country': 'Burkina Faso',
        },
    {
        'name': 'Burundi',
        'founded': 1948,
        'country': 'Burundi',
        },
    {
        'name': 'Cameroon',
        'founded': 1959,
        'country': 'Cameroon',
        },
    {
        'name': 'Cape Verde',
        'founded': 1982,
        'country': 'Cape Verde',
        },
    {
        'name': 'Central African Republic',
        'founded': 1961,
        'country': 'Central African Republic',
        },
    {
        'name': 'Chad',
        'founded': 1962,
        'country': 'Chad',
        },
    {
        'name': 'Comoros',
        'founded': 1979,
        'country': 'Comoros',
        },
    {
        'name': 'Congo',
        'founded': 1962,
        'country': 'Congo',
        },
    {
        'name': 'Congo DR',
        'founded': 1919,
        'country': 'Congo DR',
        },
    {
        'name': 'Egypt',
        'founded': 1921,
        'country': 'Egypt',
        },
    {
        'name': 'Kenya',
        'founded': 1960,
        'country': 'Kenya',
        },
    {
        'name': 'Lesotho',
        'founded': 1932,
        'country': 'Lesotho',
        },
    {
        'name': 'Liberia',
        'founded': 1936,
        'country': 'Liberia',
        },
    {
        'name': 'Libya',
        'founded': 1962,
        'country': 'Libya',
        },
    {
        'name': 'Madagascar',
        'founded': 1961,
        'country': 'Madagascar',
        },
    {
        'name': 'Malawi',
        'founded': 1966,
        'country': 'Malawi',
        },
    {
        'name': 'Mauritania',
        'founded': 1961,
        'country': 'Mauritania',
        },
    {
        'name': 'Mali',
        'founded': 1960,
        'country': 'Mali',
        },
    {
        'name': 'Equatorial Guinea',
        'founded': 1960,
        'country': 'Equatorial Guinea',
        },
    {
        'name': 'Eritrea',
        'founded': 1996,
        'country': 'Eritrea',
        },
    {
        'name': 'Ethiopia',
        'founded': 1943,
        'country': 'Ethiopia',
        },
    {
        'name': 'Gabon',
        'founded': 1962,
        'country': 'Gabon',
        },
    {
        'name': 'Gambia',
        'founded': 1952,
        'country': 'Gambia',
        },
    {
        'name': 'Ghana',
        'founded': 1957,
        'country': 'Ghana',
        },
    {
        'name': 'Guinea',
        'founded': 1960,
        'country': 'Guinea',
        },
    {
        'name': 'Guinea-Bissau',
        'founded': 1974,
        'country': 'Guinea-Bissau',
        },
    {
        'name': 'Mauritius',
        'founded': 1952,
        'country': 'Mauritius',
        },
    {
        'name': 'Morocco',
        'founded': 1955,
        'country': 'Morocco',
        },
    {
        'name': 'Mozambique',
        'founded': 1976,
        'country': 'Mozambique',
        },
    {
        'name': 'Namibia',
        'founded': 1992,
        'country': 'Namibia',
        },
    {
        'name': 'Niger',
        'founded': 1967,
        'country': 'Niger',
        },
    {
        'name': 'Nigeria',
        'founded': 1945,
        'country': 'Nigeria',
        },
    {
        'name': 'Reunion',
        'founded': 1956,
        'country': 'Reunion',
        },
    {
        'name': 'Rwanda',
        'founded': 1972,
        'country': 'Rwanda',
        },
    {
        'name': 'Sao Tome and Principe',
        'founded': 1975,
        'country': 'Sao Tome and Principe',
        },

    {
        'name': 'Senegal', 
        'founded': 1960,
        'country': 'Senegal',
        },
    {
        'name': 'Seychelles',
        'founded': 1979,
        'country': 'Seychelles',
        },
    {
        'name': 'Sierra Leone',
        'founded': 1967,
        'country': 'Sierra Leone',
        },
    {
        'name': 'Somalia',
        'founded': 1960,
        'country': 'Somalia',
        },
    {
        'name': 'South Africa',
        'founded': datetime.datetime(1991, 12, 8),
        'country': 'South Africa',
        },
    {
        'name': 'Sudan',
        'founded': 1936,
        'country': 'Sudan',
        },
    {
        'name': 'South Sudan',
        'founded': 2011,
        'country': 'South Sudan',
        },
    {
        'name': 'Swaziland',
        'founded': 1968,
        'country': 'Swaziland',
        },
    {
        'name': 'Tanzania',
        'founded': 1930,
        'country': 'Tanzania',
        },
    {
        'name': 'Togo',
        'founded': 1960,
        'country': 'Togo',
        },
    {
        'name': 'Tunisia',
        'founded': 1956,
        'country': 'Tunisia',
        },
    {
        'name': 'Uganda',
        'founded': 1924,
        'country': 'Uganda',
        },
    {
        'name': 'Zanzibar',
        'founded': 1926,
        'country': 'Zanzibar',
        },
    {
        'name': 'Zambia',
        'founded': 1929,
        'country': 'Zambia',
        },
    {
        'name': 'Zimbabwe',
        'founded': 1965,
        'country': 'Zimbabawe',
        },
    {
        'name': 'Afghanistan',
        'founded': 1922,
        'country': 'Afghanistan',
        },

    {
        'name': 'Australia',
        'founded': 1911,
        'country': 'Australia',
        },
    {
        'name': 'Bahrain',
        'founded': 1957,
        'country': 'Bahrain',
        },
    {
        'name': 'Bangladesh',
        'founded': 1972,
        'country': 'Bangladesh',
        },
    {
        'name': 'Bhutan',
        'founded': 1983,
        'country': 'Bhutan',
        },

    {
        'name': 'Brunei',
        'founded': 1959,
        'country': 'Brunei',
        },
    {
        'name': 'Cambodia',
        'founded': 1933,
        'country': 'Cambodia',
        },
    {
        'name': 'China',
        'founded': 1924,
        'country': 'China',
        },
    {
        'name': 'Guam',
        'founded': 1975,
        'country': 'Guam',
        },
    {
        'name': 'Hong Kong',
        'founded': 1909,
        'country': 'Hong Kong',
        },
    {
        'name': 'India',
        'founded': datetime.datetime(1937, 6, 23),
        'country': 'India',
        },
    {
        'name': 'Indonesia',
        'founded': datetime.datetime(1930, 4, 19),
        'country': 'Indonesia',
        },
    {
        'name': 'Iran',
        'founded': 1920,
        'country': 'Iran',
        },
    {
        'name': 'Iraq',
        'founded': 1948,
        'country': 'Iraq',
        },
    {
        'name': 'Japan',
        'founded': 1921,
        'country': 'Japan',
        },
    {
        'name': 'Jordan',
        'founded': 1949,
        'country': 'Jordan',
        },
    {
        'name': 'North Korea',
        'founded': 1945,
        'country': 'North Korea',
        },
    {
        'name': 'South Korea',
        'founded': 1928,
        'country': 'South Korea',
        },
    {
        'name': 'Kuwait',
        'founded': 1952,
        'country': 'Kuwait',
        },
    {
        'name': 'Kyrgyzstan',
        'founded': 1992,
        'country': 'Kyrgyzstan',
        },
    {
        'name': 'Laos',
        'founded': 1951,
        'country': 'Laos',
        },
    {
        'name': 'Lebanon',
        'founded': 1933,
        'country': 'Lebanon',
        },
    {
        'name': 'Macao',
        'founded': 1939,
        'country': 'Macao',
        },
    {
        'name': 'Malaysia',
        'founded': 1933,
        'country': 'Malaysia',
        },
    {
        'name': 'Maldives',
        'founded': 1982,
        'country': 'Maldives',
        },
    {
        'name': 'Mongolia',
        'founded': 1959,
        'country': 'Mongolia',
        },
    {
        'name': 'Myanmar',
        'founded': 1947,
        'country': 'Myanmar',
        },
    {
        'name': 'Nepal',
        'founded': 1951,
        'country': 'Nepal',
        },
    {
        'name': 'Northern Mariana Islands',
        'founded': 2005,
        'country': 'Northern Mariana Islands',
        },
    {
        'name': 'Oman',
        'founded': 1978,
        'country': 'Oman',
        },
    {
        'name': 'Pakistan',
        'founded': 1947,
        'country': 'Pakistan',
        },
    {
        'name': 'Palestine',
        'founded': 1928,
        'country': 'Palestine',
        },
    {
        'name': 'Philippines',
        'founded': 1907,
        'country': 'Philippines',
        },
    {
        'name': 'Qatar',
        'founded': 1960,
        'country': 'Qatar',
        },
    {
        'name': 'Saudi Arabia',
        'founded': 1956,
        'country': 'Saudi Arabia',
        },
    {
        'name': 'Singapore',
        'founded': 1892,
        'country': 'Singapore',
        },
    {
        'name': 'Sri Lanka',
        'founded': 1939,
        'country': 'Sri Lanka',
        },
    {
        'name': 'Syria',
        'founded': 1936,
        'country': 'Syria',
        },
    {
        'name': 'Taiwan',
        'founded': 1936,
        'country': 'Taiwan',
        },
    {
        'name': 'Tajikstan',
        'founded': 1936,
        'country': 'Tajikstan',
        },
    {
        'name': 'Thailand',
        'founded': 1916,
        'country': 'Thailand',
        },
    {
        'name': 'Timor-Leste',
        'founded': 2002,
        'country': 'Timor-Leste',
        },
    {
        'name': 'Turkmenistan',
        'founded': 1992,
        'country': 'Turkmenistan',
        },
    {
        'name': 'United Arab Emirates',
        'founded': 1971,
        'country': 'United Arab Emirates',
        },
    {
        'name': 'Uzbekistan',
        'founded': 1946,
        'country': 'Uzbekistan',
        },
    {
        'name': 'Vietnam',
        'founded': 1962,
        'country': 'Vietnam',
        },
    {
        'name': 'Yemen',
        'founded': 1962,
        'country': 'Yemen',
        },
    {
        'name': 'American Samoa',
        'founded': 1984,
        'country': 'American Samoa',
        },
    {
        'name': 'Cook Islands',
        'founded': 1971,
        'country': 'Cook Islands',
        },
    {
        'name': 'Fiji',
        'founded': 1938,
        'country': 'Fiji',
        },
    {
        'name': 'Kiribati',
        'founded': 1980,
        'country': 'Kiribati',
        },
    {
        'name': 'New Caledonia',
        'founded': 1928,
        'country': 'New Caledonia',
        },
    {
        'name': 'New Zealand',
        'founded': 1891,
        'country': 'New Zealand',
        },
    {
        'name': 'Papua New Guinea',
        'founded': 1962,
        'country': 'Papua New Guinea',
        },
    {
        'name': 'Samoa',
        'founded': 1968,
        'country': 'Samoa',
        },
    {
        'name': 'Solomon Islands',
        'founded': 1978,
        'country': 'Solomon Islands',
        },
    {
        'name': 'Tahiti',
        'founded': 1938,
        'country': 'Tahiti',
        },
    {
        'name': 'Tonga',
        'founded': 1965,
        'country': 'Tonga',
        },
    {
        'name': 'Tuvalu',
        'founded': 1979,
        'country': 'Tuvalu',
        },
    {
        'name': 'Vanuatu',
        'founded': 1934,
        'country': 'Vanuatu',
        },
])

