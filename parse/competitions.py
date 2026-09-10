
import os
from metadata.settings import ROOT_DIR

COMPETITIONS = os.path.join(ROOT_DIR, 'metadata/data/competitions/definitions')
RELATIONSHIPS = os.path.join(ROOT_DIR, 'metadata/data/competitions/relationships')
ACTIVE = os.path.join(ROOT_DIR, 'metadata/data/competitions/active')


def load_active():
    with open(ACTIVE) as f:
        return set(line.strip() for line in f if line.strip() and not line.startswith('*'))

def load_competitions():

    def helper(line):
        fields = [e.strip() for e in line.split(';')]

        try:
            name, abbreviation, code, international, ctype, level, scope, area = fields
        except:
            print(line)

        ib =  (international.strip() == 'international')

        if level == '':
            level = None
        else:
            level = int(level)

        return {
            'name': name,
            'abbreviation': abbreviation,
            'code': code,
            'international': ib,
            'ctype': ctype,
            'level': level,
            'scope': scope,
            'area': area
            }
    

    p = os.path.join(COMPETITIONS)
    f = open(p)
    competitions = [helper(line.strip()) for line in f if line.strip() and not line.startswith('*')]

    active = load_active()
    unknown = active - set(c['name'] for c in competitions)
    if unknown:
        raise ValueError("active competitions not in definitions: %s" % sorted(unknown))
    for c in competitions:
        c['active'] = c['name'] in active

    return competitions



def load_competition_relations():

    def parse(line):
        before, after = [e.strip() for e in line.split(";")]
        return {
            'before': before,
            'after': after,
            }


    p = os.path.join(RELATIONSHIPS)
    f = open(p)
    return [parse(line.strip()) for line in f if line.strip() and not line.startswith('*')]

