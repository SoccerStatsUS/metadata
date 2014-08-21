# This is just a bad copy of text/games.py; should be merged.

import datetime
import os
import re

from soccerdata.settings import ROOT_DIR


def load_pdl_games():
    games = process_pdl_games_file('domestic/country/usa/leagues/d4/pdl/pdl.csv')
    games2 = process_pdl_games_file('domestic/country/usa/leagues/d4/pdl/2012')
    return games + games2


def process_string(s):
    lines = s.split('\n')
    return process_lines(lines)


def process_pdl_games_file(fn):
    p = os.path.join(ROOT_DIR, 'soccerdata/data/games', fn)
    f = open(p)
    gp = GeneralProcessor()
    for line in f:
        gp.process_line(line)

    return gp.games





class GeneralProcessor(object):
    """
    An object to feed lines of text to.
    Retains a basic memory
    """

    DATE_RE = re.compile("(\d+)/([\d\?]+)/(\d+)")
    DATE_TIME_RE = re.compile("(\d+)/(\d+)/(\d+) (\d+)z")

    def __init__(self):
        self.competition = None
        self.season = None
        self.sources = []

        self.date = None

        self.current_game = None
        self.score_type = "standard"
        self.century = None # Manage dates like 3/23/10

        self.date_style = 'month first'

        self.games = []
        self.goals = []
        self.misconduct = []
        self.appearances = []


    def process_line(self, line):
        """
        Do a lot of processing.
        """
        
        line = line.strip()

        if not line:
            return

        #if self.current_game is not None and self.current_game['date'] == datetime.datetime(2011, 10, 26):
        #    import pdb; pdb.set_trace()

        # Represents a comment.
        if line.startswith("*"):
            return
        # Set the previous game as a minigame.
        if line.startswith("Minigame"):
            try:
                self.games[-1]['minigame'] = True
                return
            except:
                import pdb; pdb.set_trace()
                x = 5

        if line.startswith("Forfeit"):
            self.games[-1]['forfeit'] = True
            return


        # Change the number of minutes.
        if line.startswith("Minutes:"):
            return

        if line.startswith("Notes:"):
            return

        if line.startswith("Date:"):
            d = line.split('Date:')[1].strip()
            month, day, year = [int(e) for e in d.split('/')]
            self.date = datetime.datetime(year, month, day)
            return


        # Set the competition.
        if line.startswith("Competition:"):
            self.competition = line.split("Competition:")[1].strip()
            return

        if line.startswith("Season:"):
            self.season = line.split("Season:")[1].strip()
            return

        # Set the round.
        if line.startswith("Round"):
            return

        # Add a source.
        if line.startswith("Source:"):
            source = line.split("Source:")[1].strip()
            self.games[-1]['sources'].append(source)
            return

        if line.startswith('BlockSource:'):
            source = line.split("BlockSource:")[1].strip()
            self.sources = [source]
            return
            

        fields = line.split(";")
            
        # I think we can knock this out.
        skip_team = False
        if ';' in line and ':' in line:
            if line.index(';') < line.index(':'):
                skip_team = True

        if ":" in line and not skip_team:
            possible_team = line.split(":")[0]
            try:
                #if self.current_game['date'] == datetime.datetime(2011, 11, 6):
                #    import pdb; pdb.set_trace()

                if possible_team in (self.current_game['team1'], self.current_game['team2']):
                    lineups = self.process_lineup(line)
                    self.appearances.extend(lineups)
                    return 

            except:
                import pdb; pdb.set_trace()

        return self.process_game_fields(fields)

        import pdb; pdb.set_trace()
        x = 5
        
    def process_game_fields(self, fields):

        team1_result = team2_result = None
        result_unknown = False
        time_string = fields[0].strip()

        if time_string.strip():
            try:
                start = int(time_string)
            except:
                import pdb; pdb.set_trace()
        else:
            start = None


        if True:
            try:
                team1, score, team2 = fields[1:4]

                score = score.lower().strip()

                if '(aet)' in score:
                    score = score.replace('(aet)', '')

                if '(asdet)' in score:
                    score = score.replace('(asdet)', '')


                # Eventually will indicate a blank score.
                # We're not prepared to handle this, so leave the function.
                if score == 'w/o':
                    print("skipping: %s" % score)
                    winner = team1
                    return

                elif score == '?':
                    team1_score = team2_score = None
                    result_unknown = True
                elif score in ('at', 'n/p', 'np'):
                    team1_score = team2_score = None
                else:
                    team1_score, team2_score = [e.strip() for e in score.split('-')]

                    if team1_score in 'wlt':
                        team1_result = team1_score
                        team1_score = None
                    else:
                        team1_score = int(team1_score)


                    if team2_score in 'wlt':
                        team2_result = team2_score
                        team2_score = None
                    else:
                        team2_score = int(team2_score)

                    winner = None
            except:
                import pdb; pdb.set_trace()

            remaining = fields[4:]

        else:
            import pdb; pdb.set_trace()

        # Attendance is always the last item.
        if remaining:
            try:
                attendance = int(remaining[-1])
                remaining = remaining[:-1]
            except ValueError:
                attendance = None
        else:
            attendance = None


        location = referee = ''

        if len(remaining) == 1:
            location = remaining[0].strip()

        elif len(remaining) == 2:
            location, referee = [e.strip() for e in remaining]

        linesmen = []
        if referee and ',' in referee:
            people = referee.split(',')
            referee = people[0].strip()
            linesmen = [e.strip() for e in people[1:]]

        if self.competition is None or self.season is None:
            import pdb; pdb.set_trace()

        
        team1 = team1.strip()
        team2 = team2.strip()
        location = location.strip()
        
        neutral = False
        home_team = None
        if location in (team1, team2):
            home_team, location = location, ''
        elif location.lower() == 'neutral':
            neutral = True

        g = {
            'competition': self.competition,
            'season': self.season,
            'date': self.date,

            'team1': team1.strip(),
            'team2': team2.strip(),
            'team1_score': team1_score,
            'team2_score': team2_score,
            'team1_result': team1_result,
            'team2_result': team2_result,
            'home_team': home_team,
            'neutral': neutral,

            'result_unknown': result_unknown,

            'location': location,
            'referee': referee,
            'linesmen': linesmen,
            'attendance': attendance,
            'minigame': False,
            'forfeit': False,
            'sources': self.sources[:],
            }

        self.current_game = g
        self.games.append(g)


        
        
if __name__ == "__main__":
    d = os.path.join(ROOT_DIR, 'www/soccerdata/data/general')
    for fn in os.listdir(d):
        p = os.path.join(d, fn)
        if os.path.isfile(p) and not fn.endswith("~"):
            print(process_general_file(fn))
    #print(process_general_file("harmarville.txt"))
    
