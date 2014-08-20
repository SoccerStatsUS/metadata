import datetime
import os

from soccerdata.settings import ROOT_DIR

CONFEDERATIONS = os.path.join(ROOT_DIR, 'soccerdata/data/organizations')


def load_confederations():

    def parse(line):

        name, full_name, region, date_string = [e.strip() for e in line.split(";")]
        
        try:
            month, day, year = [int(e) for e in date_string.split('/')]
        except:
            import pdb; pdb.set_trace()


        d = datetime.datetime(year, month, day)

        return {
            'name': name,
            'full_name': full_name,
            'region': region,
            'founded': d,
            }



    p = os.path.join(CONFEDERATIONS)
    f = open(p)
    return [parse(line.strip()) for line in f if line.strip() and not line.startswith('*')]


