import datetime
import os

from metadata.utils import pounds_to_kg, inches_to_cm
from metadata.settings import ROOT_DIR

# Scrape bios compiled by me.
# These should be turned into YAML and this code discarded.

DIR = os.path.join(ROOT_DIR, 'metadata/data/people')



def process_name(s):
    """
    All names should be in normal form. 
    None of this last name first nonsense.
    """

    if ',' not in s:
        return s

    if "Jr" in s:
        return s

    # Multiple comma names.
    mapping = {
        'Da Silva-Sarafim, Jr, Edivaldo': 'Da Silva-Sarafim Jr, Edivaldo',
        'Novas, Lomonaca, Ignacio': 'Novas, Ignacio',
        'Kato, Hajime,': 'Kato, Hajime',
        'Kolba, JR., Thoms': 'Kolba Jr., Thomas',
        'Fragoso-Gonzalez, Jr, Pedro': 'Fragoso-Gonzalez Jr, Pedro',
        }

    if s in mapping:
        s = mapping[s]

    last, first = name = s.split(',') # Assume no 2-comma names.    
    name = first + ' ' + last    
    return name.strip()


def load_other_bios():
    """
    Load all bio files.
    This is just MLS/USL bios compiled by me a long time ago.
    """

    filenames = [
        'bios.chris.csv', 
        'usl_bios.csv',
        'pdl_bios.csv', 
        ]
    
    l = []
    for fn in filenames:
        p = os.path.join(DIR, fn)
        l.extend(load_bios(p))
    return l




def process_asl_bios():
    bp = os.path.join(ROOT_DIR, 'metadata/data/people/asl_bios.csv')


    f = open(bp)

    l = []
    for line in f:

        if line.startswith("*"):
            continue

        fields = line.split(";") # 9 fields
        name, birthplace, bmonth, bday, byear, deathplace, dmonth, dday, dyear = fields

        if bmonth:
            try:
                birthdate = datetime.datetime(int(byear), int(bmonth), int(bday))
            except:
                #print(name, byear, bmonth, bday )
                birthdate = None
        else:
            birthdate = None
            
        if dmonth:
            try:
                deathdate = datetime.datetime(int(dyear), int(dmonth), int(dday))
            except:
                #print("deathdate problem")
                #print(name, dyear, dmonth, dday )
                deathdate = None

        else:
            deathdate = None

        l.append({
                'name': name,
                'birthdate': birthdate,
                'birthplace': birthplace,
                'deathdate': deathdate,
                'deathplace': deathplace,
                'source': 'American Soccer League (1921-1931)',
                })

    return l


def process_misl_bios():
    return semicolon_bios('misl', 'http://nasljerseys.com')

def process_ussf2_bios():
    return semicolon_bios('ussf2', 'Wikipedia')

def process_apsl_bios():
    return semicolon_bios('apsl', 'Wikipedia')

def process_nasl2_bios():
    return semicolon_bios('nasl2', 'Wikipedia')

def process_asl2_bios():
    return semicolon_bios('asl2', 'Wikipedia')


def process_usl1_bios():
    return semicolon_bios('usl1', 'Wikipedia')

def process_usl2_bios():
    return semicolon_bios('usl2', 'Wikipedia')

def process_pdl_bios():
    return semicolon_bios('pdl', 'Wikipedia')

def process_mls_bios():
    return semicolon_bios('mls', 'Wikipedia')  + semicolon_bios('mls2', 'Wikipedia') 

def process_world_cup_bios():
    return semicolon_bios('wc', 'Wikipedia')

def process_mls_reserve_bios():
    return semicolon_bios('mls_reserve', 'Wikipedia')

def process_usa_bios():
    return semicolon_bios('usa', 'Wikipedia')

def process_nasl_bios():
    return semicolon_bios('nasl', 'http://nasljerseys.com')

def process_asl_bios2():
    return semicolon_bios('asl', 'Wikipedia')


def semicolon_bios(fn, source):
            

    p = os.path.join(ROOT_DIR, 'metadata/data/people/')
    bp = os.path.join(p, fn)

    f = open(bp)

    l = []
    for line in f:
        if line.startswith('*'):
            continue

        if not line.strip():
            continue

        fields = [e.strip() for e in line.split(";")] # up to five fields
        empty_fields = 5 - len(fields)
        fields.extend([''] * empty_fields)
        name, birthdate, birthplace, deathdate, deathplace = fields


        if birthdate:
            if '/' in birthdate:
                fields = [int(e) for e in birthdate.split('/')]
                # e.g. 12/2008
                if len(fields) == 3:
                    m, d, y = fields
                    try:
                        bd = datetime.datetime(y, m, d)
                    except:
                        import pdb; pdb.set_trace()
                else:
                    bd = None
            else:
                try:
                    # Not using these anyway.
                    # Figure why normalizing them out isn't working.
                    bd = int(birthdate)
                    bd = None
                except:
                    import pdb; pdb.set_trace()
                    x = 5
        else:
            bd = None

        if deathdate:
            if '/' in deathdate:
                fields = [int(e) for e in deathdate.split('/')]
                # e.g. 12/2008
                if len(fields) == 3:
                    m, d, y = fields
                    try:
                        dd = datetime.datetime(y, m, d)
                    except:
                        import pdb; pdb.set_trace()
                else:
                    dd = None
            else:
                try:
                    dd = int(deathdate)
                    dd = None
                except:
                    import pdb; pdb.set_trace()
                    x = 5
        else:
            dd = None

        l.append({
                'name': name,
                'birthdate': bd,
                'birthplace': birthplace,
                'deathdate': dd,
                'deathplace': deathplace,
                'source': source,
                })

    return l

        

def load_bios(p):
    """
    Load bio data.
    """


    def process_line(line):

        if not line.strip():
            return {}

        # Remove trailing newline.
        if line.endswith("\n"):
            line = line[:-1]

        # Tab separated.
        items = line.split('\t')
        d = dict(zip(header, items))
        d['name'] = process_name(d['name'])

        if d['year'] and d['month'] and d['day']:
            # Repair inconsistent year handling.
            if int(d['year']) < 100:
                d['year'] = int(d['year']) + 1900

            d['birthdate'] = datetime.datetime(int(d['year']), int(d['month']), int(d['day']))
        else:
            d['birthdate'] = None

        if 'feet' in d:
            cm = inches_to_cm(feet=d['feet'], inches=d['inches'])
            d['height'] = cm

        if 'pounds' in d:
            d['weight'] = pounds_to_kg(d['pounds'])
            

        for e in 'year', 'month', 'day', 'feet', 'inches', 'pounds', '':
            if e in d:
                d.pop(e)

        d['source'] = os.path.split(p)[1]

        return d

    lines = open(p).read().strip().split('\n')
    header = lines[0].split('\t')
    bios = [process_line(line) for line in lines[1:]]
    return [e for e in bios if e]


def bios_yaml(p):
    # Convert bios to yaml.
    import yaml
    s = yaml.dump(load_all_bios())
    f = open(p, 'w')
    f.write(s)
    f.close()


if __name__ == "__main__":
    print(bios_yaml())
    



    

        
        
