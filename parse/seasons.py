

import os

from soccerdata.settings import ROOT_DIR

SEASON_DIR = os.path.join(ROOT_DIR, 'soccerdata/data/seasons')

SEASONS = [

    #'asl',
    'nasl',
    'mls',

    'mexico',

    'australia',
    'japan',
    'china',

    'argentina',
    'uruguay',
    'chile',

    'nasl2',
    ]


def load_seasons():
    p = os.path.join(ROOT_DIR, 'soccerdata/data/seasons/all')

    seasons = []
    for order, line in enumerate(open(p), start=1):
        if line.startswith('*') or not line.strip():
            continue

        sx = line.split(',')
        for order2, e in enumerate(sx, start=1):
            seasons.append({
                    #'competition': competition,
                    #'season': e,
                    'name': e.strip(),
                    'order': order,
                    'order2': order2,
                    })             

    return seasons
            


def load_seasons_old():
    l = []
    for fn in SEASONS:
        p = os.path.join(SEASON_DIR, fn)
        l.extend(process_file(p))

    return l





def process_file(p):
    f = open(p)


    seasons = []
    competition = None
    order = 0

    for line in f:
        line = line.strip()

        if line.startswith('Competition:'):
            competition = line.split('Competition:')[1]
            order = 0

        else:
            if line:
                seasons.append({
                        'competition': competition,
                        'season': line,
                        'order': order,
                        }) 
            order += 1

    return seasons
            
            
