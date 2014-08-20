import os

from soccerdata import utils

from soccerdata.settings import ROOT_DIR

DIR = os.path.join(ROOT_DIR, 'soccerdata/data/teams')


def load():
    m = []
    for p in utils.list_paths(DIR):
        s = p.split('/data/teams/', 1)[1] # get trailing part.
        s = s.replace('/', '.')[:-3]
        s = "soccerdata.data.teams.%s" % s
        if '#' in s: 
            continue
        try:
            m.extend(utils.import_path(s).l)
        except: 
            import pdb; pdb.set_trace()
            x = 5

    return [process_item(e) for e in m]




def process_item(d):
    base = {
        'name': '',
        'abbreviation': '',
        'founded': None,
        'dissolved': None,
        'city': '',
        }
    e = base.copy()
    e.update(d)
    return e



def process_teams(team_module):
    """
    Given a dictionary, process the awards described inside.
    """
    l = []


    for td in team_module.l:
        d = base.copy()
        d.update(td)
        l.append(d)

        
    return l


def load_usa_teams():
    from soccerdata.data.teams.usa import mls, asl, nasl, ncaa, usl, indoor
    return process_teams(mls) + \
        process_teams(nasl) + \
        process_teams(asl) + \
        process_teams(ncaa) + \
        process_teams(usl) + \
        process_teams(indoor)


def load_world_teams():
    from soccerdata.data.teams.world import asia, concacaf, conmebol, uefa
    return process_teams(conmebol) + \
        process_teams(asia) + \
        process_teams(concacaf) + \
        process_teams(uefa)


#def load():
#    return load_usa_teams() + load_world_teams()


#if __name__ == "__main__":
#    print(load())
