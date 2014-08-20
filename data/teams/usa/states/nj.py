#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

import datetime

l = [


    {
        'name': 'Hoboken Germans',
        'city': 'Hoboken, NJ',
        },
    

    # early

    {
        'name': 'Americus AA',
        'city': 'West Hoboken, NJ',
        },


    # ASL

    {
        'name': 'Jersey City (ASL)',
        'city': 'Jersey City, NJ',
        },


    {
        'name': 'Paterson Almas',
        'city': 'Paterson, NJ',
        },

    {
        'name': 'Paterson Thistles',
        'city': 'Paterson, NJ',
        },

    {
        'name': 'Newarks',
        'city': 'Newark, NJ',
        },

    {
        'name': 'Newark Ironsides',
        'city': 'Newark, NJ',
        },

    {
        'name': 'Newark Hearts',
        'city': 'Newark, NJ',
        },


    {
        'name': 'Newark Ukrainians',
        'city': 'Newark, NJ',
        },

    {
        'name': 'Kearny AC',
        'city': 'Kearny, NJ',
        },



    {
        'name': 'Paterson Rangers',
        'city': 'Paterson, NJ',
        },



    {
        'name': 'Kearny Federal Ship',
        'city': 'Kearny, NJ',
        },

    {
        'name': 'Kearny Athletics',
        'city': 'Kearny, NJ',
        },

    {
        'name': 'Jersey City FC',
        'city': 'Jersey City, NJ',
        },


    {
        'name': 'New Brunswick Hungarians',
        'city': 'New Brunswick, NJ',
        },

    {
        'name': 'New Brunswick Brigade',
        'city': 'New Brunswick, NJ',
        # http://www.soccertimes.com/directory/usisl/premier/brigade.htm
        },

    {
        'name': 'NJ-LUSO Parma',
        'city': 'Denville, NJ',
        'founded': 2007,
        # http://www.soccertimes.com/directory/usisl/premier/brigade.htm
        },

    {
        'name': 'Liederkranz Trenton',
        'city': 'Trenton, NJ',
        'founded': 1930,
        # currently German American Kickers SC http://gakickers.webs.com/gakhistory.htm
        },

    {
        'name': 'Jersey City Almas',
        'city': 'Paterson, NJ',
        },


    {
        'name': 'Jersey City Liberties',
        'city': 'Jersey City, NJ',
        },

    {
        'name': 'Princeton Theological Seminary',
        'city': 'Princeton, NJ',
        },

    {
        'name': 'Princeton Cliosophic Hall',
        'city': 'Princeton, NJ',
        },

    {
        'name': 'Princeton Whig Hall',
        'city': 'Princeton, NJ',
        },

    {
        'name': 'Trenton Butler Street',
        'city': 'Trenton, NJ',
        },

    {
        'name': 'Trenton Rovers',
        'city': 'Trenton, NJ',
        },

    {
        'name': 'Trenton Potters',
        'city': 'Trenton, NJ',
        },

    {
        'name': 'Trenton Cricketeers',
        'city': 'Trenton, NJ',
        },

    {
        'name': 'Trenton Tile Rovers',
        'city': 'Trenton, NJ',
        },

    {
        'name': 'Newark Cricket Association',
        'city': 'Newark, NJ',
        },

    {
        'name': 'Pingry School',
        'city': 'Bernards, NJ',
        },

    {
        'name': 'Hoboken Union Club',
        'city': 'Hoboken, NJ',
        },


    {
        'name': 'Newark Domestics',
        'city': 'Newark, NJ',
        },

    {
        'name': 'Newark Hamilton Baseball AC',
        'city': 'Newark, NJ',
        },
    {
        'name': 'Newark Canadian Rovers',
        'city': 'Newark, NJ',
        },

    {
        'name': 'Newark Tiffany Rovers',
        'city': 'Newark, NJ',
        },

    {
        'name': 'Trenton Eagle Potters', # probably different from other potters?
        'city': 'Trenton, NJ',
        },

    {
        'name': 'Trenton Knights of Labor',
        'city': 'Trenton, NJ',
        },
    {
        'name': 'Trenton Model School',
        'city': 'Trenton, NJ',
        },

    {
        'name': 'Trenton Independents Team',
        'city': 'Trenton, NJ',
        },

    {
        'name': 'Trenton International Team',
        'city': 'Trenton, NJ',
        },

    {
        'name': 'Trenton Central High School',
        'city': 'Trenton, NJ',
        },




    {
        'name': 'Trenton Swifts',
        'city': 'Trenton, NJ',
        },

    {
        'name': 'Trenton Young Americans',
        'city': 'Trenton, NJ',
        },

    # indoor

    {
        'name': 'New Jersey Ironmen',
        'city': 'Newark, NJ',
        'founded': 2007,
        'dissolved': 2009,
        },



    {
        'name': 'Holyoke Falcos',
        'founded': 1921,
        'dissolved': 1924,
        'city': 'Holyoke, NJ',
        },
    {
        'name': 'Jersey City Celtics',
        'founded': 1921,
        'dissolved': 1922,
        'city': 'Jersey City, NJ',
        },


    # Need to separate later Paterson FC teams (there are multiple.)
    {
        'name': 'Paterson F.C.',
        'founded': 1917,
        'dissolved': 1923,
        'city': 'Paterson, NJ',
        },

    {
        'name': 'Paterson True Blues',
        'city': 'Paterson, NJ',
        },

    {
        'name': 'Haledon Thistles',
        'city': 'Haledon, NJ',
        },

    {
        'name': 'Newark Skeeters',
        'founded': 1923,
        'dissolved': 1929,
        'city': 'Newark, NJ',
        },

    {
        'name': 'Newark Americans',
        'founded': 1930,
        'dissolved': 1932,
        'city': 'Newark, NJ',
        },

    {
        'name': 'Harrison Erie F.C.',
        'founded': 1919,
        'dissolved': 1923,
        'city': 'Harrison, NJ',
        },



    {
        'name': 'New Jersey Brewers',
        #'city': 'Brooklyn, NY',
        'founded': 1972,
        'dissolved': 1975,
        },

    {
        'name': 'Sky Blue FC',
        'city': 'Piscataway, NJ',
        'founded': 2007,
        },

    {
        'name': 'Red Bull Academy',
        'city': 'Newark, NJ',
        'founded': 2005,
        },

    {
        'name': 'New Jersey Rockets',
        'city': 'East Rutherford, NJ',
        'founded': 1981,
        'dissolved': 1981,
        },

    {
        'name': 'Newark Portuguese',
        'city': 'Newark, NJ',
        },


    {
        'name': 'Polish Falcons',
        'city': 'Elizabeth, NJ',
        },

    {
        'name': 'Elizabeth SC',
        'city': 'Elizabeth, NJ',
        },

    {
        'name': 'New Jersey Eagles',
        'city': 'Paterson, NJ',
        'founded': 1987,
        'dissolved': 1990,
        },

    {
        'name': 'Erie AA',
        'city': 'Harrison, NJ',
        #'founded': 1987,
        #'dissolved': 1990,
        },

    {
        'name': 'Penn-Jersey Spirit',
        'city': 'Ewing, NJ',
        'founded': 1990,
        'dissolved': 1991,
        },


    {
        'name': 'New Jersey Rangers',
        'city': 'Denville, NJ',
        'founded': 2007,
        },

    {
        'name': 'Newark Almas',
        'city': 'Newark, NJ',
        },

    {
        'name': 'Kearney Clarks ONT',
        'founded': datetime.datetime(1883, 11, 15),
        'city': 'Kearny, NJ',
        },

    {
        'name': 'Newark Caledonians',
        'city': 'Newark, NJ',
        },

    {
        'name': 'Babcock and Wilcox',
        'city': 'Bayonne, NJ',
        },

    {
        'name': 'Centreville AC',
        'city': 'Bayonne, NJ',
        },

    {
        'name': 'West Hudson A.A.',
        'city': 'West Hudson, NJ',
        },


    {
        'name': 'Elizabeth Falcons',
        'city': 'Elizabeth, NJ',
        }


]
 
