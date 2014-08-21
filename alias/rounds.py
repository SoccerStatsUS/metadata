#!/usr/local/bin/env python
# -*- coding: utf-8 -*-


def get_round(s):
    """
    Recursive. 
    """

    s = str(s)

    s = s.strip()
    if s in rounds:
        return get_round(rounds[s])
    else:
        return s


rounds = {

    'round of 64': '/64',
    'round of 32': '/32',
    'round of 16': '/16',
    'semifinals': 'sf',
    'quarterfinals': 'qf',
    'final': 'f',
    'finals': 'f',
    'Championship Final': 'f',

    'qualifying': 'q',
    'preliminary': 'pre',
    'Promotion/Relegation Playoff': 'p/r',
    'Promotion/Relegation Playoffs': 'p/r',
    'Relegation Playoff': 'p/r',
    'Relegation Playoffs': 'p/r',

    'Group Stage': 'group',
    'Group stage': 'group',
    'Group Phase': 'group',
    'Group': 'group',
    'group': 'G',

    'repesca': 'repechaje',
    'Repechaje': 'repechaje',
    'repechaje': 'rp',

    'Superfinal ANAPROF': 'f',
    

    'Round  1': 'Round 1',
    'Round  2': 'Round 2',
    'Round  3': 'Round 3',
    'Round  4': 'Round 4',
    'Round  5': 'Round 5',
    'Round  6': 'Round 6',
    'Round  7': 'Round 7',
    'Round  8': 'Round 8',
    'Round  9': 'Round 9',

    'Round 1': '1',
    'Round 2': '2',
    'Round 3': '3',
    'Round 4': '4',
    'Round 5': '5',
    'Round 6': '6',
    'Round 7': '7',
    'Round 8': '8',
    'Round 9': '9',
    'Round 10': '10',
    'Round 11': '11',
    'Round 12': '12',
    'Round 13': '13',
    'Round 14': '14',
    'Round 15': '15',
    'Round 16': '16',
    'Round 17': '17',
    'Round 18': '18',
    'Round 19': '19',
    'Round 20': '20',
    'Round 21': '21',
    'Round 22': '22',
    'Round 23': '23',
    'Round 24': '24',
    'Round 25': '25',
    'Round 26': '26',
    'Round 27': '27',
    'Round 28': '28',
    'Round 29': '29',
    'Round 30': '30',
    'Round 31': '31',
    'Round 32': '32',
    'Round 33': '33',
    'Round 34': '34',
    'Round 35': '35',
    'Round 36': '36',
    'Round 37': '37',
    'Round 38': '38',
    'Round 39': '39',
    'Round 40': '40',
    'Round 41': '41',
    'Round 42': '42',
    'Round 43': '43',
    'Round 44': '44',

    'Bronze Medal': 'third place',
    'Bronze Medal Game': 'third place',
    'Bronze Medal Match': 'third place',

    'Third Place': 'third place',
    'Third Place Game': 'third place',
    'Third Place Match': 'third place',
    'Third Place Matches': 'third place',
    'Third Place Playoff': 'third place',
    'Third Round': 'third place',
    'Third place': 'third place',
    'third place': '3rd place',

    '3rd Place': '3rd place',
    '3rd Place Match': '3rd place',
    '3rd place': '3p',

    'Fourth Place': '4th place',
    'Playoff for Fourth Place': '4th place',
    '4th place': '4p',

    '5th Place Match': '5th place',
    '5th Place': '5th place',
    'Fifth Place': '5th place',
    '5th place': '5p',

    '8th Place': '8th place',
    '8th place': '8p',

    'Playoff Against Ninth Place ': '9th place',
    '9th place': '9p',
    
    'Qualifying': 'qualifying',
    'Qualifying Matches': 'qualifying',
    'Qualifying Playoff':  'qualifying',
    'Qualifying Round':  'qualifying',
    'Qualifying Rounds':  'qualifying',
    'Qualifying round':  'qualifying',

    'Quarter Finals': 'quarterfinals',
    'Quarter-Finals':  'quarterfinals',
    'Quarter-finals': 'quarterfinals',
    'Quarterfinal': 'quarterfinals',
    'Quarterfinals': 'quarterfinals',
    '1/8 Final': 'quarterfinals',
    '1/8 final': 'quarterfinals',


    'Regional Semifinals': 'quarterfinals',
    'Conference Semifinals': 'quarterfinals',

    'Semi Finals': 'semifinals',
    'Semi-Finals': 'semifinals',
    'Semifinal': 'semifinals',
    'Semifinal Round': 'semifinals',
    'Semifinal Stage': 'semifinals',
    'Semifinals': 'semifinals',

    'Conference Finals': 'semifinals',
    'Regional Finals': 'semifinals',
    'National Semifinals': 'semifinals',


    'Final': 'finals',
    'Final Playoff': 'finals',
    'Final Round': 'finals',
    'Final Stage': 'finals',
    'Final Tournament': 'finals',
    'Finals': 'finals',
    'Grand Final': 'finals',
    'MLS Cup': 'final',
    'Championship': 'final',

    'Knockout Round': 'knockout',
    'knockout': 'ko',

    'First Stage': '1st',
    'First Phase': '1st',
    'Regional First Round': '1st',
    'First Round': '1st',
    'First round': '1st',
    'First Rounds': '1st',
    'first': '1st',
    'First': '1st',

    'Second Stage': '1st',
    'Second Phase': '1st',
    'Second Round': '2nd',
    'Second round': '2nd',
    'Second': '2nd',

    'Third Round': '3rd',
    'Third': '3rd',

    'Fourth': '4th',
    'Fourth Round': '4th',

    'Fifth': '5th',
    'Fifth Round': '5th',

    'Sixth': '6th',
    'Sixth Round': '6th',

    'Seventh': '7th',
    'Seventh Round': '7th',

    '1st': '1',
    '2nd': '2',
    '3rd': '3',
    '4th': '4',
    '5th': '5',
    '6th': '6',
    '7th': '7',

    'Play-in': 'play-in',
    'play-in': 'pi',

    'Preliminary': 'preliminary',    
    'Preliminary Round': 'preliminary',
    'Preliminary Rounds': 'preliminary',
    'Preliminary Phase': 'preliminary',

    'First Preliminary Round': 'pre1',
    'Second Preliminary Round': 'pre2',

    'Intermediate Round': 'intermediate',
    'Intermediate': 'intermediate',
    'intermediate': 'I',

    'Fifth Place Match': '5th place',

    'Fourth Place Match': '4th place',

    'Play-Offs': 'playoffs',
    'Playoff': 'playoffs',

    'Play-in Round': 'play-in',

    'Repesca': 'repesca',
    'Triangular Final' : 'triangular final',


    'Round of 64': 'round of 64',
    
    'Round of 32': 'round of 32',

    'Round of 16': 'round of 16',
    'Round of Sixteen': 'round of 16',
    '1/16 final': 'round of 16',



    'Round of 32': 'round of 32',
    'Round of 64': 'round of 64',

    'Losers\' Round': 'lr',

}
