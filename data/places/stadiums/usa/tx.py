#!/usr/local/bin/env python
# -*- coding: utf-8 -*-


import datetime

l = [

    {
        'name': 'Lake Cliff Park',
        'location': 'Dallas, TX',
        },

    {
        'name': 'Westcott Field',
        'location': 'University Park, TX',
        'capacity': 4000,
        },

    {
        'name': 'Toyota Field',
        'address': 'Thousand Oaks Drive',
        'location': 'San Antonio, TX',
        'opened': datetime.datetime(2013, 4, 13),
        'capacity': 8000,
        },

    {
        'name': 'Herman Clark Stadium',
        'location': 'Fort Worth, TX',
        'opened': 1970,
        'capacity': 12000,
        },

    {
        'name': 'TAMIU Soccer Complex',
        'address': '5201 University Boulevard',
        'location': 'Laredo, TX',
        'capacity': 4000,
        'opened': 2006,
        },

    {
        'name': 'Grande Communications Stadium',
        'location': 'Midland, TX',
        'opened': 2002,
        'capacity': 18000,
        },

    {
        'name': 'Woodforest Bank Stadium',
        'address': '19115 David Memorial Drive',
        'location': 'Shenandoah, TX',
        'capacity': 9600,
        'opened': 2008,
        },

    {
        'name': 'Heroes Stadium',
        'address': '4799 Thousand Oaks Dr',
        'location': 'San Antonio, TX',
        'opened': datetime.datetime(2009, 8, 28),
        'capacity': 11122,
        
        },

    {
        'name': 'Houston Amateur Sports Park',
        'address': '12131 Kirby Dr',
        'location': 'Houston, TX',
        },

    {
        'name': 'Samuell Field',
        'location': 'Dallas, TX',
        },

    {
        'name': 'Edinburg Stadium',
        'address': 'Sugar Road at Schunior Street',
        'location': 'Edinburg, TX',
        'architect': 'Cotera, Kolar, Negrete & Reed',
        'opened': 2001,
        'cost': 5300000,
        'capacity': 4000,
        },

    {
        'name': 'Sun Bowl Stadium',
        'address': 'Sun Bowl Drive',
        'location': 'El Paso, TX',
        },

    {
        'name': 'adidas Field',
        'location': 'Frisco, TX',
        },

    {
        'name': 'Carl Lewis Track & Field Stadium',
        'location': 'Houston, TX',
        },
    {
        'name': 'Pennington Field',
        'location': 'Bedford, TX',
        },


    {
        'name': 'Dallas University Field',
        'location': 'Dallas, TX',
        },

    {
        'name': 'Gaston Park',
        'location': 'Dallas, TX',
        'opened': 1902,
        'closed': 1914,
        },


    {
        'name': 'Burnett Field',
        'location': 'Dallas, TX',
        'opened': 1924,
        'closed': 1964,
        'capacity': 10500,
        },
    
    {
        'name': 'P.C. Cobb Stadium',
        'location': 'Dallas, TX',
        'opened': 1939,
        'architect': 'Hoke Smith',
        'capacity': 25000,
        },
    
    {
        'name': 'Robertson Stadium',
        'address': '3874 Holman Street',
        'location': 'Houston, TX',
        'opened': datetime.datetime(1948, 8, 14),
        'cost': 650000,
        'architect': 'Harry D. Payne',
        'capacity': 32000,
        },
    
    {
        'name': 'BBVA Compass Stadium',
        'address': 'East End',
        'location': 'Houston, TX',
        'cost': 95000000,
        'architect': 'Populous',
        'capacity': 22000,
        },
    
    {
        'name': 'Cowboys Stadium',
        'address': '1 Legends Way',
        'location': 'Arlington, TX',
        'opened': datetime.datetime(2009, 5, 27),
        'cost': 1300000000,
        'architect': 'HKS, Inc.',
        'capacity': 80000,
        },
    
    {
        'name': 'Reliant Stadium',
        'address': 'One Reliant Park',
        'location': 'Houston, TX',
        'opened': datetime.datetime(2002, 8, 24),
        'cost': 352000000,
        'architect': 'HOK Sport',
        'capacity': 71054,
        },
    
    
    {
        'name': 'Texas Stadium',
        'address': '2401 East Airport Freeway',
        'location': 'Irving, TX',
        'opened': datetime.datetime(1971, 9, 17),
        'closed': datetime.datetime(2008, 12, 20),
        'cost': 35000000,
        'architect': 'A. Warren Morey',
        'capacity': 41922,
        },
    
    
    {
        'name': 'Alamodome',
        'address': '100 Montana Street',
        'location': 'San Antonio, TX',
        'opened': datetime.datetime(1990, 11, 5),
        'cost': 186000000,
        'architect': 'Populous',
        'capacity': 65000,
        },
    
    {
        'name': 'Astrodome',
        'address': '8400 Kirby Drive',
        'location': 'Houston, TX',
        'opened': datetime.datetime(1965, 4, 9),
        'cost': 35000000,
        'architect': 'Hermon Lloyd & W.B. Morgan',
        'capacity': 62439,
        },
    
    {
        'address': '10000 Hillcrest',
        'name': 'Franklin Stadium',
        'location': 'Dallas, TX',
        'opened': 1954,
        'capacity': 8500,
        },
    {
        'name': 'Ownby Stadium',
        'address': '5800 Ownby Dr',
        'location': 'Dallas, TX',
        'opened': 1926,
        'closed': 1988,
        'capacity': 23783,
        
        },
    
    
    
    {
        'name': 'Alamo Stadium',
        'address': '110 Tuleta Dr',
        'location': 'San Antonio, TX',
        'opened': 1940,
        'cost': 500000,
        'architect': 'Phelps & Dewees & Simmons',
        'capacity': 23000,
        },
    
    
    {
        'name': 'Old Panther Field',
        'location': 'Duncanville, TX',
        },
    {
        'name': 'Delmar Stadium',
        'location': 'Houston, TX',
        },
    {
        'name': 'Oak Cliff Baseball Grounds',
        'location': 'Dallas, TX',
        },
    
    {
        'name': 'SISD Student Activities Complex',
        'location': 'El Paso, TX',
        'opened': 2000,
        'capacity': 11000,
        'cost': 9200000,
        },
    
    
    {
        'name': 'Patriot Stadium',
        'location': 'El Paso, TX',
        'opened': 2005,
        'capacity': 3000,
        'cost': 7200000,
        },
    
    {
        'name': 'House Park',
        'location': 'Austin, TX',
        'opened': 1939,
        'capacity': 6500,
        },
    {
        'name': 'Nelson Field',
        'location': 'Austin, TX',
        },
    
    {
        'name': 'Dudley Field',
        'location': 'El Paso, TX',
        'opened': 1924,
        'closed': datetime.datetime(2005, 11, 5),
        },
    
    {
        'name': 'Texas A&M International University Soccer Complex',
        'location': 'Laredo, TX',
        },
    
    {
        'name': 'Richland Stadium',
        'location': 'Dallas, TX',
        },
    
    {
        'name': 'Cotton Bowl',
        'address': '1300 Robert B. Cullum Boulevard',
        'location': 'Dallas, TX',
        'capacity': 92100,
        'opened': 1930,
        'cost': 328200,
        },
    
    
    {
        'name': 'Dragon Stadium',
        'address': '1085 S Kimball Ave',
        'location': 'Southlake, TX',
        'capacity': 11000,
        'opened': 2001,
        'cost': 15000000,
        },
    
    {
        'name': 'FC Dallas Stadium',
        'address': '9200 World Cup Way, Ste 202',
        'location': 'Frisco, TX',
        'capacity': 20500,
        'cost': 80000000,
        'opened': datetime.datetime(2005, 8, 6),
        'length': 107,
        'width': 68,
        },
    
    ]
