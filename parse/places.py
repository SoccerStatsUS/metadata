#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Load country and state data.
# Country names and populations (2000?)
# State and territory names, postal abbreviations, date joining union, and historical populations.

import datetime
import importlib
import os

from utils import list_paths, import_path

from soccerdata.settings import ROOT_DIR

PLACES_DIR = os.path.join(ROOT_DIR, 'soccerdata/data/places')


def load_countries():
    l = []
    p = os.path.join(PLACES_DIR, 'country_codes')
    for line in open(p):
        if line.strip():
            if not line.startswith('*'):
                try:
                    country, country_code, confederations = line.split(';')
                except:
                    import pdb; pdb.set_trace()

                if ',' in confederations:
                    confederation, subconfederation = [e.strip() for e in confederations.split(',')]
                else:
                    confederation = confederations.strip()
                    subconfederation = None

                l.append({
                        'name': country.strip(),
                        'code': country_code.strip(),
                        'confederation': confederation,
                        'subconfederation': subconfederation,
                        })

    return l



def load_country_populations():
    l = []
    p = os.path.join(PLACES_DIR, 'countries')
    for line in open(p):
        if line.strip():
            country, population = line.split(';')
            l.append({
                    'name': country.strip(),
                    'population': int(population)
                    })

    return l
        

def load_states():
    l = []
    p = os.path.join(PLACES_DIR, 'states')
    for line in open(p):
        if line.strip():

            fields = line.split(',')

            if len(fields) == 3:
                name, abbreviation, country = fields
                d = None

            elif len(fields)== 4:
                name, abbreviation, country, joined = fields
                month, day, year = [int(e) for e in joined.split('/')]

                d = datetime.datetime(year, month, day)

            else:
                import pdb; pdb.set_trace()
            
            l.append({
                    'name': name.strip(),
                    'country': country.strip(),
                    'abbreviation': abbreviation.strip(),
                    'joined': d,
                    })

    return l


def load_state_populations():
    l = []
    p = os.path.join(PLACES_DIR, 'state_populations_by_year')
    for line in open(p):
        if line.strip():
            abbreviation, year, population = line.split(';')
            l.append({
                    'abbreviation': abbreviation.strip(),
                    'year': int(year),
                    'population': int(population)
                    })

    return l
    



def load_stadiums():
    print("Loading stadiums.")
    p = os.path.join(ROOT_DIR, 'soccerdata/data/places/stadiums')
    pys = [e for e in list_paths(p) if e.endswith('.py')]
    l = []

    # What is this?
    for py in pys:
        if not py.startswith('_'):
            #tail = py.replace('/home/chris/www/', '').replace('.py', '').replace('/', '.')
            tail = py.replace(ROOT_DIR, '').replace('.py', '').replace('/', '.')
            l.extend(import_path(tail).l)

    regions = [e for e in os.listdir(p) if '.' not in e]

    final = []

    # Do this in normalize?
    for e in l:
        d = stadium_defaults.copy()
        d.update(e)
        final.append(d)

    return final

        
stadium_defaults = {
    'denomination': 'dollars',
    'measure': 'meters',
    'closed': None,
    'year_closed': None,
    'opened': None,
    'year_opened': None,
    'architect': None,
    'capacity': None,
    'location': '',
    'address': '',
    'cost': None,
}

