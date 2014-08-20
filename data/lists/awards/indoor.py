#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

import datetime


# NASL

nasl = {
    'competition': 'North American Soccer League (indoor)',
    'team_data': ['Champion'],

    'Champion': [
        ('1975', 'San Jose Earthquakes'),
        ('1976', 'Tampa Bay Rowdies'),
        ('1979', 'Dallas Tornado'),
        ('1979-1980', 'Tampa Bay Rowdies'),
        ('1980-1981', 'Edmonton Drillers'),
        ('1981-1982', 'San Diego Sockers'),
        ('1983', 'Tampa Bay Rowdies'),
        ('1983-1984', 'San Diego Sockers'),
        ],

    'MVP': [
        ('1975', 'Paul Child'),
        ('1975', 'Gabbo Garvic'),
        ('1976', 'Clyde Best'),
        ('1981-1982', 'Juli Veee'),
        ('1983', 'Laurie Abrahams'), # offensive
        ('1983', 'Mehdi Cerbah'), # defensive
        ('1983-1984', 'Steve Zungul'),
        ],

    'Finals MVP': [
        ('1980-1981', 'Kai Haaskivi'),
        ('1981-1982', 'Juli Veee'), # Playoff
        ('1983-1984', 'Jean Willrich'),
        ],

    'Coach of the Year': [
        ('1983-1984', 'Eddie Firmani'),
        ],

    
}

# MISL 1-3


misl1 = {
    'competition': 'Major Indoor Soccer League (1978-1992)',
    'team_data': ['Champion'],

    'Champion': [
        ('1978-1979', 'New York Arrows'),
        ('1979-1980', 'New York Arrows'),
        ('1980-1981', 'New York Arrows'),
        ('1981-1982', 'New York Arrows'),
        ('1982-1983', 'San Diego Sockers'),
        ('1983-1984', 'Baltimore Blast'),
        ('1984-1985', 'San Diego Sockers'),
        ('1985-1986', 'San Diego Sockers'),
        ('1986-1987', 'Dallas Sidekicks'),
        ('1987-1988', 'San Diego Sockers'),
        ('1988-1989', 'San Diego Sockers'),
        ('1989-1990', 'San Diego Sockers'),
        ('1990-1991', 'San Diego Sockers'),
        ('1991-1992', 'San Diego Sockers'),
         ],

    'MVP': [
        ('1978-1979', 'Steve Zungul'),
        ('1979-1980', 'Steve Zungul'),
        ('1980-1981', 'Steve Zungul'),
        ('1981-1982', 'Steve Zungul'),
        ('1981-1982', 'Stan Terlecki'),
        ('1982-1983', 'Alan Mayer'),
        ('1983-1984', 'Stan Stamenkovic'),
        ('1984-1985', 'Steve Zungul'),
        ('1985-1986', 'Steve Zungul'),
        ('1986-1987', 'Tatu'),
        ('1987-1988', 'Erik Rasmussen'),
        ('1988-1989', 'Preki'),
        ('1989-1990', 'Tatu'),
        ('1990-1991', 'Victor Nogueira'),
        ('1991-1992', 'Victor Nogueira'),
         ],


    'Coach of the Year': [
        ('1978-1979', 'Timo Liekoski'),
        ('1979-1980', 'Len Bilous'),
        ('1979-1980', 'Pat McBride'),
        ('1980-1981', 'Don Popovic'),
        ('1981-1982', 'David Clements'),
        ('1982-1983', 'Pat McBride'),
        ('1983-1984', 'Kenny Cooper'),
        ('1984-1985', 'Peter Wall'),
        ('1985-1986', 'Gordon Jago'),
        ('1986-1987', 'David Clements'),
        ('1987-1988', 'Ron Newman'),
        ('1988-1989', 'Kenny Cooper'),
        ('1989-1990', 'Billy Phillips'),
        ('1990-1991', 'Trevor Dawkins'),
        ('1991-1992', 'Gordon Jago'),
        ],

    'Defender of the Year': [
        ('1981-1982', 'Val Tuksa'),
        ('1982-1983', 'Bernie James'),
        ('1983-1984', 'Kim Roentved'),
        ('1984-1985', 'Kevin Crow'),
        ('1985-1986', 'Kim Roentved'),
        ('1986-1987', 'Bruce Savage'),
        ('1987-1988', 'Kevin Crow'),
        ('1988-1989', 'Kevin Crow'),
        ('1989-1990', 'Wes McLeoad'),
        ('1990-1991', 'Kevin Crow'),
        ('1991-1992', 'Kevin Crow'),
        ],

    'Goalkeeper of the Year': [
        ('1978-1979', 'Paul Hammond'),
        ('1979-1980', 'Sepp Gantenhammer'),
        ('1980-1981', 'Enzo DiPede'),
        ('1981-1982', 'Slobo Ilijevski'),
        ('1982-1983', 'Zoltan Toth'),
        ('1983-1984', 'Slobo Ilijevski'),
        ('1984-1985', 'Scott Manning'),
        ('1985-1986', 'Keith Van Eron'),
        ('1986-1987', 'Tino Lettieri'),
        ('1987-1988', 'Zoltan Toth'),
        ('1988-1989', 'Victor Nogueira'),
        ('1989-1990', 'Joe Papaleo'),
        ('1990-1991', 'Victor Nogueira'),
        ('1991-1992', 'Victor Nogueira'),
        ],

    'Scoring Champion': [
        ('1978-1979', 'Fred Grgurev'),
        ('1979-1980', 'Steve Zungul'),
        ('1980-1981', 'Steve Zungul'),
        ('1981-1982', 'Steve Zungul'),
        ('1982-1983', 'Steve Zungul'),
        ('1983-1984', 'Stan Stamenkovic'),
        ('1984-1985', 'Steve Zungul'),
        ('1985-1986', 'Steve Zungul'),
        ('1986-1987', 'Tatu'),
        ('1987-1988', 'Erik Rasmussen'),
        ('1988-1989', 'Preki'),
        ('1989-1990', 'Tatu'),
        ('1990-1991', 'Tatu'),
        ('1991-1992', 'Zoran Karic'),
        ],


    'Pass Master': [
        ('1978-1979', 'Paul Hammond'),
        ('1979-1980', 'Sepp Gantenhammer'),
        ('1980-1981', 'Enzo DiPede'),
        ('1981-1982', 'Slobo Ilijevski'),
        ('1982-1983', 'Zoltan Toth'),
        ('1983-1984', 'Slobo Ilijevski'),
        ('1984-1985', 'Scott Manning'),
        ('1985-1986', 'Keith Van Eron'),
        ('1986-1987', 'Tino Lettieri'),
        ('1987-1988', 'Zoltan Toth'),
        ('1988-1989', 'Victor Nogueira'),
        ('1989-1990', 'Joe Papaleo'),
        ('1990-1991', 'Victor Nogueira'),
        ('1991-1992', 'Zoran Karic'),
        ],

    'Rookie of the Year': [
        ('1979-1980', 'Jim Sinclair'),
        ('1980-1981', 'Don Ebert'),
        ('1981-1982', 'German Iglesias'),
        ('1982-1983', 'Kirk Shermer'),
        ('1983-1984', 'Kevin Maher'),
        ('1984-1985', 'Ali Kazemaini'),
        ('1985-1986', 'Dave Boncek'),
        ('1986-1987', 'John Stollmeyer'),
        ('1987-1988', 'David Doyle'),
        ('1988-1989', 'Rusty Troy'),
        ('1989-1990', 'Terry Brown'),
        ('1990-1991', 'David Banks'),
        ('1991-1992', 'Tommy Tanner'),
        ],

    'Newcomer of the Year': [
        ('1986-1987', 'Steve Kinsey'),
        ('1987-1988', 'Nenad Zigante'),
        ('1988-1989', 'Domenic Mobilio'),
        ('1989-1990', 'Claudio DeOliveira'),
        ('1990-1991', 'Paul Pescholido'),
        ],

    # Playoff MVP, playoff Unsung hero

}

misl2 = {
    'competition': 'Major Indoor Soccer League (2001-2008)',
    'team_data': ['Champion'],

    'Champion': [
        ('2001-2002', 'Philadelphia KiXX'),
        ('2002-2003', 'Baltimore Blast'),
        ('2003-2004', 'Baltimore Blast'),
        ('2004-2005', 'Milwaukee Wave'),
        ('2005-2006', 'Baltimore Blast'),
        ('2006-2007', 'Philadelphia KiXX'),
        ('2007-2008', 'Baltimore Blast'),
        ],

    'Coach of the Year': [
        ('2001-2002', 'Keith Tozer'),
        ('2002-2003', 'Keith Tozer'),
        ('2003-2004', 'Tatu'),
        ('2004-2005', 'Omid Namazi'),
        ('2005-2006', 'Omid Namazi'),
        ('2006-2007', 'Mark Pulisic'),
        ],

    'Defender of the Year': [
        ('2001-2002', 'Sean Bowers'),
        ('2002-2003', 'Genoni Martinez'),
        ('2003-2004', 'Genoni Martinez'),
        ('2004-2005', 'Pat Morris'),
        ('2005-2006', 'Genoni Martinez'),
        ('2006-2007', 'Genoni Martinez'),
        ],

    'Goalkeeper of the Year': [
        ('2001-2002', 'Voctor Nogueira'),
        ('2002-2003', 'Voctor Nogueira'),
        ('2003-2004', 'Pete Pappas'),
        ('2004-2005', 'Pete Pappas'),
        ('2005-2006', 'Brett Phillips'),
        ('2006-2007', 'Pete Pappas'),
        ],

    'MVP': [
        ('2001-2002', 'Dino Delevski'),
        ('2002-2003', 'Dino Delevski'),
        ('2003-2004', 'Greg Howes'),
        ('2004-2005', 'Greg Howes'),
        ('2005-2006', 'Adauto Neto'),
        ('2006-2007', 'Jamar Beasley'),
        ],

    'Rookie of the Year': [
        ('2001-2002', 'Billy Nelson'),
        ('2002-2003', 'PJ Wakefield'),
        ('2003-2004', 'Jamar Beasley'),
        ('2004-2005', 'John Barry Nusum'),
        ('2005-2006', 'Vicente Figueroa'),
        ('2006-2007', 'Stephen Armstrong'),
        ],

    # All-MISL first, second teams, all-rookie
}

misl3 = {
    'competition': 'Major Indoor Soccer League (2008-2014)',
    'team_data': ['Champion'],

    'Champion': [
        ('2008-2009', 'Baltimore Blast'),
        ('2009-2010', 'Monterrey La Raza'),
        ('2010-2011', 'Milwaukee Wave'),
        ('2011-2012', 'Milwaukee Wave'), 
        ('2012-2013', 'Baltimore Blast'),
        ('2013-2014', 'Missouri Comets'),
        ],

    'MVP': [
        ('2008-2009', 'Byron Alvarez'),
        ('2009-2010', 'Genoni Martinez'), 
        ('2010-2011', 'Byron Alvarez'), #http://www.examiner.net/x911071376/Byron-Alvarez-picked-as-MISL-MVP
        ('2011-2012', 'Geison'),
        ('2012-2013', 'Doug Miller'),
        ('2013-2014', 'Mike Lookingland'),

        ],

    'Defensive Player of the Year': [
        ('2008-2009', 'Pat Morris'),
        ('2009-2010', 'Genoni Martinez'), 
        #('2010-2011', 
        ('2011-2012', 'Mike Lookingland'),
        ('2012-2013', 'Mike Lookingland'),
        ('2013-2014', 'Mike Lookingland'),

        ],

    'Goalkeeper of the Year': [
        ('2008-2009', 'Sagu'),
        ('2009-2010', 'Nick Vorberg'),
        #('2010-2011', 
        ('2011-2012', 'Sagu'),
        ('2012-2013', 'Nick Vorberg'),
        ('2013-2014', 'William Vanzela'),

        ],

    'Rookie of the Year': [
        ('2008-2009', 'Pat Healey'),
        ('2009-2010', 'Max Ferdinand'),
        ('2010-2011', 'Lucas Rodriguez'),
        ('2011-2012', 'Sinisa Ubiparipovic'),
        ('2012-2013', 'Luan Oliveira'),
        ('2013-2014', 'Odaine Sinclair'),
        ],

    'Coach of the Year': [
        ('2008-2009', 'Danny Kelly'),
        ('2009-2010', 'Keith Tozer'),
        #('2010-2011', 
        ('2011-2012', 'Keith Tozer'),
        ('2012-2013', 'Danny Kelly'),
        ('2013-2014', 'Danny Kelly'),
        ],

    # All-Rookie, All-League, Championship MVP
}

# Division 2
        

npsl = {
    'competition': 'National Professional Soccer League (indoor)',
    'team_data': ['Champion'],
    
    # find original 1999-2000, 2000-2001 awards.
    # soccer history archives unreliable.

    'Champion': [
        ('1984-1985', 'Canton Invaders'),
        ('1985-1986', 'Canton Invaders'),
        ('1986-1987', 'Louisville Thunder'),
        ('1987-1988', 'Canton Invaders'),
        ('1988-1989', 'Canton Invaders'),
        ('1989-1990', 'Canton Invaders'),
        ('1990-1991', 'Chicago Power'),
        ('1991-1992', 'Detroit Rockers'),
        ('1992-1993', 'Kansas City Attack'),
        ('1993-1994', 'Cleveland Crunch'),
        ('1994-1995', 'St. Louis Ambush'),
        ('1995-1996', 'Cleveland Crunch'),
        ('1996-1997', 'Kansas City Attack'),
        ('1997-1998', 'Milwaukee Wave'),
        ('1998-1999', 'Cleveland Crunch'),
        ('1999-2000', 'Milwaukee Wave'),
        ('2000-2001', 'Milwaukee Wave'),
        ],

    'MVP': [
        ('1984-1985', 'Lesh Shkeli'),
        ('1985-1986', 'Don Tobin'),
        ('1986-1987', 'Rudy Pikuzinski'),
        ('1987-1988', 'Rudy Pikuzinski'),
        ('1988-1989', 'Rudy Pikuzinski'),
        ('1989-1990', 'Jamie Swanner'),
        ('1990-1991', 'Andy Chapman'),
        ('1991-1992', 'Jamie Swanner'),
        ('1992-1993', 'Hector Marinaro'),
        ('1993-1994', 'Zoran Karic'),
        ('1994-1995', 'Hector Marinaro'),
        ('1995-1996', 'Hector Marinaro'),
        ('1996-1997', 'Hector Marinaro'),
        ('1997-1998', 'Victor Nogueira'),
        ('1998-1999', 'Hector Marinaro'),
        ('1999-2000', 'Hector Marinaro'),
        ],

    'Defender of the Year': [
        ('1984-1985', 'Oscar Pisano'),
        ('1985-1986', 'Oscar Pisano'),
        ('1986-1987', 'Tim Tyma'),
        ('1987-1988', 'Tim Tyma'),
        ('1988-1989', 'Tim Tyma'),
        ('1989-1990', 'Bret Hall'),
        ('1990-1991', 'Denzil Antonio'),
        ('1991-1992', 'Matt Knowles'),
        ('1992-1993', 'Kim Roentved'),
        ('1993-1994', 'Sean Bowers'),
        ('1994-1995', 'Sean Bowers'),
        ('1995-1996', 'Matt Knowles'),
        ('1996-1997', 'Daryl Doran'),
        ('1997-1998', 'Matt Knowles'),
        ('1998-1999', 'Kevin Hundelt'),
        ('1999-2000', 'James Dunn'),
        ],

    'Goalkeeper of the Year': [
        ('1984-1985', 'Rick Schweizer'),
        ('1985-1986', 'Victor Petroni'),
        ('1986-1987', 'Jamie Swanner'),
        ('1987-1988', 'Manny Sanchez'),
        ('1988-1989', 'Jamie Swanner'),
        ('1989-1990', 'Jamie Swanner'),
        ('1990-1991', 'Jamie Swanner'),
        ('1991-1992', 'Jamie Swanner'),
        ('1992-1993', 'Cris Vaccaro'),
        ('1993-1994', 'Victor Nogueira'),
        ('1994-1995', 'Jamie Swanner'),
        ('1995-1996', 'Victor Nogueira'),
        ('1996-1997', 'Victor Nogueira'),
        ('1997-1998', 'Victor Nogueira'),
        ('1998-1999', 'Victor Nogueira'),
        ('1999-2000', 'Victor Nogueira'),
        ],

    'Rookie of the Year': [
        ('1985-1986', 'Jamie Swanner'),
        ('1986-1987', 'Paul Zimmerman'),
        ('1987-1988', 'Rod Castro'),
        ('1988-1989', 'Carlos Pena'),
        ('1989-1990', 'Brian Haynes'),
        ('1990-1991', 'Brian Finnerty'),
        ('1990-1991', 'Jay Resink'),
        ('1991-1992', 'Sean Bowers'),
        ('1992-1993', 'Brett Phillips'),
        ('1993-1994', 'Tarik Walker'),
        ('1994-1995', 'Henry Gutierrez'),
        ('1995-1996', 'Jason Willan'),
        ('1996-1997', 'Jason Dunn'),
        ('1997-1998', 'Travis Roy'),
        ('1998-1999', 'Martin Nash'),
        ('1999-2000', 'Clovia Simas'),
        ],

    'Coach of the Year': [
        ('1984-1985', 'Klaas deBoer'),
        ('1985-1986', 'Trevor Dawkins'),
        ('1986-1987', 'Terry Nichol'),
        ('1987-1988', 'Terry Nichol'),
        ('1988-1989', 'John Dolinsky'),
        ('1989-1990', 'Rick Schweizer'),
        ('1990-1991', 'Pato Margetic'),
        ('1990-1991', 'Brian Tinnion'),
        ('1991-1992', 'Jim Polihan'),
        ('1992-1993', 'Zoran Savic'),
        ('1993-1994', 'Daryl Doran'),
        ('1994-1995', 'Zoran Savic'),
        ('1995-1996', 'Keith Tozer'),
        ('1996-1997', 'Ross Ongaro'),
        ('1997-1998', 'Keith Tozer'),
        ('1998-1999', 'Ross Ongaro'),
        ('1999-2000', 'Keith Tozer'),
        ],

}
       


cisl = {
    'competition': 'Continental Indoor Soccer League',
    'team_data': ['Champion'],

    'Champion': [
        (1993, 'Dallas Sidekicks'),
        (1994, 'Las Vegas Dustdevils'),
        (1995, 'Monterrey La Raza'),
        (1996, 'Monterrey La Raza'),
        (1997, 'Seattle SeaDogs'),
        ],

    'MVP': [
        (1993, 'Tatu'),
        (1994, 'Tatu'),
        (1995, 'Preki'),
        (1996, 'Tatu'),
        (1997, 'Paul Dougherty'),
        ],

    'Coach of the Year': [
        (1993, 'Gordon Jago'),
        (1994, 'George Fernandez'),
        (1995, 'Erich Geyer'),
        (1996, 'Trevor Dawkins'),
        (1997, 'Fernando Clavijo'),
        ],

    'Rookie of the Year': [
        (1993, 'Marco Lopez'),
        (1994, 'John Olu Molomo'),
        (1995, 'Mark Chung'),
        (1996, 'Carlos Farias'),
        ],

    'Defender of the Year': [
        (1993, 'Sean Bowers'),
        (1994, 'Ralph Black'),
        (1995, 'Danny Pena'),
        (1996, 'Troy Snyder'),
        ],

    # Playoff MVP

    'Goalkeeper of the Year': [
        (1994, 'Antonio Cortes'),
        (1995, 'Mike Dowler'),
        (1996, 'Juan de la O'),
        ],
}




wisl = {
    'competition': 'World Indoor Soccer League',
    'team_data': ['Champion'],

    'Champion': [
        (1998, 'Dallas Sidekicks'),
        (1999, 'Sacramento Knights'),
        (2000, 'Monterrey La Raza'),
        (2001, 'Dallas Sidekicks'),
        ],

    'MVP': [
        (1998, 'Tatu'),
        (1999, 'David Doyle'),
        (2000, 'Mariano Bollela'),
        (2001, 'Ato Leone'),
        ],

    'Goalkeeper of the Year': [
        (1998, 'Dan Madsen'),
        (1999, 'Brett Phillips'),
        (2000, 'Sagu'),
        (2001, 'Sagu'),
        ],

    'Goalkeeper of the Year': [
        (1998, 'Dan Madsen'),
        (1999, 'Brett Phillips'),
        (2000, 'Sagu'),
        (2001, 'Sagu'),
        ],

    'Defender of the Year': [
        (1998, 'Rusty Troy'),
        (1999, 'Iain Fraser'),
        (2000, 'Rob Baarts'),
        (2001, 'Iain Fraser'),
        ],

    'Rookie of the Year': [
        (1998, 'Dan Madsen'),
        (2000, 'Clint Regier'),
        ],

    'Coach of the Year': [
        (1998, 'Tatu'),
        (2000, 'Jeff Betts'),
        ],


}


xsl = {
    'competition': 'Xtreme Soccer League',
    'team_data': ['Champion'],

    'Champion': [('2008-2009', 'Detroit Ignition')],
    'MVP': [('2008-2009', 'Danny Waltman')],
    'Offensive Player of the Year': [('2008-2009', 'Lucio Gonzaga')],
    'Defensive Player of the Year': [('2008-2009', 'Josh Rife')],
    'Rookie of the Year': [('2008-2009', 'Mrco Terminesi')],
    'Coach of the Year': [('2008-2009', 'Matt Johnson')],
    # All-XSL team, players of the month
    }



# Developmental

eisl = {
    'competition': 'Eastern Indoor Soccer League',
    'team_data': ['Champion'],

    'Champion': [
        (1997, 'Lafayette SwampCats'),
        (1998, 'Lafayette SwampCats'),
        ],
}


aisl = {
    'competition': 'American Indoor Soccer League',
    'team_data': ['Champion'],

    'Champion': [
        ('2002-2003', 'Massachusetts Aztecs'),
        ('2004-2005', 'Detroit-Windsor Border Stars'),
        ('2005-2006', 'Cincinnati Excite'),
        ('2006-2007', 'Massachusetts Twisters'),
        ('2007-2008', 'Rockford Rampage'),

        ],
}

sisl = {
    'competition': 'Southwest Indoor Soccer League',
    'team_data': ['Champion'],

    'Champion': [
        ('1986-1987', 'Garland Genesis'),
        ('1987-1988', 'Oklahoma City Warriors'),
        ('1988-1989', 'Lubbock Lazers'),
        ('1989-1990', 'Addison Arrows'),
        ('1990-1991', 'Colorado Comets'),
        ('1991-1992', 'Oklahoma City Warriors'),
        ('1992-1993', 'Atlanta Magic'),
        ('1993-1994', 'Atlanta Magic'),
        ('1994-1995', 'Atlanta Magic'),
        ('1995-1996', 'Baltimore Bays'),
        ('1996-1997', 'Baltimore Bays'),
        ('1997-1998', 'Baltimore Bays'),
        ],


    'MVP': [
        ('1986-1987', 'Greg Nicholas'),
        ('1987-1988', 'Austin Hudson'),
        ('1988-1989', 'Brian Monaghan'),
        ('1989-1990', 'Andy Crawford'),
        ('1990-1991', 'Chino Melendez'),
        ('1991-1992', 'Chris Cook'),
        ('1992-1993', 'Rich Richmond'),
        ('1993-1994', 'Brian Moore'), #Sizzling Four MVP
        ('1994-1995', 'Moe Suri'),
        ],


    'Goalkeeper of the Year': [
        ('1986-1987', 'Steve Myers'),
        ('1987-1988', 'Todd Brunskill'),
        ('1988-1989', 'David Swissler'),
        ],


    'Rookie of the Year': [
        ('1986-1987', 'Ty Kongdara'),
        ('1987-1988', 'Steve Bailey'),
        ('1988-1989', 'Todd Hoodenpyle'),
        ('1989-1990', 'Jose Miranda'),
        ('1990-1991', 'Albertico Morales'),
        ('1991-1992', 'Noel Clackum'),
        ('1991-1992', 'Emillo Romero'),
        ('1992-1993', 'Omar Felix'),
        ('1993-1994', 'Billy Ronson'),
        ('1994-1995', 'Colby Williams'),
        ],


    'Coach of the Year': [
        ('1986-1987', 'Chico Villar'),
        ('1987-1988', 'Chico Villar'),
        ('1988-1989', 'Tony Simoes'),
        ('1989-1990', 'Peter Baralic'),
        ('1990-1991', 'Caesar Cervin'),
        ('1991-1992', 'Carlos Acosta'),
        ('1992-1993', 'Zelimar Antonievic'),
        ('1993-1994', 'Charlie Morgan'),
        ('1994-1995', 'Charlie Morgan'),
        ],
}



