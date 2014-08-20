# Team name mappings; e.g. FC Dallas; Dallas Burn; 1996, 2003

import datetime
import os

from soccerdata.settings import ROOT_DIR



def correct_date(s, start=True):

    if '/' in s:
        month, day, year = [int(e) for e in s.split('/')]
        d = datetime.datetime(year, month, day)
    else:
        year = int(s)
        if start:
            d = datetime.datetime(year, 1, 1)
        else:
            try:
                d = datetime.datetime(year, 12, 31)
            except:
                import pdb; pdb.set_trace()
            x = 5

    return d

    
def load():
    # Loads all files in the relevant directory.


    PATH = os.path.join(ROOT_DIR, 'soccerdata/data/mappings/team_name')
    files = os.listdir(PATH)

    l = []
    
    for e in files:
        if not e.endswith('~'): # avoid duplicate emacs files
            px = os.path.join(PATH, e)
            l.extend(process_name_map_file(px))
    return l
            
def process_name_map_file(p):
    f = open(p)
    
    nm = []
    
    for line in f:
        if line.strip() and not line.startswith("*"):
            fields = line.split(';')
            if len(fields) == 3:
                from_name, to_name, start = fields
                end = start
            elif len(fields) == 4:
                from_name, to_name, start, end = fields
            else:
                import pdb; pdb.set_trace()

            start = correct_date(start, start=True)
            end = correct_date(end, start=False)

            nm.append({
                    'from_name': from_name.strip(),
                    'to_name': to_name.strip(),
                    'start': start,
                    'end': end,
                    })
    return nm


if __name__ == "__main__":
    print(load())
