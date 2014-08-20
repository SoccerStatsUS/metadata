#!/usr/bin/env python


# Clean up the drafts so that we can basically remove this. This is really unnecessary.
# Export to yaml and destroy.


import datetime
import os
import re

from soccerdata.settings import ROOT_DIR

DRAFTS_DIR = os.path.join(ROOT_DIR, 'soccerdata/data/transactions/drafts')

DRAFTS = [

    # MLS
    'allocation', 
    'college', 
    'dispersal', 
    'expansion', 
    'inaugural',  
    'reentry', 
    'superdraft', 
    'supplemental', 
    'supplemental2' , 

    # minor

    'usl',

    # indoor

    # NASL
    'nasl', 
    ]



USMNT_DRAFTS = ['usmnt/2004', 'usmnt/2005', 'usmnt/2006', 'usmnt/2007', 'usmnt/2008', 'usmnt/2009', 'usmnt/2010', 'usmnt/2011', 'usmnt/2012'] #, 'usmnt/2013']

# This should probably be in utils.
def remove_pairs(text, start, end):
    """
    Removes pairs like (hello) or [whatever]
    """
    s = ""
    include = True
    for char in text:
        if char == start:
            include = False

        if include:
            s += char
        
        if char == end:
            include = True

    return s


def load_draft_data():

    draft_filenames = []
    draft_filenames.extend(DRAFTS)
    #draft_filenames.append(USMNT_DRAFTS)

    dp = DraftProcessor()

    for fn in draft_filenames:
        p = os.path.join(DRAFTS_DIR, fn)
        for line in open(p):
            dp.process_line(line)

    return dp


def load_drafts():
    return load_draft_data().drafts


def load_picks():
    return load_draft_data().picks
        

def process_date(s):
    month, day, year = [int(e) for e in s.split('/')]
    return datetime.datetime(year, month, day)

class DraftProcessor():
    
    def __init__(self):
        self.name = None
        self.competition = None
        self.season = None
        self.round = None
        self.pick_number = 1

        self.drafts = []
        self.picks = []


    @property
    def current_draft(self):
        return self.drafts[-1]


    def process_line(self, line):

        line = remove_pairs(line, "[", "]")

        if line.startswith('*'):
            return


        if line.startswith("Round:"):
            return

        if line.startswith("Draft:"):
            self.name = line.replace("Draft:", '').strip()

        elif line.startswith("Competition"):
            self.competition = line.replace("Competition:", '').strip()
            if self.competition == "None":
                self.competition = None


        elif line.startswith("Season"):
            self.season = line.replace("Season:", '').strip()
            self.pick_number = 1
            self.drafts.append({
                    'name': self.name,
                    'season': self.season,
                    'competition': self.competition,
                    })

        elif line.startswith("Date:"):
            s = line.replace("Date:", '')
            fields = s.split(',')

            fields = [e.strip() for e in fields]

            if len(fields) == 2:
                start, end = [process_date(e) for e in fields]
                
            elif len(fields) == 1:
                start = process_date(fields[0])
                end = start

            self.current_draft['start'] = start
            self.current_draft['end'] = end

        elif line.strip():
            fields = [e.strip() for e in line.split(';')]

            # Remove leading #'s if possible (we do them ourselves)
            # e.g. 12; MetroStars; Eddie Gaven; M -> MetroStars; Eddie Gaven; M

            try:
                int(fields[0])
                fields = fields[1:]
            except:
                pass

            if len(fields) == 2:
                team, text = fields
                position = former_team = None

            elif len(fields) == 3:
                team, text, position = fields
                former_team = None

            elif len(fields) == 4:
                team, text, position, former_team = fields

            else:
                import pdb; pdb.set_trace()
                
            if position and len(position) > 5:
                import pdb; pdb.set_trace()

            self.picks.append({
                    'team': team,
                    'text': text,
                    'position': position,
                    'former_team': former_team,
                    'number': self.pick_number,
                    'draft': self.current_draft['name'],
                    'season': self.current_draft['season'],
                    'competition': self.competition,
                    })

            self.pick_number += 1


if __name__ == "__main__":
    print(load_drafts())
    
