#!/usr/local/bin/env python
# -*- coding: utf-8 -*-


# This is not being used currently.
# Will need to merge into awards if we want to bring back international award data.
# Ultimately, probably a good idea to dump this stuff into yaml.

from soccerdata.data.lists import africa, argentina, asia, australia, england, europe, fifa, france, japan, korea, mls

# Should create standardized processors for easy data entry.
# Then should dump those files into yaml.



def load():
    l = []
    for e in [
        load_africa,
        load_asia,
        load_argentina,
        load_australia,
        load_brazil,
        load_england,
        load_europe,
        load_fifa,
        load_france,
        load_japan,
        #load_korea,
        load_mls,
        load_oceania,
        load_south_america,
        load_uefa,
        load_world_cup,
        load_world_soccer,

        ]:
        lx = e()
        l.extend(lx)
    return l


def load_member(l, award):
    # The simplest of all.
    # e.g., Fifa 100.
    return [{'name': name, 'award': award} for name in l]


def load_list(l, award):
    # A list
    # e.g. ?
    r = []
    for number, name in l:
        r.append({
                'number': number, 
                'name': name,
                'award': award,
                })
    return r


def load_set(s, award, year):
    # e.g. MLS Best XI
    r = []
    for name in s:
        r.append({
                'name': name,
                'award': award,
                })
    return r

        

def load_simple(l, award):
    """Format:     (1991, 'Raymond Goethals'),"""
    def process_line(line):
        year, name = line
        return {
            'year': year,
            'name': name,
            'award': award,
            }

    return [process_line(line) for line in l]



def load_top_three(lst, award):
    # A top three.
    # technically this can be more than 3 if there's a tie.
    l = []
    for t in lst:
        year = t[0]
        winners = t[1:]
        for i, e in enumerate(winners):
            if i > 2:
                place = 3
            else:
                place = i

            l.append({
                'year': year,
                'name': e,
                'place': place,
                'award': award,
                })
    return l


def load_top_three_tuples(lst, award):
    # top three with votes.
    
    l = []
    for t in lst:
        year = t[0]
        winners = t[1:]
        for i, e in enumerate(winners):
            try:
                name, votes = e
            except:
                import pdb; pdb.set_trace()
            if i > 2:
                place = 3
            else:
                place = i

            l.append({
                    'award': award,
                    'year': year,
                    'name': name,
                    'place': place,
                    'votes': votes,
                })
    return l





def load_africa():
    l = []
    l.extend(load_caf())
    l.extend(load_africa_young())
    l.extend(load_africa_coach())
    #l.extend(load_french_african())
    #l.extend(load_africa_team())
    return l

def load_caf():
    return load_top_three(africa.caf_award, "CAF Award")

def load_french_african():
    return load_top_three_tuples(africa.french_african, "something")

def load_africa_young():
    return load_simple(africa.young_player, "Africa Young Player")

def load_africa_coach():
    return load_simple(africa.coach, "Coach")

def load_africa_team():
    return load_simple(africa.team, "Team")


def load_asia():
    l = []
    l.extend(load_asia_young())
    # Need to do asia footballer...
    return l

def load_asia_young():
    return load_simple(asia.young_player, "Asia Young Player")


def load_argentina():
    return load_argentina_footballer()


# year, names
def load_argentina_footballer():
    def format_award(name):
        return {
            'year': year,
            'name': name,
            'award': 'Footballer of the Year Argentina',
            }

    l = []
    for year, t in argentina.footballer:
        for name in t:
            l.append(format_award(name))
    return l

def load_australia():
    l = []
    return l

# Australia

def load_australia_mvp():
    return load_simple(australia.johnny_warren_medal, "Johnny Warren Medal")

def load_australia_finals_mvp():
    return load_simple(australia.joe_marston_medal)
def load_australia_finals():
    return load_simple(australia.nab_young_fooballer)
def load_australia_goalkeeper():
    return load_simple(australia.goalkeeper_of_the_year)
def load_australia_manager():
    return load_simple(australia.manager_of_the_year)


def load_brazil():
    l = []
    return l

def load_england():
    return [{"award": "Football League 100 Legends", "name": e[1]} for e in england.football_league]

def load_europe():
    #return load_top_three_tuples(europe.footballer_of_the_year, "European Footballer of the Year")
    return []


def load_fifa():
    l = []
    l.extend(load_top_three(fifa.world_player_of_the_year, "FIFA World Player of the Year"))
    l.extend(load_set(fifa.fifa_100, "Fifa 100", 2004))
    return l


def load_france():
    l = []
    l.extend(load_top_three(france.onze_de_or, "Onze de Or"))
    l.extend(load_simple(france.coach, "French Coach of the Year"))
    return l


def load_japan():
    l = []
    l.extend(load_simple(japan.mvp, "J-League MVP"))
    l.extend(load_simple(japan.rookie_of_the_year, "J-League Rookie of the Year"))
    l.extend(load_simple(japan.manager_of_the_year, "J-League Manager of the Year"))
    # Load best XI
    return l


def load_korea():
    l = []
    l.extend(load_simple(korea.mvp, "K-League MVP"))
    l.extend(load_simple(korea.rookie, "K-League Rookie of the Year"))
    return l


def load_mls():
    l = []
    l.extend(load_simple(mls.mvp, "MLS MVP"))
    l.extend(load_simple(mls.coach, "MLS Coach of the Year"))
    l.extend(load_simple(mls.defender, "MLS Defender of the Year"))
    l.extend(load_simple(mls.rookie, "MLS Rookie of the Year"))
    l.extend(load_simple(mls.newcomer, "MLS Newcomer of the Year"))
    # load best xi
    return l


def load_oceania():
    from soccerdata.data.lists import oceania
    return [{'year': l[0], 'name': l[2],'award': 'Oceania Player of the Year',} for l in oceania.oceania]


def load_south_america():
    from soccerdata.data.lists import south_america
    l = []
    l.extend(load_top_three(south_america.el_mundo, "South American Player of the Year"))
    l.extend(load_top_three(south_america.el_pais, "South American Player of the Year"))
    return l


def load_uefa():
    from soccerdata.data.lists import uefa
    l = []
    l.extend(load_top_three(uefa.footballer_of_the_year, "UEFA Footballer of the Year"))
    l.extend(load_top_three(uefa.best_goalkeeper, "UEFA Goalkeeper of the Year"))
    l.extend(load_top_three(uefa.best_defender, "UEFA Defender of the Year"))
    l.extend(load_top_three(uefa.best_midfielder, "UEFA Midfielder of the Year"))
    l.extend(load_top_three(uefa.best_forward, "UEFA Forward of the Year"))
    return l


def load_world_cup():
    from soccerdata.data.lists import world_cup
    l = []
    l.extend(load_top_three(world_cup.golden_ball, "World Cup Golden Ball"))
    l.extend(load_top_three(world_cup.young_player, "World Cup Young Player"))
    # All star team
    return l


def load_world_soccer():
    from soccerdata.data.lists import world_soccer
    l = []
    l.extend(load_simple(world_soccer.player_of_the_year, "World Soccer Player of the Year"))
    l.extend(load_simple(world_soccer.manager_of_the_year, "World Soccer Manager of the Year"))
    l.extend(load_simple(world_soccer.young_player_of_the_year, "World Soccer Young Player of the Year"))
    # team of the year
    # greatest player
    return l


if __name__ == "__main__":
    for e in load():
        print(e)
