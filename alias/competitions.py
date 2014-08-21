#!/usr/local/bin/env python
# -*- coding: utf-8 -*-


aliases = {}

full_alias = {

    'NCAA Division I Men\'s Soccer Championship': 'NCAA Division I',
    
    'Copa Rio de Janeiro': 'Copa Rio', # not sure?

    'Tweede Klasse': 'Belgian Second Division',
    'Eindronde': 'Belgian Third Division',



    'FDLY': 'Friendly',

    'Championnat Féminin National, Division 1': 'Championnat Féminin',
    'Championnat Féminin National': 'Championnat Féminin',
    'Championnat Feminin': 'Championnat Féminin',

    'Women\'s Premier League': 'FA Women\'s Premier League',

    'Haiti Tournament?': 'Haiti Tournament',
    'Haiti ?': 'Haiti Tournament',

    'Austrian Football Bundesliga': 'Austrian Bundesliga',

    'Panama Liga Profesional de Fútbol': 'Liga Panameña de Fútbol',
    'Primera División de Nicaragua': 'Nicaraguan Primera División',

    'Juegos Panamericanos Femenil': 'Women\'s Panamerican Games',
    'Preolímpico CONCACAF': 'Olympic Games qualification (CONCACAF)',
    'Preolímpico Femenil CONCACAF': 'Women\'s Olympic Games qualification (CONCACAF)',

    'CONCACAF Championship Qualifying': 'CONCACAF Championship qualification',

    'Supercopa': 'Supercopa de España',

    'Carling Cup': 'Football League Cup',
    'Dutch Cup': 'KNVB Cup',

    'Copa Mustang': 'Categoría Primera A',


    'Juegos Olímpicos Femenil': 'Olympic Games Women',

    'DFB Pokal': 'DFB-Pokal',

    'Bundesliga': '1. Bundesliga',
    '1. Bundesliga': '1. Bundesliga',

    'Liga de Ascenso': 'Ascenso MX',

    'Europa League': 'UEFA Europa League',

    'USOC': 'U.S. Open Cup',
    'US Open Cup': 'U.S. Open Cup',

    'Copa Mundial': 'FIFA World Cup',

    'Copa Mundial Femenil': 'FIFA Women\'s World Cup',
    'Copa Mundial Sub-20 Femenil': 'FIFA U-20 Women\'s World Cup',
    'Copa Mundial Sub-17 Femenil': 'FIFA U-17 Women\'s World Cup',

    'MLS': 'Major League Soccer',

    #'Amistosos': 'Friendly',
    'Amistosos': 'International Friendly',



    'Copa Mundial Sub-20': 'FIFA U-20 World Cup',
    'Copa Mundial Sub-17': 'FIFA U-17 World Cup',

    'Juegos Panamericanos': 'Pan American Games',

    'Eurocopa': 'UEFA European Championship',

    'Eliminatorias CONCACAF': 'FIFA World Cup qualification (CONCACAF)',
    'Eliminatorias CONMEBOL': 'FIFA World Cup qualification (CONMEBOL)',
    'Eliminatorias UEFA': 'FIFA World Cup qualification (UEFA)',
    'Eliminatorias OFC': 'FIFA World Cup qualification (OFC)',
    'Eliminatorias CAF': 'FIFA World Cup qualification (CAF)',
    'Eliminatorias AFC': 'FIFA World Cup qualification (AFC)',

    'FIFA World Cup Qualifying (CONCACAF)': 'FIFA World Cup qualification (CONCACAF)',
    'FIFA World Cup Qualification (CONCACAF)': 'FIFA World Cup qualification (CONCACAF)',

    'CONCACAF Men\'s Olympic Qualifying Tournament': 'Olympic Games qualification (CONCACAF)',
    'FIFA World Cup Qualification': 'FIFA World Cup qualification',


    'Copa Confederaciones': 'FIFA Confederations Cup',
    'Zon Sagres': 'Primeira Liga',


    'Copa de Oro': 'Gold Cup',

    'Primera División Mexicana': 'Liga MX',


    'Superliga': 'North American SuperLiga',

    'Champions League': 'UEFA Champions League',
    'European Champions Cup': 'UEFA Champions League',

    'La Liga Española': 'La Liga',

    'Russian Football Premier League': 'Russian Premier League',

    'Rio de Janeiro Championship': 'Campeonato Carioca',
    'Campeonato da Cidade de Belo Horizonte': 'Belo Horizonte City Championship',
    'Belo Horizonte City Championship': 'Campeonato Mineiro',



    'NCAA Division I Men\'s Soccer Championship': 'NCAA Division I',
    'NCAA Division II Men\'s Soccer Championship': 'NCAA Division II',

    '1.Bundesliga': '1. Bundesliga',

    'Rio Branco Cup': 'Copa Rio Branco',

    'Interliga': 'InterLiga',
    'La Ligue': 'Ligue 1',

    'K-League': 'K League',

    'FIFA World Youth Championship': 'FIFA U-20 World Cup',


    'Costa Rican Primera División': 'Primera División de Costa Rica',
    
    'Mundial de Clubes': 'FIFA Club World Cup',
    'Club World Cup': 'FIFA Club World Cup',

    'Super Lig': 'Süper Lig',
    'Superlig': 'Süper Lig',

    # Once competition mapping is implemented.

    'CCC': 'CONCACAF Champions\' Cup',
    'Liga de Campeones CONCACAF': 'CONCACAF Champions League',
    'Copa de Campeones CONCACAF': 'CONCACAF Champions League',
    #'CONCACAF Champions\' Cup': 'CONCACAF Champions League',

    'Copa Fraternidad Centroamericana': 'Copa Interclubes UNCAF',
    'Torneo Grandes de Centroamerica': 'Copa Interclubes UNCAF',
    'UNCAF Club Championship': 'Copa Interclubes UNCAF',

    'Copa Interamericana': 'Interamerican Cup',
    'Copa Intercontinental': 'Intercontinental Cup',

    'Liga Argentina de Football': 'Argentine Primera División',
    'Primera División Argentina': 'Argentine Primera División',

    'Brasileirao': 'Brasileirão',
    'Campeonato Brasileiro Série A': 'Brasileirão',
    

    'Chilean Primera Division': 'Chilean Primera División', 
    'Uruguayan Primera Division': 'Uruguayan Primera División',

    'Merconorte Cup': 'Copa Merconorte',

    'Duvalier Cup': 'Coupe Duvalier',
    'Newton Cup': 'Copa Newton',
    'President R.S. Pena Cup': 'Copa Roque Saenz Pena',
    'Juan Pinto Duran Cup': 'Copa Pinto Duran',
    'Argentine Honour Cup': 'Copa Premio Honor Argentino',

    'Uruguayan Honour Cup': 'Copa Premio Honor Uruguayo',

    'CONCACAF Nations Cup': 'CONCACAF Championship',

    'Confederations Cup': 'FIFA Confederations Cup',
    'King Fahd Cup': 'FIFA Confederations Cup',

    'Panamerican Games': 'Pan American Games',
    'Panamerican Games Qualifying': 'Pan American Games Qualifying',

    'South American Championship': 'Copa America',
    'Copa América': 'Copa America',
    #'Copa America': 'Copa América',

    'Copa Caribe': 'Caribbean Cup',
    'Copa Caribe Qualifying': 'Caribbean Cup Qualifying',

    'UNCAF Cup': 'Copa Centroamericana',
    'UNCAF Nations Cup': 'Copa Centroamericana',



    'United Soccer League': 'United Soccer League (1984-1985)',

    'Western Soccer Alliance': 'Western Soccer League',
    'Western Soccer Alliance Playoffs': 'Western Soccer League Playoffs',


    'Southwest Independent Soccer League (indoor)': 'United States Interregional Soccer League (indoor)',
    'Southwest Independent Soccer League': 'United States Interregional Soccer League',

    'US Cup': 'U.S. Cup',
    'USISL Premier League': 'USL Premier Developmental League',

    'USISL Professional League': 'USL Second Division',
    'USL Pro': 'USL Second Division',

    'A-League': 'USL First Division',
    'USL Division 1': 'USL First Division',



    'Friendly International': 'International Friendly',

    'Unofficial Friendly': 'Friendly',

    'Recopa CONCACAF': 'CONCACAF Cup Winners Cup',
    'CONCACAF Champions Cup': 'CONCACAF Champions\' Cup',

    # Indoor

    'Southwest Indoor Soccer League': 'United States Interregional Soccer League (indoor)',

    'Premier Soccer Alliance': 'World Indoor Soccer League',

    'American Indoor Soccer Association': 'National Professional Soccer League (indoor)',

    'National Indoor Soccer League': 'Major Indoor Soccer League (2008-2014)',




    'World Cup': 'FIFA World Cup',



    'Olympic Games Qualifying': 'Olympic Games qualification',


    # Just fix...
    'Black Stars': 'Tournoi Black Stars',
    '3 Nations Cup': '3 Nations Tournament',
    'Mexico Cup': 'Mexico City Cup',
    'UNCAF': 'Copa Centroamericana',


}

aliases.update(full_alias)

# Don't want to completely delete these.
partial_alias = {

    'Domestic Tour': 'Friendly',
    'International Tour': 'Friendly',

    'Parmalat Cup': 'Friendly',

    'Desert Diamond Cup': 'Friendly',
    'Chicago Sister Cities International Cup': 'Friendly',

    'U.S. Cup': 'International Friendly',

    'Le Championnat': 'Ligue 1',
    'Calcio': 'Serie A',

    'Bicentennial Cup': 'Friendly',
    'Carlsberg Cup': 'Friendly',
    'Carolina Challenge Cup': 'Friendly',
    'Dynamo Charities Cup': 'Friendly',
    'Europac International': 'Friendly',
    'Spring Cup Matches': 'Friendly',
    'Sunshine International': 'Friendly',
    'Toronto International': 'Friendly',
    'Tournament of Champions': 'Friendly',
    'Trans-Atlantic Challenge Cup': 'Friendly',

    'Hurricane Mitch Benefit': 'Friendly',

    'Amistad Cup': 'International Friendly',

    'International Cup': 'International Friendly',
    'Joe Robbie Cup': 'International Friendly',
    'Kirin Cup': 'International Friendly',
    'Los Angeles Soccer Tournament': 'Friendly',
    'Mexico City Tournament': 'International Friendly',
    'Miami Cup': 'International Friendly',
    'North American Nations Cup': 'International Friendly',
    'Presidents Cup': 'International Friendly',
    'Trinidad Tournament': 'International Friendly',
    'Orange Bowl Cup': 'International Friendly',
    'Mexico City Cup': 'International Friendly',
    'Marlboro Cup': 'International Friendly',
    'Los Angeles Friendship Cup': 'International Friendly',

    'International Friendly Tournament': 'International Friendly',



    }

aliases.update(partial_alias)


def get_competition(s):
    if s is None:
        return None
    
    s = s.strip()
    return aliases.get(s, s)
