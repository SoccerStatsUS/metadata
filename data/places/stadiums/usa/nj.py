#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

import datetime

l = [

    {
        'name': 'Lubetkin Field',
        'location': 'Newark, NJ',
        },

    {
        'name': 'Newark Schools Stadium',
        'address': '450 Bloomfield Avenue',
        'location': 'Newark, NJ',
        'opened': 1925,
        'closed': 2009,
        'capacity': 15000,
        },
    {
        'name': 'Red Bull Arena',
        'address': '600 Cape May Street',
        'location': 'Harrison, NJ',
        'opened': datetime.datetime(2010, 3, 20),
        'cost': 200000000,
        'architect': 'Rossetti Architects',
        'capacity': 25000,
        },
    {
        'name': 'Giants Stadium',
        'address': '50 Route 120',
        'location': 'East Rutherford, NJ',
        'capacity': 80242,
        'cost': 78000000,
        'opened': datetime.datetime(1976, 10, 10),
        'closed': datetime.datetime(2010, 1, 3),
        'architect': 'Kivett and Myers',
        },        
    {
        'name': 'MetLife Stadium',
        'address': 'One MetLife Stadium Drive',
        'location': 'East Rutherford, NJ',
        'opened': datetime.datetime(2010, 4, 10),
        'cost': 1600000000,
        'architect': '360 Architecture',
        'capacity': 82566,
        },
    
    {
        'name': 'High Point Solutions Stadium',
        'address': '1 Scarlet Knight Way',
        'location': 'Piscataway, NJ',
        'opened': datetime.datetime(1994, 9, 3),
        'cost': 28000000,
        'architect': 'GSGSBH',
        'capacity': 52454,
        },

    {
        'name': 'Yurcak Field',
        'location': 'Piscataway, NJ',
        'opened': 1994,
        'cost': 28000000,
        'capacity': 5000,
        },

    {
        'name': 'Meadowbrook Oval',
        'location': 'Newark, NJ',
        'address': 'South Orange Avenue and 12th Street',
        },

    {
        'name': 'TD Bank Ballpark',
        'location': 'Bridgewater, NJ',
        'opened': datetime.datetime(1999, 6, 7),
        'capacity': 6100,
        'cost': 18000000,
        },

    {
        'name': 'Sprague Field',
        'location': 'Montclair, NJ',
        'capacity': 5700,
        },

    {
        'name': 'Pittser Field',
        'location': 'Montclair, NJ',
        # Are these the same?
        },


    {
        'name': 'Transamerica Field',
        'location': 'Charlotte, NC',
        'capacity': 20000,
        'opened': datetime.datetime(1996, 2, 25),
        'cost': 2100000,
        },

    {
        'name': 'Clark ONT Field',
        'location': 'East Newark, NJ',
        'opened': 1885,
        'capacity': 0,
        },

    {
        'name': 'J. Malcolm Simon Stadium',
        'location': 'Newark, NJ',
        },    

    {
        'name': 'The Great Lawn',
        'location': 'West Long Branch, NJ',
        },    

    {
        'name': 'Montclair State University',
        'location': 'Upper Montclair, NJ',
        },
    {
        'name': 'Dreamland Park',
        'location': 'Newark, NJ',
        },
    {
        'name': 'Newark School Stadium', 
        'location': 'Newark, NJ',
        },

    {
        'name': 'Winslow Township High School',
        'location': 'Winslow Township, NJ',
        },

    {
        'name': 'Cosmopolitan Park',
        'location': 'East Newark, NJ',
        },
    {
        'name': 'College Field',
        'location': 'Princeton, NJ',
        },

    {
        'name': 'Hetzel\'s Grove',
        'location': 'Trenton, NJ',
        },
    {
        'name': 'Domestic Baseball Grounds',
        'location': 'Newark, NJ',
        },
    {
        'name': 'Bartell\'s Park',
        'location': 'Newark, NJ',
        },
    {
        'name': 'Caledonian Park',
        'location': 'Newark, NJ',
        },
    
    {
        'name': 'Emmet Street Grounds',
        'location': 'Newark, NJ',
        },
    {
        'name': 'Olympic Grounds',
        'location': 'Paterson, NJ',
        },
    {
        'name': 'Trenton Cricket Grounds',
        'location': 'Trenton, NJ',
        },

    {
        'name': 'Frelinghuysen Grounds',
        'location': 'Newark, NJ',
        },

    {
        'name': 'Weidenmayer\'s Park',
        'location': 'Newark, NJ',
        },
    {
        'name': 'St. George\'s Cricket Grounds',
        'location': 'Hoboken, NJ',
        },

    {
        'name': 'Liberty Grounds',
        'location': 'Trenton, NJ',
        },
    {
        'name': 'Elysian Fields',
        'location': 'Hoboken, NJ',
        },

    {
        'name': 'Americus Park',
        'location': 'West Hoboken, NJ',
        },
    {
        'name': 'Federal League Baseball Grounds',
        'location': 'Harrison, NJ',
        },

    {
        'name': 'Scots Field',
        'location': 'Kearny, NJ',
        },

    {
        'name': 'Morris Park',
        'location': 'Newark, NJ',
        },
    {
        'name': 'Harrison Oval',
        'location': 'Harrison, NJ',
        },

    {
        'name': 'Trades\' League Grounds',
        'location': 'Trenton, NJ',
        },
    
    {
        'name': 'Roosevelt Stadium',
        'location': 'Jersey City, NJ',
        },

    {
        'name': 'Washburn Park',
        'location': 'Jersey City, NJ',
        },        
    {
        'name': 'West End Grounds',
        'location': 'Jersey City, NJ',
        },        

    
    {
        'name': 'Ruppert Stadium',
        'location': 'Newark, NJ',
        'opened': 1926,
        'closed': 1967,
        'capacity': 12000,
        },

    {
        'name': 'Ryle Park',
        'location': 'Paterson, NJ',
        },
    {
        'name': 'Carey Stadium',
        'location': 'Ocean City, NJ',
        },

    {
        'name': 'Newark Rink',
        'location': 'Newark, NJ',
        },        
    {
        'name': 'Olympic Field',
        'location': 'Paterson, NJ',
        },
    
    {
        'name': 'Harrison Field',
        'location': 'Harrison, NJ',
        },
    {
        'name': 'Federal Field',
        'location': 'Harrison, NJ',
        },
    {
        'name': 'West Hudson Athletic Field',
        'location': 'Harrison, NJ',
        },

    {
        'name': 'Washington Oval',
        'location': 'Kearny, NJ',
        },
    {
        'name': 'Ironbound Field',
        'location': 'Newark, NJ',
        },

    {
        'name': 'Turn Verein Field',
        'location': 'Newark, NJ',
        },

    {
        'name': 'East State Street Grounds',
        'location': 'Trenton, NJ',
        },
    {
        'name': 'Wright Street Grounds',
        'location': 'Newark, NJ',
        },
    {
        'name': 'Shooting Park',
        'location': 'Newark, NJ',
        },

    {
        'name': 'Farcher\'s Grove',
        'location': 'Union, NJ',
        },


    ]
