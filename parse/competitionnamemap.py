# Competition name mappings; e.g. USL First Divison -> A-League

import datetime
import os

from soccerdata.settings import ROOT_DIR

p = os.path.join(ROOT_DIR, 'soccerdata/data/mappings/competition_name')

make_joint_season = lambda y: "%s-%s" % (y, y+1)


def generate_seasons(start, end):
    # Given seasons like 1927-1928, 191-1932, produce
    # [1927-1928, 1928-1929, 1930-1931, 1931-1932]
    
    l = []
    start_year = int(start.split('-')[0])
    end_year = int(end.split('-')[1])

    
    
    i = start_year
    while i < end_year:
        l.append(make_joint_season(i))
        i += 1
    
    return l
        

def load():
    return process_competition_name_map_file()
    
def process_competition_name_map_file():
    f = open(p)
    
    nm = []
    
    for line in f:
        if line.strip() and not line.startswith("*"):
            fields = line.split(';')
            if len(fields) == 3:
                from_name, to_name, season = fields
                seasons = [season]
            elif len(fields) == 4:
                from_name, to_name, start, end = fields
                
                if '-' in start:

                    if end.strip() == 'now':
                        end = make_joint_season(datetime.datetime.today().year)

                    assert '-' in end
                    seasons = generate_season(start, end)
                
                else:
                    assert '-' not in end
                    if end.strip() == 'now':
                        end = datetime.date.today().year

                    seasons = [str(e) for e in range(int(start), int(end) + 1)]
                

            else:
                import pdb; pdb.set_trace()

            nm.append({
                    'from_name': from_name.strip(),
                    'to_name': to_name.strip(),
                    'seasons': seasons,
                    })
    return nm


if __name__ == "__main__":
    print(load())
