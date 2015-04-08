#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

import datetime

l = [

    # indoor

    {
        'name': 'Hidalgo La Fiera',
        'city': 'Hidalgo, TX',
        'founded': 2012,
        },

    {
        'name': 'Texas Outlaws',
        'city': 'North Richland Hills, TX',
        'founded': 2008,
        'dissolved': 2010,
        },

    {
        'name': 'Texas Strikers',
        'city': 'Beaumont, TX',
        'founded': 2012,
        },

    # old

    {
        'name': 'Dallas Association',
        'city': 'Dallas, TX',
        },

    {
        'name': 'Wichita Fallas Fever',
        'city': 'Wichita Falls, TX',
        'founded': 1989,
        'dissolved': 1992,
        },

    {
        'name': 'Houston Dash',
        'founded': 2013,
        'city': 'Houston, TX',
        },

    {
        'name': 'Houston Summit Soccer',
        'city': 'Houston, TX',
        },

    {
        'name': 'North Texas Mid-Cities Flyers',
        'city': 'Euless, TX', # just a guess.
        },

    {
        'name': 'Texas Lightning',
        'city': 'Dallas, TX',
        },

    {
        'name': 'Houston Hurricanes',
        'city': 'Houston, TX',
        },

    {
        'name': 'Dallas YMCA',
        'city': 'Dallas, TX',
        },

    {
        'name': 'Oak Cliff Bankers',
        'city': 'Dallas, TX',
        },

    {
        'name': 'Baylor University',
        'city': 'Waco, TX',
        },

    {
        'name': 'Dallas Athletics',
        'city': 'Dallas, TX',
        },

    {
        'name': 'Dallas Nomads',
        'city': 'Dallas, TX',
        },

    {
        'name': 'Dallas Sears-Roebuck',
        'city': 'Dallas, TX',
        },

    {
        'name': 'Cleburne',
        'city': 'Cleburne, TX',
        },

    {
        'name': 'Oak Cliff High School',
        'city': 'Dallas, TX',
        },

    # division 1

    {
        'name': 'Dallas Tornado',
        'founded': 1967,
        'dissolved': 1981,
        'city': 'Dallas, TX',
        },

    {
        'name': 'Houston Stars',
        'founded': 1967,
        'dissolved': 1968,
        'city': 'Houston, TX',
        },

    {
        'name': 'Houston Hurricane',
        'founded': 1978,
        'dissolved': 1980,
        'city': 'Houston, TX',
        },

    {
        'name': 'Houston Dynamo',
        'founded': 2005,
        'city': 'Houston, TX',
        },

    {
        'name': 'FC Dallas',
        'founded': 1996,
        'city': 'Dallas, TX',
        },

    { 
        'name': 'FC Dallas Reserves',
        'city': 'Dallas, TX',
        },

    { 
        'name': 'Houston Dynamo Reserves',
        'city': 'Houston, TX',
        },

    # USL

    {
        'name': 'Laredo Heat',
        'city': 'Laredo, TX',
        'founded': 2004,
        },

    {
        'name': 'West Texas United Sockers',
        'city': 'Midland, TX',
        'founded': 2008
        },

    {
        'name': 'Austin Aztex',
        'city': 'Austin, TX',
        'founded': 1998,
        'dissolved': 2010,
        },

    {
        'name': 'El Paso Patriots',
        'city': 'El Paso, TX',
        'founded': 1989,
        },

    {
        'name': 'Austin Lone Stars',
        'city': 'Austin, TX',
        'founded': 1987,
        'dissolved': 2000,
        },

    {
        'name': 'San Antonio Scorpions',
        'city': 'San Antonio, TX',
        'founded': 2010,
        },



    # indoor

    {
        'name': 'Dallas Sidekicks',
        'founded': 1984,
        'dissolved': 2004,
        'city': 'Dallas, TX',
        },

    {
        'name': 'Houston Hotshots',
        'city': 'Houston, TX',
        'founded': 1994,
        'dissolved': 2000,
        },

    # ?

    {
        'name': 'El Paso/Juarez Gamecocks',
        'city': 'El Paso, TX',
        'founded': 1985,
        'dissolved': 1985,
        },


    {
        'name': 'ASC New Stars',
        'city': 'Houston, TX',
        'founded': 1974,
        },


    {
        'name': 'Legends FC',
        'city': 'Dallas, TX',
        'founded': 1992,
        },

    {
        'name': 'Houston Summit',
        'city': 'Houston, TX',
        'founded': 1978,
        'dissolved': 1980,
        },

    {
        'name': 'Regals FC',
        'city': 'Houston, TX',
        'founded': 1992,
        },

    {
        'name': 'NTX Rayados',
        'city': 'Dallas, TX',
        },
    {
        'name': 'Permian Basin Shooting Stars',
        'city': 'Odessa, TX',
        'founded': 1989,
        'dissolved': 1992,
        },

    {
        'name': 'San Antonio Thunder',
        'city': 'San Antonio, TX',
        'founded': 1975,
        'dissolved': 1976,
        },
    {
        'name': 'Amarillo Challengers',
        'city': 'Amarillo, TX',
        'founded': 1986,
        'dissolved': 1992,
        },
    {
        'name': 'Houston Express',
        'city': 'Houston, TX',
        'founded': 1988,
        'dissolved': 1990,
        },
    {
        'name': 'Dallas Texans',
        'city': 'Dallas, TX',
        },


    {
        'name': 'Waco Kickers',
        'city': 'Waco, TX',
        'founded': 1989,
        'dissolved': 1990,
        },

    {
        'name': 'Houston Dutch Lions',
        'city': 'Shenandoah, TX',
        'founded': 2011,
        },

    {
        'name': 'Houston Leones',
        'city': 'Houston, TX',
        'founded': 2007,
        'dissolved': 2010,
        },

    {
        'name': 'Lubbock Lazers',
        'city': 'Lubbock, TX',
        'founded': 1986,
        'dissolved': 1993,
        },

    {
        'name': 'Mesquite Kickers',
        'city': 'Mesquite, TX',
        'founded': 1994,
        'dissolved': 1997,
        },

    {
        'name': 'Border Bandits',
        'city': 'McAllen, TX',
        },


    {
        'name': 'Houston Toros',
        'city': 'Houston, TX',
        'founded': 2002,
        },

    {
        'name': 'Dallas Rockets',
        'city': 'Richardson, TX',
        'founded': 1989,
        'dissolved': 1994,
        },

    {
        'name': 'Dallas Roma FC',
        'city': 'Dallas, TX',
        'founded': 2001,
        },

    {
        'name': 'Rio Grande Valley Bravos',
        'city': 'Brownsville, TX',
        'founded': 2008,
        'dissolved': 2010,
        },

    {
        'name': 'Austin Aztex U23',
        'city': 'Austin, TX',
        'founded': 2007,
        'dissolved': 2009,
        },

    {
        'name': 'West Dallas Kings',
        'city': 'Dallas, TX', # where?
        'founded': 2001,
        'dissolved': 2001,
        },

    {
        'name': 'Rio Grande Valley Grandes',
        'city': 'Edinburg, TX',
        'founded': 2010,
        },

    {
        'name': 'DFW Tornados',
        'city': 'Dallas, TX',
        'founded': 1986,
        'dissolved': 2010,
        },


    {
        'name': 'Dallas Express',
        'city': 'Dallas, TX',
        'founded': 1984,
        'dissolved': 1992,
        },

    {
        'name': 'Houston Dynamos',
        'city': 'Houston, TX',
        'founded': 1983,
        'dissolved': 1991,
        },

    {
        'name': 'El Paso Indios USA',
        'city': 'El Paso, TX',
        'founded': 2007,
        'dissolved': 2008,
        },

    {
        'name': 'Real Madrid AC',
        'city': 'Dallas, TX',
        },

    {
        'name': 'Dallas Strikers',
        'city': 'Dallas, TX',
        },

    {
        'name': 'Wichita Falls Fever',
        'city': 'Wichita Falls, TX',
        'founded': 1989,
        'dissolved': 1992,
        },

    {
        'name': 'Austin Thunder',
        'city': 'Austin, TX',
        'founded': 1987,
        'dissolved': 1992,
        },

    {
        'name': 'Austin Lightning',
        'city': 'Austin, TX',
        'founded': 2002,
        'dissolved': 2007,
        },


    {
        'name': 'San Antonio International',
        'city': 'San Antonio, TX',
        'founded': 1987,
        'dissolved': 1990,
        },

    {
        'name': 'San Antonio Pumas',
        'city': 'San Antonio, TX',
        'founded': 1988,
        'dissolved': 1998,
        },

    {
        'name': 'San Antonio XLR8',
        'city': 'San Antonio, TX',
        'founded': 1992,
        'dissolved': 1992,
        },

    {
        'name': 'Houston Alianza',
        'city': 'Houston, TX',
        'founded': 1988,
        'dissolved': 1991,
        },


]
 
