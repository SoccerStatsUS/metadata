import datetime
import os

from soccerdata.settings import ROOT_DIR

p = os.path.join(ROOT_DIR, 'soccerdata/data/mappings/team_stadium')


# Eliminate this duplicate? Move to utils?
def correct_date(s, start=True):

    if '/' in s:
        month, day, year = [int(e) for e in s.split('/')]
        d = datetime.datetime(year, month, day)
    else:
        try:
            year = int(s)
        except:
            import pdb; pdb.set_trace()
        if start:
            d = datetime.datetime(year, 1, 1)
        else:
            d = datetime.datetime(year, 12, 31)

    return d
    

def load():
    files = os.listdir(p)

    l = []
    
    for e in files:
        if not e.endswith('~'): # avoid duplicate emacs files
            px = os.path.join(p, e)
            l.extend(process_stadium_map_file(px))
    return l
            
def process_stadium_map_file(p):
    """
    Process a stadium map file.
    """


    f = open(p)
    
    nm = []
    
    for line in f:
        if line.strip() and not line.startswith("*"):
            fields = [e.strip() for e in line.split(',')]
            fields = [e for e in fields if e]
            if len(fields) == 3:
                team, stadium, start = fields

                # Process date at the correct time so we don't have to do this?
                #end = unicode(datetime.date.today().year)
                end = str(datetime.date.today().year)
            elif len(fields) == 4:
                team, stadium, start, end = fields
            else:
                print("Incorrect fields for stadium map: %s" % fields)
                continue


            start = correct_date(start, start=True)
            end = correct_date(end, start=False)

            nm.append({
                    'team': team,
                    'stadium': stadium.strip(),
                    'start': start,
                    'end': end,
                    })
    return nm


if __name__ == "__main__":
    print(load())
