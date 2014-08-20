#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

# Footballer of the Year of Argentina (in Spanish: Olimpia de Plata al Mejor Futbolista, 
# that literally translates to "Silver Olimpia to the Best Footballer) is a yearly award 
# given by the Argentine Sports Journalists' Circle 
# (Círculo de Periodistas Deportivos de la República Argentina) as one of 
# the Olimpia Awards, the most important sports award in Argentina.


metropolitano = {
    'competition': 'Campeonato Metropolitano (Argentina)',
    'team_data': ['Champion'],
    'champion': 'Champion',

    'Champion': [
        (1967, 'Estudiantes (LP)'),
        (1968, 'San Lorenzo de Almagro'),
        (1969, 'Chacarita Juniors'),
        (1970, 'Independiente'),
        (1971, 'Independiente'),
        (1972, 'San Lorenzo de Almagro'),
        (1973, 'Huracan'),
        (1974, 'Newell\'s Old Boys'),
        (1975, 'River Plate'),
        (1976, 'Boca Juniors'),
        (1977, 'River Plate'),
        (1978, 'Quilmes'),
        (1979, 'River Plate'),
        (1980, 'River Plate'),
        (1981, 'Boca Juniors'),
        (1982, 'Estudiantes (LP)'),
        (1983, 'Independiente'),
        (1984, 'Argentinos Juniors'),
        ],
}

d = {
    'competition': 'Argentine Primera División',
    'team_data': ['Champion'],
    'champion': 'Champion',

    'Champion': [
        (1899, 'Belgrano Athletic'),
        (1900, 'English High School AC'),
        (1901, 'Alumni'),
        (1902, 'Alumni'),
        (1903, 'Alumni'),
        (1904, 'Belgrano Athletic'),
        (1905, 'Alumni'),
        (1906, 'Alumni'),
        (1907, 'Alumni'),
        (1908, 'Belgrano Athletic'),
        (1909, 'Alumni'),
        (1910, 'Alumni'),
        (1911, 'Alumni'),
        #(1912, 
        #(1913, 
        #(1914,
        (1915, 'Racing Club (Argentina)'),
        (1916, 'Racing Club (Argentina)'),
        (1917, 'Racing Club (Argentina)'),
        (1918, 'Racing Club (Argentina)'),
        #(1919,
        (1927, 'San Lorenzo de Almagro'),
        (1928, 'Huracan'),
        (1929, 'Gimnasia y Esgrima La Plata'),

        (1935, 'Boca Juniors'),
        (1936, 'River Plate'),
        (1937, 'River Plate'),
        (1938, 'Independiente'),
        (1939, 'Independiente'),
        (1940, 'Boca Juniors'),
        (1941, 'River Plate'),
        (1942, 'River Plate'),
        (1943, 'Boca Juniors'),
        (1944, 'Boca Juniors'),
        (1945, 'River Plate'),
        (1946, 'San Lorenzo de Almagro'),
        (1947, 'River Plate'),
        (1948, 'Independiente'),
        (1949, 'Racing Club'),
        (1950, 'Racing Club'),
        (1951, 'Racing Club'),
        (1952, 'River Plate'),
        (1953, 'River Plate'),
        (1954, 'Boca Juniors'),
        (1955, 'River Plate'),
        (1956, 'River Plate'),
        (1957, 'River Plate'),
        (1958, 'Racing Club'),
        (1959, 'San Lorenzo de Almagro'),
        (1960, 'Independiente'),
        (1961, 'Racing Club'),
        (1962, 'Boca Juniors'),
        (1963, 'Independiente'),
        (1964, 'Boca Juniors'),
        (1965, 'Boca Juniors'),
        (1966, 'Racing Club'),

        (1967, 'Independiente (A)'),
        (1968, 'Velez Sarsfield'),
        (1969, 'Boca Juniors'),
        (1970, 'Boca Juniors'),
        (1971, 'Rosario Central'),
        (1972, 'San Lorenzo de Almagro'),
        (1973, 'Rosario Central'),
        (1974, 'San Lorenzo de Almagro'),
        (1975, 'River Plate'),
        (1976, 'Boca Juniors'),
        (1977, 'Independiente (A)'),
        (1978, 'Independiente (A)'),
        (1979, 'River Plate'),
        (1980, 'Rosario Central'),
        (1981, 'River Plate'),
        (1982, 'Estudiantes (LP)'),
        (1983, 'Independiente (A)'),
        (1984, 'Argentinos Juniors'),
        (1985, 'Argentinos Juniors'),

        ('1985-1986', 'River Plate'),
        ('1986-1987', 'Rosario Central'),
        ('1987-1988', 'Newell\'s Old Boys'),
        ('1988-1989', 'Independiente'),
        ('1989-1990', 'River Plate'),
        ('1990-1991', 'Newell\'s Old Boys'),

        ('1991-1992 Apertura', 'River Plate'),
        ('1991-1992 Clausura', 'Newell\'s Old Boys'),

        ('1992-1993 Apertura', 'Boca Juniors'),
        ('1992-1993 Clausura', 'Velez Sarsfield'),

        ('1993-1994 Apertura', 'River Plate'),
        ('1993-1994 Clausura', 'Independiente'),

        ('1994-1995 Apertura', 'River Plate'),
        ('1994-1995 Clausura', 'San Lorenzo de Almagro'),

        ('1995-1996 Apertura', 'Velez Sarsfield'),
        ('1995-1996 Clausura', 'Velez Sarsfield'),

        ('1996-1997 Apertura', 'River Plate'),
        ('1996-1997 Clausura', 'River Plate'),

        ('1997-1998 Apertura', 'River Plate'),
        ('1997-1998 Clausura', 'Velez Sarsfield'),

        ('1998-1999 Apertura', 'Boca Juniors'),
        ('1998-1999 Clausura', 'Boca Juniors'),

        ('1999-2000 Apertura', 'River Plate'),
        ('1999-2000 Clausura', 'River Plate'),
        
        ('2000-2001 Apertura', 'Boca Juniors'),
        ('2000-2001 Clausura', 'San Lorenzo de Almagro'),

        ('2001-2002 Apertura', 'Racing Club'),
        ('2001-2002 Clausura', 'River Plate'),

        ('2002-2003 Apertura', 'Independiente'),
        ('2002-2003 Clausura', 'River Plate'),

        ('2003-2004 Apertura', 'Boca Juniors'),
        ('2003-2004 Clausura', 'River Plate'),

        ('2004-2005 Apertura', 'Newell\'s Old Boys'),
        ('2004-2005 Clausura', 'Velez Sarsfield'),

        ('2005-2006 Apertura', 'Boca Juniors'),
        ('2005-2006 Clausura', 'Boca Juniors'),

        ('2006-2007 Apertura', 'Estudiantes de la Plata'),
        ('2006-2007 Clausura', 'San Lorenzo de Almagro'),

        ('2007-2008 Apertura', 'Lanus'),
        ('2007-2008 Clausura', 'River Plate'),

        ('2008-2009 Apertura', 'Boca Juniors'),
        ('2008-2009 Clausura', 'Velez Sarsfield'),

        ('2009-2010 Apertura', 'Banfield'),
        ('2009-2010 Clausura', 'Argentinos Juniors'),

        ('2010-2011 Apertura', 'Estudiantes de la Plata'),
        ('2010-2011 Clausura', 'Velez Sarsfield'),

        ('2011-2012 Apertura', 'Boca Juniors'),
        ('2011-2012 Clausura', 'Arsenal de Sarandi'),

        ('2012-2013 Inicial', 'Velez Sarsfield'),
        ('2012-2013 Final', 'Newell\'s Old Boys'),
        #('2012-2013', 'Velez Sarsfield'),

        ('2013-2014 Inicial', 'San Lorenzo de Almagro'),
        ('2013-2014 Final', 'River Plate'),
        
         ]




}

l = [
    (1970, ('Héctor Yazalde', )),
    (1971, ('José Omar Pastoriza', )), 
    (1972, ('Ángel Bargas', )),
    (1973, ('Miguel Ángel Brindisi', )),
    (1974, ('Miguel Ángel', )),
    (1975, ('Héctor Scotta', )),
    (1976, ('Daniel Passarella', )),
    (1977, ('Ubaldo Fillol', )), 
    (1978, ('Mario Kempes', )), 
    (1979, ('Diego Maradona', )),
    (1980, ('Diego Maradona', )),
    (1981, ('Diego Maradona', )),
    (1982, ('Hugo Orlando Gatti', )),
    (1983, ('Ricardo Bochini', )),
    (1984, ('Alberto Márcico', )),
    (1985, ('Enzo Francescoli', )),
    (1986, ('Diego Maradona', )),
    (1987, ('Néstor Fabbri', )),
    (1988, ('Rubén Paz', )),
    (1989, ('Carlos Alfaro Moreno', )),
    (1990, ('Sergio Goycochea', )),
    (1991, ('Oscar Ruggeri', )),
    (1992, ('Luis Islas', )),
    (1993, ('Ramón Medina', )),
    (1994, ('Carlos Navarro Montoya', )),
    (1995, ('Enzo Francescoli', )),
    (1996, ('José Luis Chilavert', )),
    (1997, ('Marcelo Salas', )),
    (1998, ('Gabriel Batistuta', )),
    (1999, ('Javier Saviola', )),
    (2000, ('Juan Román Riquelme', )),
    (2001, ('Juan Román Riquelme', )),
    (2002, ('Gabriel Milito', )),
    (2003, ('Carlos Tévez', )),
    (2004, ('Carlos Tévez', )),
    (2005, ('Lionel Messi', )),
    (2006, ('Juan Sebastián Verón', )),
    (2007, ('Lionel Messi', )),
    (2008, ('Juan Román Riquelme', 'Lionel Messi', )),
    (2009, ('Juan Sebastián Verón', 'Lionel Messi', )),
    (2010, ('Juan Manuel Martínez', 'Lionel Messi', )),
    ]
