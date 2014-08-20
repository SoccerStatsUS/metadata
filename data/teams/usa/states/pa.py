#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

import datetime

l = [

    { 
        'name': 'Donora Steel Works',
        'city': 'Donora, PA',
        },

    # indoor
    
    { 
        'name': 'Pennsylvania Roar',
        'city': 'Reading, PA',
        'founded': 2013,
        'dissolved': 2014,
        },

    # ASL2

    { 
        'name': 'Philadelphia Nationals',
        'city': 'Philadelphia, PA',
        #'founded': 1936,
        #'dissolved': 1954,
        },

    { 
        'name': 'Philadelphia Ukrainians',
        'city': 'Philadelphia, PA',
        'founded': 1950,
        'dissolved': 1976,
        },

    # ASL

    { 
        'name': 'Bridgeport Hungaria',
        'city': 'Bridgeport, PA',
        'founded': 1930,
        'dissolved': 1930,
        },


    { 
        'name': 'Norristown Association',
        'city': 'Norristown, PA',
        },

    { 
        'name': 'Philadelphia Fever',
        'city': 'Philadelphia, PA',
        },

    { 
        'name': 'Philadelphia Independence',
        'city': 'Philadelphia, PA',
        'founded': 2009,
        'dissolved': 2012,
        },

    { 
        'name': 'Pittsburgh Spirit',
        'city': 'Pittsburgh, PA',
        },

    { 
        'name': 'Disston',
        'city': 'Philadelphia, PA',
        },

    { 
        'name': 'Widener Military Academy',
        'city': 'Chester, PA',
        },


    { 
        'name': 'Philadelphia Senecas',
        'city': 'Philadelphia, PA',
        },

    { 
        'name': 'Philadelphia Kensington Rovers',
        'city': 'Philadelphia, PA',
        },

    { 
        'name': 'Philadelphia Irish Nationalists',
        'city': 'Philadelphia, PA',
        },

    { 
        'name': 'Philadelphia South Ends',
        'city': 'Philadelphia, PA',
        },
    { 
        'name': 'Philadelphia North Ends',
        'city': 'Philadelphia, PA',
        },

    { 
        'name': 'Philadelphia Frankfords',
        'city': 'Philadelphia, PA',
        },

    { 
        'name': 'Philadelphia Manayunks',
        'city': 'Philadelphia, PA',
        },

    { 
        'name': 'Philadelphia Oxfords',
        'city': 'Philadelphia, PA',
        },

    { 
        'name': 'Philadelphia Nicetowns',
        'city': 'Philadelphia, PA',
        },

    { 
        'name': 'Philadelphia Enterprises',
        'city': 'Philadelphia, PA',
        },

    { 
        'name': 'Philadelphia North End Alexanders',
        'city': 'Philadelphia, PA',
        },

    { 
        'name': 'Philadelphia North End Astins',
        'city': 'Philadelphia, PA',
        },

    { 
        'name': 'Philadelphia Thistles',
        'city': 'Philadelphia, PA',
        },

    { 
        'name': 'Philadelphia Athletics',
        'city': 'Philadelphia, PA',
        },

    { 
        'name': 'Philadelphia Celtics',
        'city': 'Philadelphia, PA',
        },

    { 
        'name': 'Philadelphia Corinthians',
        'city': 'Philadelphia, PA',
        },

    { 
        'name': 'Philadelphia Nondescripts',
        'city': 'Philadelphia, PA',
        },

    { 
        'name': 'Philadelphia Wanderers',
        'city': 'Philadelphia, PA',
        },

    { 
        'name': 'Philadelphia Orianas',
        'city': 'Philadelphia, PA',
        },

    {

        'name': 'Chester Town Team',
        'city': 'Chester, PA',
        },

    { 
        'name': 'Philadelphia Association',
        'city': 'Philadelphia, PA',
        },

    { 
        'name': 'Philadelphia Shamrocks',
        'city': 'Philadelphia, PA',
        },

    { 
        'name': 'Pittsburgh East End Gym',
        'city': 'Pittsburgh, PA',
        },

    { 
        'name': 'Wilkes-Barre Lace Factory',
        'city': 'Wilkes-Barre, PA',
        },

    { 
        'name': 'Wilkes-Barre Oliphants',
        'city': 'Wilkes-Barre, PA',
        },

    { 
        'name': 'Wilkes-Barre Wantibes',
        'city': 'Wilkes-Barre, PA',
        },

    { 
        'name': 'Wilkes-Barre North Ends',
        'city': 'Wilkes-Barre, PA',
        },

    { 
        'name': 'Wilkes-Barre Shamrocks',
        'city': 'Wilkes-Barre, PA',
        },

    { 
        'name': 'Scranton Caledonians',
        'city': 'Scranton, PA',
        },

    { 
        'name': 'Chester Eddystones',
        'city': 'Chester, PA',
        },

    { 
        'name': 'Chester Volunteers',
        'city': 'Chester, PA',
        },

    { 
        'name': 'Lafayette College',
        'city': 'Easton, PA',
        },

    { 
        'name': 'West Chester University',
        'city': 'West Chester, PA',
        },

    { 
        'name': 'Wilkes-Barre Albions',
        'city': 'Wilkes-Barre, PA',
        },

    { 
        'name': 'Indiana Normal School',
        'city': 'Indiana, PA',
        },

    { 
        'name': 'Indiana Town Team',
        'city': 'Indiana, PA',
        },

    { 
        'name': 'Indiana FBC',
        'city': 'Indiana, PA',
        },

    # division 1

    {
        'name': 'Philadelphia Phillies',
        'founded': 1894,
        'dissolved': 1894,
        'city': 'Philadelphia, PA',
        },


    # Need to separate later Philadelphia FC's.
    {
        'name': 'Philadelphia Field Club',
        'founded': 1921,
        'dissolved': 1922,
        'city': 'Philadelphia, PA',
        },


    {
        'name': 'Bethlehem Steel',
        'founded': 1911,
        'dissolved': 1930,
        'city': 'Bethlehem, PA',
        },


    {
        'name': 'Philadelphia Atoms',
        'founded': 1973,
        'dissolved': 1976,
        'city': 'Philadelphia, PA',
        },


    {
        'name': 'Philadelphia Union',
        'founded': 2008,
        'city': 'Philadelphia, PA',
        },

    { 
        'name': 'Philadelphia Union Reserves',
        'city': 'Philadelphia, PA',
        },




    # USL

    {
        'name': 'Pittsburgh Riverhounds',
        'city': 'Pittsburgh, PA',
        'founded': 1999,
        },

    {
        'name': 'Harrisburg City Islanders',
        'city': 'Harrisburg, PA',
        'founded': 2004,
        },

    {
        'name': 'Lehigh Valley Steam',
        'city': 'Lehigh Valley, PA',
        'founded': 1999,
        'dissolved': 1999,
        },


    {
        'name': 'Hershey Wildcats',
        'city': 'Hershey, PA',
        'founded': 1997,
        'dissolved': 2001,
        },





    # indoor

    {
        'name': 'Pittsburgh Stingers',
        'founded': 1994,
        'dissolved': 1995,
        'city': 'Pittsburgh, PA',
        },

    {
        'name': 'Philadelphia Kixx',
        'city': 'Philadelphia, PA',
        'founded': 1995,
        'dissolved': 2010,
        },



    # amateurs?
    {
        'name': 'Fleisher Yarn',
        'founded': 1921, # maybe earlier.
        'dissolved': 1925,
        'city': 'Philadelphia, PA',

        },



    {
        'name': 'Beadling SC',
        'city': 'Pittsburgh, PA',
        'founded': 1898,
        },


    {
        'name': 'Philadelphia Charge',
        'city': 'Philadelphia, PA',
        'founded': 2009,
        'dissolved': 2012,
        },

    {
        'name': 'Pittsburgh Indians',
        'city': 'Pittsburgh, PA',
        },

    {
        'name': 'Philadelphia Centennials',
        'city': 'Philadelphia, PA',
        },

    {
        'name': 'Pennsylvania Stoners',
        'city': 'Allentown, PA',
        'founded': 2007,
        'dissolved': 2008,
        },

    {
        'name': 'FC Sonic Lehigh Valley',
        'city': 'Allentown, PA',
        'founded': 2009,
        },

    {
        'name': 'Phoenix SC',
        'city': 'Feasterville, PA', # Quite old?
        },

    {
        'name': 'Vereinigung Erzgebirge',
        'city': 'Warminster, PA',
        'founded': 1931,
        },

    {
        'name': 'Pittsburgh Miners',
        'city': 'Pittsburgh, PA',
        'founded': 1975,
        'dissolved': 1975,
        },



    {
        'name': 'Philadelphia Freedom',
        'city': 'Philadelphia, PA',
        'founded': 1994,
        'dissolved': 1997,
        },

    {
        'name': 'Harrisburg Heat',
        'city': 'Harrisburg, PA',
        'founded': 1991,
        'dissolved': 2003,
        },


    {
        'name': 'Hershey Impact',
        'city': 'Hershey, PA',
        'founded': 1988,
        'dissolved': 1991,
        },

    {
        'name': 'Beadling Terriers',
        'city': 'Beadling, PA',
        },

    {
        'name': 'Philadelphia Fury',
        'city': 'Philadelphia, PA',
        'founded': 1978,
        'dissolved': 1980,
        },

    {
        'name': 'Philadelphia Spartans',
        'city': 'Philadelphia, PA',
        'founded': 1967,
        'dissolved': 1968,
        },

    {
        'name': 'Pittsburgh Phantoms',
        'city': 'Pittsburgh, PA',
        'founded': 1967,
        'dissolved': 1967,
        },

    {
        'name': 'Harmarville Hurricanes',
        'city': 'Harmarville, PA',
        'founded': 1947,
        'dissolved': 1967,
        },

]
 
