#!/usr/local/bin/env python
# -*- coding: utf-8 -*-


import datetime

l = [
    {
        'name': 'Stadio Luigi Ferraris',
        'location': 'Genoa, Italy',
        'opened': datetime.datetime(1997, 4, 11),
        'capacity': 10000,
        'cost': 26000000,
        'architect': 'HOK Sport',
        },

    {
        'name': 'Stadio Flaminio',
        'location': 'Rome, Italy',
        'opened': 1959,
        'capacity': 32000,
        },

    {
        'name': 'Stadio Tommaso Fattori',
        'location': 'L\'Aquila, Italy',
        'opened': 1929,
        'capacity': 10000,
        },


    {
        'name': 'Generali Arena',
        'location': 'Prague, Czech Republic',
        'opened': 1969,
        'capacity': 20854
        },

    {
        'name': 'Estádio da Luz',
        'location': 'Lisbon, Portugal',
        'opened': 2003, # October 2003
        'capacity': 65647
        },

    {
        'name': 'Estádio Municipal de Braga',
        'location': 'Braga, Portugal',
        'opened': datetime.datetime(2003, 12, 30),
        'capacity': 30286,
        },

    {
        'name': 'Estádio das Antas',
        'location': 'Porto, Portugal',
        'opened': datetime.datetime(1952, 5, 28),
        'closed': 2004,
        'capacity': 50000,
        },

    {
        'name': 'Estádio D. Afonso Henriques',
        'location': 'Guimaraes, Portugal',
        'opened': 1965,
        'capacity': 30165
        },


    {
        'name': 'Stadio Renato Dall\'Ara',
        'location': 'Bologna, Italy',
        'opened': 1927,
        'capacity': 38279,
        },


    {
        'name': 'Loftus Road',
        'location': 'London, England',
        'opened': 1904,
        'capacity': 18500,
        },

    {
        'name': 'Anfield',
        'location': 'Liverpool, England',
        'opened': 1884,
        'capacity': 45276,
        },

    {
        'name': 'De Kuip',
        'location': 'Rotterdam, Netherlands',
        'opened': datetime.datetime(1937, 7, 23),
        'capacity': 51577
        },


    {
        'name': 'Easter Road',
        'location': 'Edinburgh, Scotland',
        'opened': 1893,
        'capacity': 20421,
        },


    {
        'name': 'Espenmoos',
        'location': 'St. Gallen, Switzerland',
        'opened': 1910,
        },


    {
        'name': 'The Hawthorns',
        'location': 'West Bromwich, England',
        'opened': 1900,
        'capacity': 26272,
        },




    {
        'name': 'UPC-Arena',
        'location': 'Graz, Austria',
        'opened': datetime.datetime(1997, 7, 9),
        'capacity': 15400,
        },

    {
        'name': 'Estadio Multiusos de San Lázaro',
        'location': 'Santiago de Compostela, Spain',
        'opened': datetime.datetime(1993, 6, 24),
        'capacity': 13000,
        },

    {
        'name': 'Estadi Cornellà-El Prat',
        'location': 'El Prat de Llobregat, Spain',
        'opened': datetime.datetime(2009, 8, 2),
        'capacity': 40500,
        },

    {
        'name': 'Stadio San Paolo',
        'location': 'Naples, Italy',
        'opened': datetime.datetime(1959, 12, 6),
        'capacity': 60240,
        },


    {
        'name': 'Stadio Armando Picchi',
        'location': 'Livorno, Italy',
        'opened': 1935,
        'capacity': 19238,
        },

    {
        'name': 'Stadio Adriatico',
        'location': 'Pescara, Italy',
        'opened': 1955,
        'capacity': 24400,
        },

    {
        'name': 'Kazimierza Gorskiego Stadium', 
        'location': 'Plock, Poland',
        },

    {
        'name': 'Stade Olympique Yves-du-Manoir',
        'location': 'Colombes, France',
        'opened': 1907,
        'capacity': 14000,
        },

    {
        'name': 'Stade Municipal de Toulouse',
        'location': 'Toulouse, France',
        'opened': 1937,
        'capacity': 35472,
        },

    {
        'name': 'Töölön Pallokenttä',
        'location': 'Helsinki, Finland',
        'opened': 1915,
        'capacity': 4000,
        },

    {
        'name': 'Stade du Fort Carré',
        'location': 'Antibes, France',
        'capacity': 7000,
        },

    {
        'name': 'Råsunda Stadium',
        'location': 'Solna, Stockholm, Sweden',
        'capacity': 36608,
        'opened': datetime.datetime(1937, 5, 17),
        },

    {
        'name': 'Råsunda Idrottplats',
        'location': 'Solna, Stockholm, Sweden',
        'opened': datetime.datetime(1910, 9, 18),
        },

    {
        'name': 'Traneberg Idrottplats',
        'location': 'Traneberg, Stockholm, Sweden',
        'opened': 1911,
        'closed': 1935
        },

    {
        'name': 'Bosuilstadion',
        'location': 'Antwerp, Belgium',
        'opened': datetime.datetime(1923, 11, 1),
        'capacity': 16649
        },

    {
        'name': 'Stedelijk Olympisch Stadion',
        'location': 'Antwerp, Belgium',
        'capacity': 12388,
        },

    {
        'name': 'Olympic Stadion',
        'location': 'Stockholm, Sweden',
        'opened': 1912,
        'capacity': 13145,
        },

    {
        'name': 'Arosvallen',
        'location': 'Västerås, Sweden',
        },

    {
        'name': 'Idrottsparken',
        'location': 'Norrköping, Sweden',
        'opened': 1904,
        'capacity': 16700,
        },

    {
        'name': 'Jernvallen',
        'location': 'Sandviken, Sweden',
        'opened': 1938,
        'capacity': 7000,
        },

    {
        'name': 'Ryavallen',
        'location': 'Boras, Sweden',
        'opened': 1941,
        },

    {
        'name': 'Eyravallen',
        'location': 'Orebro, Sweden',
        'opened': 1923,
        'capacity': 14500,
        },

    {
        'name': 'Malmö Stadion',
        'location': 'Malmo, Sweden',
        'opened': datetime.datetime(1958, 5, 28),
        'capacity': 26500,
        },

    {
        'name': 'Tunavallen',
        'location': 'Eskilstuna, Sweden',
        'opened': 1924,
        'capacity': 7800,
        },

    {
        'name': 'Rimnersvallen',
        'location': 'Uddevalla, Sweden',
        'opened': datetime.datetime(1923, 5, 5),
        'capacity': 10605,
        },

    {
        'name': 'Ullevi',
        'location': 'Gothenburg, Sweden',
        'opened': datetime.datetime(1958, 5, 29),
        'capacity': 43000,
        },


    {
        'name': 'Olympiastadion',
        'location': 'Munich, Germany',
        'opened': datetime.datetime(1972, 5, 26),
        'capacity': 69250,
        'architect': 'Frei Otto',
        },


    {
        'name': 'BayArena',
        'location': 'Leverkusen, Germany',
        'opened': datetime.datetime(1958, 8, 2),
        'capacity': 30210,
        'architect': 'Max Bogl',
        },

    {
        'name': 'Westfalenstadion',
        'location': 'Dortmund, Germany',
        'opened': datetime.datetime(1974, 4, 2),
        'capacity': 83000,
        },

    {
        'name': 'Weserstadion',
        'location': 'Bremen, Germany',
        'opened': 1924,
        'capacity': 42500,
        },

    {
        'name': 'Parkstadion',
        'location': 'Gelsenkirchen, Germany',
        'opened': datetime.datetime(1973, 8, 4),
        'closed': 2008,
        'capacity': 62008,
        },

    {
        'name': 'Stade Victor Boucquey',
        'location': 'Lille, France',
        'opened': 1902,
        'capacity': 15000,
        },

    {
        'name': 'Vélodrome de Vincennes',
        'location': 'Paris, France',
        'opened': 1894,
        },

    {
        'name': 'AWD-Arena',
        'location': 'Hanover, Germany',
        'opened': datetime.datetime(1954, 9, 26),
        'capacity': 49000,
        },

    {
        'name': 'Mercedes-Benz Arena',
        'location': 'Stuttgart, Germany',
        'opened': datetime.datetime(1933, 7, 23),
        'capacity': 60441,
        },

    {
        'name': 'Allianz Arena',
        'location': 'Munich, Germany',
        'opened': datetime.datetime(2005, 5, 30),
        'capacity': 66000,
        },

    {
        'name': 'Volksparkstadion',
        'location': 'Hamburg, Germany',
        'opened': datetime.datetime(1953, 7, 12),
        'capacity': 57000,
        },

    {
        'name': 'Volkswagen Arena',
        'location': 'Wolfsburg, Germany',
        'opened': datetime.datetime(2002, 12, 13),
        'capacity': 30000,
        'cost': 53000000,
        'denomination': 'Euros',
        },

    {
        'name': 'Camp Nou',
        'location': 'Barcelona, Spain',
        'opened': datetime.datetime(1957, 9, 24),
        'capacity': 99354,
        },

    {
        'name': 'Örjans Vall',
        'location': 'Halmstad, Sweden',
        'opened': datetime.datetime(1922, 7, 30),
        'capacity': 15500,
        },

    {
        'name': 'Estadi de Sarrià',
        'location': 'Barcelona, Spain',
        'opened': datetime.datetime(1923, 2, 18),
        'closed': datetime.datetime(1997, 9, 20),
        'capacity': 44000,
        },

    {
        'name': 'Campo de Fútbol de Vallecas',
        'location': 'Madrid, Spain',
        'opened': datetime.datetime(1978, 5, 10),
        'capacity': 14708,
        },


    {
        'name': 'Estadio San Mamés',
        'location': 'Bilbao, Spain',
        'opened': datetime.datetime(1913, 8, 21),
        'closed': datetime.datetime(2013, 6, 6),
        'capacity': 40000,
        },

    {
        'name': 'Estadio Benito Villamarín',
        'location': 'Seville, Spain',
        'opened': 1929,
        'capacity': 52745,
        },

    {
        'name': 'Estadio Santiago Bernabéu',
        'location': 'Madrid, Spain',
        'opened': datetime.datetime(1944, 10, 27),
        'capacity': 85454,
        },

    {
        'name': 'Stade Bergeyre',
        'location': 'Paris, France',
        'opened': 1918,
        'closed': 1926,
        },


    {
        'name': 'Estadio Vicente Calderón',
        'location': 'Madrid, Spain',
        'opened': datetime.datetime(1966, 10, 2),
        'capacity': 54960,
        },

    {
        'name': 'Antalya Atatürk Stadium',
        'location': 'Antalya, Turkey',
        'capacity': 11137,
        },

    {
        'name': 'Ali Sami Yen Stadium',
        'location': 'Istanbul, Turkey',
        'capacity': 23477,
        'opened': 1945,
        'closed': datetime.datetime(2011, 1, 11)
        },


    {
        'name': 'Kadir Has Stadium',
        'location': 'Kayseri, Turkey',
        'capacity': 32864,
        'opened': datetime.datetime(2009, 3, 8),
        },

    {
        'name': 'Kamil Ocak Stadium',
        'location': 'Gaziantep, Turkey',
        'capacity': 16981,
        'opened': 1974,
        },

    {
        'name': 'Hüseyin Avni Aker Stadium',
        'location': 'Trabzon, Turkey',
        'capacity': 24169,
        'opened': 1951,
        },

    {
        'name': 'Bursa Atatürk Stadium',
        'location': 'Bursa, Turkey',
        'capacity': 25213,
        'opened': 1979,
        },

    {
        'name': 'Asim Ferhatović Hase Stadium',
        'location': 'Sarajevo, Bosnia and Herzegovina',
        'capacity': 37500,
        'opened': 1947,
        },

    {
        'name': 'Türk Telekom Arena',
        'location': 'Istanbul, Turkey',
        'capacity': 52652,
        'opened': datetime.datetime(2011, 1, 15),
        },

    {
        'name': 'Akdeniz University Stadium',
        'location': 'Antalya, Turkey',
        'capacity': 7100,
        'opened': 2012,
        },

    {
        'name': 'Estadio José Rico Pérez',
        'location': 'Alicante, Spain',
        'opened': 1974,
        'capacity': 30000,
        },

    {
        'name': 'El Molinon',
        'location': 'Gijón, Spain',
        'opened': 1908,
        'capacity': 30000,
        },

    {
        'name': 'Estadio Riazor',
        'location': 'A Coruña, Spain',
        'opened': datetime.datetime(1944, 10, 28),
        'capacity': 34600,
        },

    {
        'name': 'Estadio La Rosaleda',
        'location': 'Málaga, Spain',
        'opened': datetime.datetime(1941, 9, 15),
        'capacity': 28963,
        },

    {
        'name': 'La Romareda',
        'location': 'Zaragoza, Spain',
        'opened': datetime.datetime(1957, 9, 8),
        'capacity': 34596,
        },

    {
        'name': 'Stade de la Mosson',
        'location': 'Montpellier, France',
        'opened': datetime.datetime(1927, 1, 13),
        'capacity': 32900,
        },

    {
        'name': 'Stade de la Meinau',
        'location': 'Strasbourg, France',
        'address': '12, rue de l\'Extenwoerth',
        'opened': 1914,
        'capacity': 29320,
        },

    {
        'name': 'Stade de la Cavée verte',         # 'name': 'Stade Charles-Argentin',
        'location': 'Le Havre, France',
        'address': 'Rue de la Cavée Verte',
        'opened': 1918,
        'closed': 1970, # really closed?
        'capacity': 22000
        },




    

    
    {
        'name': 'Stadion Galgenwaard',
        'location': 'Utrecht, Netherlands',
        'opened': datetime.datetime(2004, 8, 22),
        'capacity': 24426,
        },

    {
        'name': 'Univé Stadion',
        'location': 'Emmen, Netherlands',
        'opened': datetime.datetime(1977, 8, 27),
        'capacity': 8600,
        },

    {
        'name': 'Parkstad Limburg Stadion',
        'location': 'Kerkrade, Netherlands',
        'opened': datetime.datetime(2000, 8, 15),
        'capacity': 19979,
        },

    {
        'name': 'De Vijverberg',
        'location': 'De Graafschap, Netherlands',
        'capacity': 12600,
        },

    {
        'name': 'Tynecastle Stadium',
        'location': 'Edinburgh, Scotland',
        'opened': datetime.datetime(1886, 4, 10),
        'capacity': 17420,
        },

    {
        'name': 'Ibrox Stadium',
        'location': 'Glasgow, Scotland',
        'opened': datetime.datetime(1899, 12, 30),
        'capacity': 51082,
        },

    {
        'name': 'Trent Bridge',
        'location': 'Nottinghamshire, England',
        'opened': 1838,
        'capacity': 17500,
        },

    {
        'name': 'The Oval',
        'location': 'London, England',
        'opened': 1845,
        'capacity': 23500,
        },

    {
        'name': 'Millennium Stadium',
        'location': 'Cardiff, Wales',
        'opened': datetime.datetime(1999, 6, 26),
        'capacity': 74500,
        'cost': 121000000,
        'denomination': 'British pounds',
        },

    {
        'name': 'Ricoh Arena',
        'location': 'Coventry, England',
        'opened': 2005,
        'capacity': 32609,
        'cost': 113000000,
        'denomination': 'British pounds',
        },

    {
        'name': 'St James\' Park',
        'location': 'Newcastle, England',
        'opened': 1892,
        'capacity': 52387
        },

    {
        'name': 'Kaftanzoglio Stadium',
        'location': 'Thessaloniki, Greece',
        'opened': datetime.datetime(1960, 10, 27),
        'capacity': 27700,
        },

    {
        'name': 'Karaiskakis Stadium',
        'location': 'Athens, Greece',
        'opened': 1896,
        'capacity': 32115,
        },

    {
        'name': 'Olympics Stadium (Athens)',
        'location': 'Athens, Greece',
        'opened': 1982,
        'capacity': 75263,
        },


    {
        'name': 'Pankritio Stadium',
        'location': 'Heraklion, Greece',
        'opened': datetime.datetime(2004, 8, 11),
        'capacity': 26240,
        'cost': 50000000,
        'denomination': 'Euros',
        
        },

    {
        'name': 'Shepherds Bush Green',
        'location': 'London, England',
        },

    {
        'name': 'Wildparkstadion',
        'location': 'Karlsruhe, Germany',
        'opened': datetime.datetime(1955, 8, 7),
        'capacity': 29699
        },
    {
        'name': 'RheinEnergieStadion',
        'location': 'Cologne, Germany',
        'opened': datetime.datetime(1923, 9, 16),
        'capacity': 50000,
        },

    {
        'name': 'Rheinstadion',
        'location': 'Dusseldorf, Germany',
        'opened': 1925,
        'closed': datetime.datetime(2002, 6, 22),
        'capacity': 54000,
        },

    {
        'name': 'Frankenstadion',
        'location': 'Nuremberg, Germany',
        'opened': 1928,
        'capacity': 48548,
        },

    {
        'name': 'Commerzbank-Arena',
        'location': 'Frankfurt, Germany',
        'opened': datetime.datetime(1925, 5, 21),
        'capacity': 51500
        },

    {
        'name': 'Red Bull Arena (Leipzig)',
        'location': 'Leipzig, Germany',
        'opened': datetime.datetime(1956, 8, 4),
        'capacity': 44345,
        },

    {
        'name': 'Red Bull Arena (Salzburg)',
        'location': 'Salzburg, Austria',
        'opened': datetime.datetime(2003, 3, 8),
        'capacity': 31895,
        },

    {
        'name': 'Tivoli-Neu',
        'location': 'Innsbruck, Austria',
        'opened': datetime.datetime(2000, 9, 8),
        'capacity': 17400,
        },



    {
        'name': 'Invicta Ground',
        'location': 'London, England',
        'opened': 1890,
        'capacity': 12000,
        },


    {
        'name': 'Koning Willem II Stadion',
        'location': 'Tilburg, Netherlands',
        'capacity': 14637,
        'opened': 1995,
        },


    {
        'name': 'Stade Chaban-Delmas',
        'location': 'Bordeaux, France',
        'opened': datetime.datetime(1938, 6, 12),
        'capacity': 34694,
        },

    {
        'name': 'Dalymount Park',
        'location': 'Dublin, Ireland',
        'opened': datetime.datetime(1901, 9, 7),
        'capacity': 4300,

        },

    {
        'name': 'Ayresome Park',
        'opened': 1903,
        'closed': 1995,
        'capacity': 26667,
        'location': 'Middlesbrough, England',
        },

    {
        'name': 'Stade de Gerland',
        'address': '353, Avenue Jean-Jaurès, 69007',
        'location': 'Lyons, France',
        'opened': 1926,
        'capacity': 40500,
        
        },

    {
        'name': 'Stade de la Beaujoire', 
        'location': 'Nante, France',
        'address': 'Route de Saint Joseph 44300',
        'opened': datetime.datetime(1984, 5, 8),
        'capacity': 38285,
        },

    {
        'name': 'Parc des Princes',
        'location': 'Paris, France',
        'opened': datetime.datetime(1897, 7, 18),
        'capacity': 48712,

        },

    {
        'name': 'Stade Roi Baudouin',
        'location': 'Brussels, Belgium',
        },


    {
        'name': 'Stadio Cibali',
        'location': 'Catania, Italy',
        },
    {
        'name': 'Osteestadion',
        'location': 'Rostock, Germany',
        },

    {
        'name': 'Stade la Beaujoire',
        'location': 'Nantes, France',
        },

    {
        'name': 'Stade Geoffroy-Guichard',
        'location': 'St. Etienne, France',
        'opened': datetime.datetime(1931, 9, 13),
        'capacity': 26747,
        },

    {
        'name': 'Stade Félix-Bollaert',
        'location': 'Lens, France',
        'opened': 1933,
        'capacity': 41229,
        },

    {
        'name': 'Moscow Dinamo Stadium', 
        'location': 'Moscow, Russia',
        'opened': 1928,
        'closed': 2008,
        'capacity': 36540,
        },

    {
        'name': 'Petrovsky Stadium',
        'location': 'Saint Petersburg, Russia',
        'opened': datetime.datetime(1925, 7, 26),
        'capacity': 21504,
        },

    {
        'name': 'Kiev Olympic Stadium',
        'location': 'Kiev, Ukraine',
        'opened': datetime.datetime(1923, 8, 12),
        'closed': 2008,
        'capacity': 70050,
        },

    {
        'name': 'Donbass Stadium',
        'location': 'Donetsk, Ukraine',
        'opened': datetime.datetime(2009, 8, 29),
        'capacity': 52518,
        },


    {
        'name': 'Luzhniki Stadium',
        'location': 'Moscow, Russia',
        'opened': datetime.datetime(1956, 7, 31),
        'capacity': 78360,
        },

    {
        'name': 'Kirov Stadium',
        'location': 'St. Petersburg, Russia',
        'opened': datetime.datetime(1950, 7, 30),
        'closed': datetime.datetime(2006, 8, 17),
        'capacity': 100000,
        },

    {
        'name': 'Kuban Stadium',
        'location': 'Krasnodar, Russia',
        'opened': datetime.datetime(1961, 5, 14),
        'capacity': 31654,
        },
    {
        'name': 'Stadion Maksimir',
        'location': 'Zagreb, Croatia',
        'opened': datetime.datetime(1912, 5, 5),
        'capacity': 38079,
        },

    {
        'name': 'Estadio Nuevo José Zorrilla',
        'location': 'Valladolid, Spain',
        'address': 'Avenida del Mundial 82',
        'opened': datetime.datetime(1982, 2, 20),
        'capacity': 26512,
        },


    {
        'name': 'Estadio Ramón Sánchez Pizjuán',
        'location': 'Seville, Spain',
        'opened': datetime.datetime(1958, 9, 7),
        'capacity': 45500
        },

    {
        'name': 'Iberostar Stadium',
        'location': 'Palma, Spain',
        'opened': 1999,
        'capacity': 23142,
        },

    {
        'name': 'Estadio Manuel Martínez Valero',
        'location': 'Alicante, Spain',
        'opened': datetime.datetime(1976, 9, 8),
        'capacity': 39000,
        },



    {
        'name': 'EasyCredit-Stadion', 
        'location': 'Nuremberg, Germany',
        },
    {
        'name': 'Fritz Walter Stadion', 
        'location': 'Kaiserslautern, Germany',
        },

    {
        'name': 'Veltins-Arena', 
        'location': 'Gelsenkirchen, Germany',
        'opened': 2001,
        'cost': 191000000,
        'denomination': 'Euro',
        'architect': 'Hentrich, Petschnigg, und Partner',
        'capacity': 61673,
        },

    {
        'name': 'Ullevaal Stadium', 
        'location': 'Oslo, Norway',
        },

    {
        'name': 'Lerkendal Stadion',
        'location': 'Trondheim, Norway',
        'opened': datetime.datetime(1947, 8, 10),
        'capacity': 21166,
        },

    {
        'name': 'Bislett Stadion',
        'location': 'Oslo, Norway',
        'opened': 1922,
        'closed': 2004,
        },

    {
        'name': 'Amsterdam Olympic Stadium',
        'location': 'Amsterdam, Netherlands',
        'opened': datetime.datetime(1928, 5, 17),
        'capacity': 22288,
        },

    {
        'name': 'Estádio do Restelo',
        'location': 'Lisbon, Portugal',
        'opened': datetime.datetime(1956, 9, 23),
        'capacity': 25000,
        },

    {
        'name': 'Estádio José Alvalade',
        'location': 'Lisbon, Portugal',
        'opened': datetime.datetime(2003, 8, 6),
        'capacity': 50049,
        },

    {
        'name': 'Estádio do Dragão',
        'location': 'Porto, Portugal',
        'opened': datetime.datetime(2003, 11, 16),
        'capacity': 52399,
        },

    {
        'name': 'Estádio do Bonfim',
        'location': 'Setúbal, Portugal',
        'opened': datetime.datetime(1962, 9, 16),
        'capacity': 18694,
        },
    

    {
        'name': 'Laugardalsvollur', 
        'location': 'Reykjavik, Iceland',
        },
    {
        'name': 'Melavollur', 
        'location': 'Reykjavik, Iceland',
        },

    {
        'name': 'Inonu Stadium',
        'location': 'Istanbul, Turkey',
        'opened': datetime.datetime(1947, 5, 19),
        'architect': 'Paolo Vietti-Violi',
        'capacity': 32145,
        },

    {
        'name': 'Şükrü Saracoğlu Stadium',
        'location': 'Istanbul, Turkey',
        'opened': 1908,
        'capacity': 50509,
        },

    {
        'name': 'AEL FC Arena',
        'location': 'Larissa, Greece',
        'opened': 2010,
        'capacity': 16118,
        },

    {
        'name': 'Georgios Karaiskakis Stadium',
        'location': 'Piraeus, Greece',
        'opened': 2010,
        'capacity': 16118,
        },

    {
        'name': 'Valeriy Lobanovskyi Dynamo Stadium',
        'location': 'Kiev, Ukraine',
        'opened': 1934,
        'capacity': 16873,
        },

    {
        'name': 'Zdzisław Krzyszkowiak Stadium',
        'location': 'Bydgoszcz, Poland',
        'opened': 1960,
        'capacity': 20247,
        },


    {
        'name': 'Stadion Mladost',
        'location': 'Strumica, Macedonia',
        'opened': 1950,
        'capacity': 6500,
        },

    {
        'name': 'Polish Army Stadium',
        'location': 'Warsaw, Poland',
        },
    {
        'name': 'Nepstadion',
        'location': 'Budapest, Hungary',
        'opened': 1953,
        'capacity': 39111,
        },

    {
        'name': 'LKS Stadium',
        'location': 'Lodz, Poland',
        },

    {
        'name': 'Stadio Artemio Franchi',
        'location': 'Florence, Italy',
        'opened': 1931,
        'capacity': 47290,
        },

    {
        'name': 'Stadio San Nicola',
        'location': 'Bari, Italy',
        'opened': 1990,
        'capacity': 58270,
        
        },

    {
        'name': 'Stade Vélodrome',
        'location': 'Marseilles, France',
        'opened': 1937,
        'capacity': 42000,
        
        },
    {
        'name': 'Stadio Olimpico',
        'location': 'Rome, Italy',
        'opened': 1937,
        'capacity': 70634,
        },

    {
        'name': 'Stadio delle Alpi',
        'location': 'Turin, Italy',
        'opened': 1990,
        'closed': 2006,
        'capacity': 69000,
        },

    {
        'name': 'Juventus Stadium',
        'location': 'Turin, Italy',
        'opened': datetime.datetime(2011, 9, 8),
        'capacity': 41000,
        },

    {
        'name': 'Stadio Olimpico di Torino',
        'location': 'Turin, Italy',
        'opened': datetime.datetime(1933, 5, 14),
        'capacity': 28140,
        },

    {
        'name': 'Stadio Giorgio Ascarelli',
        'location': 'Naples, Italy',
        'capacity': 40000,
        },


    {
        'name': 'Stadio Giuseppe Grezar',
        'location': 'Trieste, Italy',
        'opened': 1932,
        'closed': 1992,
        'capacity': 8000,
        },

    {
        'name': 'Stadio Renzo Barbera',
        'location': 'Palermo, Italy',
        'opened': datetime.datetime(1932, 1, 24),
        'capacity': 36349,
        },


    {
        'name': 'Frogner Stadium',
        'location': 'Oslo, Norway',
        
        },

    {
        'name': 'Signal Iduna Park', 
        'location': 'Dortmund, Germany',
        },

    {
        'name': 'A. Le Coq Arena',
        'location': 'Tallinn, Estonia',
        'opened': datetime.datetime(2001, 6, 2),
        'capacity': 9692,
        },

    {
        'name': 'Ernst-Happel-Stadion',
        'location': 'Vienna, Austria',
        'opened': datetime.datetime(1931, 7, 11),
        'capacity': 50000,
        },

    {
        'name': 'Stade Alphonse Theis',
        'location': 'Hesperange, Luxembourg',
        'capacity': 3058,
        },


    {
        'name': 'Windsor Park',
        'location': 'Belfast, Northern Ireland',
        'opened': 1905,
        'capacity': 12950,
        },


    {
        'name': 'Antonis Papadopoulos Stadium',
        'location': 'Larnaca, Cyprus',
        'opened': 1986,
        'capacity': 10230,
        },

    {
        'name': 'Fritz-Walter-Stadion', 
        'location': 'Kaiserslautern, Germany',
        },


    {
        'name': 'Lansdowne Road',
        'location': 'Dublin, Ireland',
        'opened': 1872,
        'closed': datetime.datetime(2006, 12, 31),
        'capacity': 48000,
        },

    {
        'name': 'Na Stínadlech',
        'location': 'Teplice, Czech Republic',
        'opened': datetime.datetime(1973, 5, 9),
        'capacity': 18221,
        },


    {
        'name': 'Stadio Nazionale del PNF',
        'location': 'Rome, Italy',
        'opened': 1927,
        'closed': 1953,
        'capacity': 50000,
        },

    {
        'name': 'San Siro',
        'location': 'Milan, Italy',
        'opened': datetime.datetime(1926, 9, 19),
        'capacity': 80018,
        },

    {
        'name': 'Stadio Marc\'Antonio Bentegodi',
        'location': 'Verona, Italy',
        'opened': 1963,
        'capacity': 39371,
        },

    {
        'name': 'Stadio Sant\'Elia',
        'location': 'Cagliari, Italy',
        'opened': 1970,
        'capacity': 23486,
        },

    {
        'name': 'Stade Pershing',
        'location': 'Vincennes, France',
        },

    {
        'name': 'Stadio Friuli',
        'location': 'Udine, Italy',
        'opened': 1976,
        'capacity': 30642,
        },
    {
        'name': 'Agrykola Stadium',
        'location': 'Warsaw, Poland',
        },
    {
        'name': 'Warta Stadium',
        'location': 'Poznan, Poland',
        'opened': 1912,
        'capacity': 60000,
        
        },

    {
        'name': 'Griffin Park',
        'location': 'London, England',
        'opened': 1904,
        'capacity': 12763,
        },

    {
        'name': 'Stamford Bridge',
        'location': 'London, England',
        'opened': datetime.datetime(1877, 4, 28),
        'capacity': 41798,
        },

    {
        'name': 'De Grolsch Veste',
        'location': 'Enschede, Netherlands',
        'opened': datetime.datetime(1998, 5, 10),
        'capacity': 30206,
        },

    {
        'name': 'Craven Cottage',
        'location': 'London, England',
        'opened': 1896,
        'capacity': 25700,
        },

    {
        'name': 'Hampden Park', 
        'location': 'Glasgow, Scotland',
        'opened': 1903,
        'capacity': 52063,
        },

    

    {
        'name': 'Stozice Stadium',
        'location': 'Ljubljana, Slovenia',
        },

    {
        'name': 'NRGi Park',
        'location': 'Aarhus, Denmark',
        'opened': datetime.datetime(1920, 6, 5),
        'capacity': 20032,
        },


    {
        'name': 'Tehelne Pole',
        'location': 'Bratislava, Slovakia',
        'opened': 1940,
        'closed': 2010,
        'capacity': 30085,
        },

    {
        'name': 'Amsterdam ArenA',
        'location': 'Amsterdam, Netherlands',
        'opened': datetime.datetime(1996, 8, 14),
        'cost': 140000000,
        'denomination': 'Euro',
        'capacity': 52342,
        },

    {
        'name': 'Philips Stadion',
        'location': 'Eindhoven, Netherlands',
        'opened': datetime.datetime(1910, 12, 12),
        'capacity': 35000,
        },

    {
        'name': 'Estadio El Sardinero',
        'opened': 1988,
        'capacity': 22222,
        'location': 'Santander, Spain',
        },

    {
        'name': 'Coliseum Alfonso Pérez',
        'opened': 1998,
        'location': 'Getafe, Spain',
        },

    {
        'name': 'Anoeta',
        'opened': 1993,
        'capacity': 32076,
        'location': 'San Sebastian, Spain',
        },

    {
        'name': 'Estadio de Mestalla',
        'location': 'Valencia, Spain',
        'opened': datetime.datetime(1923, 5, 20),
        'capacity': 55000,
        },

    {
        'name': 'Estadi Ciutat de València',
        'location': 'Valencia, Spain',
        'opened': 1969,
        'capacity': 25354
        },

    {
        'name': 'Estadio Carlos Tartiere',
        'location': 'Oviedo, Spain',
        'opened': datetime.datetime(2000, 9, 20),
        'capacity': 30500,
        },

    {
        'name': 'Estadi de la Nova Creu Alta',
        'location': 'Sabadell, Spain',
        'opened': datetime.datetime(1967, 8, 20),
        'capacity': 12000,
        },

    {
        'name': 'La Romareda',
        'location': 'Zaragoza, Spain',
        'opened': datetime.datetime(1957, 9, 8),
        'capacity': 34596,
        },

    {
        'name': 'Wembley Stadium',
        'location': 'London, England',
        'opened': 1923,
        'closed': 2000,
        'capacity': 82000,
        'cost': 750000,
        'denomination': 'British pounds',
        },


    {
        'name': 'Goodison Park',
        'location': 'Liverpool, England',
        'opened': datetime.datetime(1892, 8, 24),
        'capacity': 39571,
        'cost': 3000,
        'denomination': 'British pounds',
        },



    {
        'name': 'Hillsborough Stadium',
        'location': 'Sheffield, England',
        'opened': datetime.datetime(1899, 9, 2),
        'capacity': 39732
        },

    {
        'name': 'Arsenal Stadium',
        'location': 'London, England',
        'opened': datetime.datetime(1913, 9, 6),
        'closed': datetime.datetime(2006, 5, 7),
        'capacity': 38419,
        },

    {
        'name': 'Selhurst Park',
        'location': 'London, England',
        'opened': 1924,
        'capacity': 26309,
        },

    {
        'name': 'White Hart Lane',
        'location': 'London, England',
        'opened': datetime.datetime(1899, 9, 4),
        'capacity': 36230,
        },


    {
        'name': 'Roker Park',
        'location': 'Sunderland, England',
        'opened': 1897,
        'closed': 1998,
        'architect': 'Archibald Leitch',
        'capacity': 22500,
        },


    {
        'name': 'Villa Park',
        'location': 'Birmingham,England',
        'opened': 1897,
        'capacity': 42788,
        'cost': 16733,
        'denomination': 'British pounds',
        },



    {
        'name': 'Old Trafford',
        'location': 'Manchester,England',
        'opened': datetime.datetime(1910, 2, 19),
        'capacity': 75765,
        'cost': 90000,
        'denomination': 'British pounds',
        },

    {
        'name': 'White City Stadium',
        'location': 'London,England',
        'opened': 1908,
        'closed': 1984,
        'capacity': 93000,
        },

    {
        'name': 'Wisla Stadium',
        'location': 'Krakow, Poland',
        },

    {
        'name': 'Cornaredo Stadium',
        'location': 'Lugano, Switzerland',
        'opened': 1951,
        'capacity': 15900,
        },

    {
        'name': 'Stadion Allmend',
        'location': 'Lucerne, Switzerland',
        'opened': 1934,
        'capacity': 13000,
        },

    {
        'name': 'Espenmoos Stadium',
        'location': 'St. Gallen, Switzerland',
        'opened': 1910,
        },

    {
        'name': 'Wankdorf Stadium',
        'location': 'Bern, Switzerland',
        'opened': datetime.datetime(1925, 10, 18),
        'capacity': 64000,
        },


    {
        'name': 'Hardturm',
        'location': 'Zurich, Switzerland',
        'opened': 1929,
        'closed': datetime.datetime(2007, 9, 1),
        'capacity': 64000,
        },

    {
        'name': 'Stade Olympique de la Pontaise',
        'location': 'Lausanne, Switzerland',
        'opened': 1904,
        'capacity': 15850,
        },

    {
        'name': 'Charmilles Stadium',
        'location': 'Geneve, Switzerland',
        'opened': 1930,
        'closed': 2002,
        'capacity': 9250,
        },

    {
        'name': 'Stade de Genève',
        'location': 'Geneve, Switzerland',
        'opened': datetime.datetime(2003, 4, 30),
        'capacity': 30084,
        },

    {
        'name': 'Stade de Suisse',
        'location': 'Bern, Switzerland',
        'opened': datetime.datetime(2005, 7, 30),
        'capacity': 32000,
        },

    {
        'name': 'Letzigrund',
        'location': 'Zurich, Switzerland',
        'opened': datetime.datetime(2007, 8, 30),
        'capacity': 25000,
        },

    {
        'name': 'St. Jakob-Park',
        'location': 'Basel, Switzerland',
        'opened': datetime.datetime(2001, 3, 15),
        'cost': 220000000,
        'denomination': 'Swiss franc',
        'architect': 'Herzog & de Meuron',
        },

    {
        'name': 'Ullevi Stadium',
        'location': 'Goteborg, Sweden',
        },

    {
        'name': 'Estadio Chamartín',
        'location': 'Madrid, Spain',
        'opened': datetime.datetime(1923, 5, 17),
        'closed': 1947,
        'capacity': 22500,
        },

    {
        'name': 'Estadio El Madrigal',
        'location': 'Villarreal, Spain',
        'opened': datetime.datetime(1923, 6, 17),
        'capacity': 22000,
        },

    {
        'name': 'Balaídos',
        'location': 'Vigo, Spain',
        'opened': datetime.datetime(1928, 12, 30),
        'capacity': 31800,
        },

    {
        'name': 'Dynama Stadium (Minsk)',
        'location': 'Minsk, Belarus',
        'opened':1934,
        'capacity': 40000,
        },



    {
        'name': 'Stade de France',
        'location': 'Paris, France',
        'opened': datetime.datetime(1998, 1, 28),
        'capacity': 81338,
        'cost': 290000000,
        'denomination': 'Euro',
        },

    {
        'name': 'Stade du Ray',
        'location': 'Nice, France',
        'opened': datetime.datetime(1927, 1, 30),
        'capacity': 18696,
        },

    {
        'name': 'Stadionul Steaua',
        'location': 'Bucharest, Romania',
        'opened': datetime.datetime(1974, 4, 9),
        'capacity': 27557,
        },

]
