#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

# For processing general format score/lineup data.

# These look something like
# 3/29/2008; FC Dallas; 3-1 (aet); Chivas Guadalajara; Laredo, TX; Alex Prus; 130000
# Ruben Luna 3, Ruben Luna 10, Hugo Sanchez 92; Chicharito 19
# FC Dallas: Matt Jordan, Chris Gbandi, Clarence Goodson, George John, Zach Loyd, Brek Shea, Oscar Pareja, Leonel Alvarez, Ronnie O'Brien, Jason Kreis, Carlos Ruiz

# Need to add in home_team


import datetime
import os
import re

from utils import get_id


from soccerdata.settings import ROOT_DIR
       
def process_copa_files():
    directory = os.path.join(ROOT_DIR, 'international-data/games/confederation/conmebol/copa_america')
    filenames = [str(e) for e in [1916, 1917, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1929, 1935, 1937, 1939, 1941, 
                 1942, 1945, 1946, 1947, 1949, 1953, 1955, 1956, 1957, '1959.1', '1959.2', 1963, 1967, 1975, 1979, 1983, 1987,
                 1989, 1991, 1993, 1995, 1997, 1999, 2001, 2004]]

    games = []
    goals = []
    misconduct = []
    appearances = []
    for fn in filenames:
        print(fn)
        gmx, glx, mcx, apx = process_copa_file(fn)
        games.extend(gmx)
        goals.extend(glx)
        misconduct.extend(mcx)
        appearances.extend(apx)
        
    return (games, goals, misconduct, appearances)
        

def process_copa_file(fn):
    p = os.path.join(ROOT_DIR, 'international-data/games/confederation/conmebol/copa_america', fn)
    return process_file(p)

def process_file(p):
    f = open(p)
    return process_lines(f)

def process_string(s):
    # Convenience method for testing.
    lines = s.split('\n')
    return process_lines(lines)

def process_lines(lines):
    gp = GeneralProcessor()
    for line in lines:
        gp.process_line(line)

    return (gp.games, gp.goals, gp.misconduct, gp.appearances)
        

def process_name(s):
    """Clean up a player name. Remove possible leading numbers.
    e.g. '18-Tim Howard ' -> 'Tim Howard'"""
    s = s.strip()
    m = re.match("(\d+-)?(.*)", s)
    if m:
        return m.groups()[1].strip()
    else:
        return s


class GeneralProcessor(object):
    """
    An object to feed lines of text to.
    Retains a basic memory
    """

    def __init__(self):
        self.competition = None
        self.season = None
        self.country = None

        self.sources = []

        self.current_game = None

        self.block = []

        self.games = []
        self.goals = []
        self.misconduct = []
        self.appearances = []

        self.previous_score = None



    def process_line(self, line):
        line = line.strip()

        if line.startswith('BlockSource:'):
            source = line.split("BlockSource:")[1].strip()
            self.sources = [source]
            return

        # Set the competition.
        if line.startswith("Competition:"):
            self.competition = line.split("Competition:")[1].strip()
            return

        if line.startswith("Season:"):
            self.season = line.split("Season:")[1].strip()
            return

        if line.startswith("Country:"):
            self.country = line.split("Country:")[1].strip()
            return

        # Set the round.
        if line.startswith("Round"):
            return

        # Set the round.
        if line.startswith("Group"):
            return

        if line.startswith('*'):
            return

        if line.startswith('booked'):
            return


        if not line:
            self.process_block()
        else:
            self.block.append(line)


    def process_block(self):
        block, self.block = self.block, []
        self.previous_score = (0,0)

        if block:
            try:
                date, city, location = self.process_date_location(block[0])
            except:
                import pdb; pdb.set_trace()
                print(block[0])

            team1, team2, team1_score, team2_score = self.process_score(block[1])
            attendance, referee, linesmen = self.process_attendance_ref(block[2])
            
            g = {
                'gid': get_id(),
                'competition': self.competition,
                'season': self.season,
                'date': date,

                'team1': team1,
                'team2': team2,
                'team1_score': team1_score,
                'team2_score': team2_score,
                #'team1_result': team1_result,
                #'team2_result': team2_result,
                #'home_team': home_team,
                #'neutral': neutral,

                'location': location,
                'referee': referee,
                #'linesmen': linesmen,
                'attendance': attendance,
                'minigame': False,
                'forfeit': False,
                'sources': self.sources[:],
                }
            self.current_game = g
            self.games.append(g)

            self.appearances.extend(self.process_lineup(block[3]))
            self.appearances.extend(self.process_lineup(block[4]))

        if len(block) > 5:
            self.process_remaining_lines(block[5:])


    def process_date_location(self, line):
        date_string, location = line.split(" ", 1)
        day, month, year = [int(e) for e in date_string.split(".")]
        if year < 10:
            year += 2000
        else:
            year += 1900
            
        d = datetime.datetime(year, month, day)
        city, home_team = location.split(",")
        if self.country:
            l = "%s, %s" % (city, self.country)
        else:
            l = city


        return d, city, l
        

    def process_remaining_lines(self, block):
        if block[0].startswith("NOTE"):
            self.process_note(block[0])

        elif block[0].startswith("sent off"):
            return

        elif block[0].startswith("GOALS"):
            self.process_goals_alternate(block[0])


        else:
            try:
                self.process_goals(block[0])
            except:
                import pdb; pdb.set_trace()



    def process_note(self, line):
        return


        
    def process_score(self, line):
        match = re.match("(\w+) ?- ?(\w+) (\d+):(\d+).*", line)
        if not match:
            import pdb; pdb.set_trace()
        t1, t2, t1s, t2s = match.groups()
        t1s, t2s = int(t1s), int(t2s)
        return t1, t2, t1s, t2s
        

    def process_attendance_ref(self, line):
        attendance, referee_string = line.split(' ', 1)
        attendance = attendance.replace('(', '').replace(')', '').replace(',', '')

        if attendance:
            attendance = int(attendance)
        else:
            attendance = None

        referees = referee_string.split(',')
        referees = [e.strip()[:-3] for e in referees]
        referee = referees[0]
        linesmen = referees[1:]

        return attendance, referee, linesmen
            
    def process_lineup(self, line):

        def process_appearance(s, team, order):

            s = s.replace('(c)', '').replace('(capt)', '').replace('(capt.)', '')

            # This is somewhat wrong. This is true of game plus/minus, but not appearance plus/minus.
            # Need to handle appearance minutes...
            # This is being used for determining the results of games.
            if team == self.current_game['team1']:
                goals_for, goals_against = self.current_game['team1_score'], self.current_game['team2_score']
            elif team == self.current_game['team2']:
                goals_for, goals_against = self.current_game['team2_score'], self.current_game['team1_score']
            else:
                import pdb; pdb.set_trace()

            base = {
                'team': team,
                'competition': self.competition,
                'date': self.current_game['date'],
                'season': self.season,
                'goals_for': goals_for,
                'goals_against': goals_against,
                'order': order,
                }

            if '(' not in s:

                name = process_name(s)

                e = {
                    'name': name,
                    'on': 0,
                    'off': 90,
                    }
                e.update(base)
                return [e]

            else:
                try:
                    starter, subs = s.split("(")
                except:
                    import pdb; pdb.set_trace()

                subs = subs.replace(")", "")
                sub_items = subs.split(",")

                starter = process_name(starter)                

                l = [{ 'name': starter, 'on': 0 }]
                    
                for item in sub_items:
                    m = re.match("(\d+ )(.*)", item)
                    if m:
                        minute, sub = m.groups()
                        minute = int(minute)
                        sub = process_name(sub)
                    else:
                        #print("No minute for sub %s" % s)
                        minute = None
                        sub = process_name(sub_items[0])

                    l[-1]['off'] = minute
                    l.append({'name': sub, 'on': minute})

                l[-1]['off'] = 90
                for e in l:
                    e.update(base)

                return l


        lineups = []

        if ':' not in line:
            import pdb; pdb.set_trace()

        team, players = line.split(":")
        for order, e in enumerate(split_outside_parens(players, ',-'), start=1):
            lineups.extend(process_appearance(e, team, order))

        return lineups

    

    def process_goals(self, line):

        def process_goal(s):
            match = re.match("\s*(\d+):(\d+) (.*?)(\d+)( \w{1,2})?$", s)
            if not match:
                import pdb; pdb.set_trace()


            if len(match.groups()) == 5:
                t1s, t2s, name, minute, flag = match.groups()
            elif len(match.groups()) == 4:
                t1s, t2s, name, minute = match.groups()
            else:
                import pdb; pdb.set_trace()
                

            t1s, t2s = int(t1s), int(t2s)
            minute = int(minute)
            if t1s > self.previous_score[0] and t2s == self.previous_score[1]:
                team = self.current_game['team1']
            elif t1s == self.previous_score[0] and t2s > self.previous_score[1]:
                team = self.current_game['team2']
            else:
                import pdb; pdb.set_trace()

            self.previous_score = (t1s, t2s)

            return {
                'competition': self.competition,
                'date': self.current_game['date'],
                'season': self.season,
                'team': team,
                'goal': name.strip(),
                'minute': minute,
                'assists': [],
                }


        line = line.strip()

        goal_strings = line.split(',')
        for s in goal_strings:
            g = process_goal(s)
            self.goals.append(g)


    def process_goals_alternate(self, line):

        def process_goal_alternate(s, team):
            m = re.match("(.*?)(\d+)", s)
            if m:
                name = m.groups()[0]
                minute = int(m.groups()[1])
            else:
                name, minute = s, None

            return {
                'competition': self.competition,
                'date': self.current_game['date'],
                'season': self.season,
                'team': team,
                'goal': name.strip(),
                'minute': minute,
                'assists': [],
                }


        s = line.split("GOALS:")[1]
        team1_goals, team2_goals = s.split(';')
        for s in team1_goals.split(','):
            g = process_goal_alternate(s, self.current_game['team1'])
            self.goals.append(g)
        for s in team2_goals:
            g = process_goal_alternate(s, self.current_game['team2'])
            self.goals.append(g)
        





def split_outside_parens(s, delimiters=','):
    # Supports multiple delimiters.
    in_paren = False
    l = []
    ns = ''

    for char in s:
        if char == '(':
            in_paren = True
        if char == ')':
            in_paren = False

        if char in delimiters and not in_paren:
            l.append(ns)
            ns = ''
        else:
            ns += char

    l.append(ns)
    return l
                    

        
if __name__ == "__main__":
    #process_copa_files()
    print(process_rosters())
