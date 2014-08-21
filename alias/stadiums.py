#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

# This should only be used for
# 1. Stadiums with multiple names
# 2. Stadiums whose names are incorrect (externally)


def get_stadium(s):
    """
    Recursive. 
    """
    #print s

    s = s.strip()

    #if type(s) == type(''):
    #    s = unicode(s, 'utf-8')

    if s in sd:
        return get_stadium(sd[s])
    else:
        return s

sd = {}


misc = {
    'Regions Park': 'Hoover Metropolitan Stadium',
    'UK Soccer Complex': 'University of Kentucky Soccer Complex',
}

world = {

    'Frank Clair Stadium': 'TD Place',


    
    'Maureen Hendricks Field Maryland SoccerPlex': 'Maryland SoccerPlex',
    'Verizon Wireless Field Durwood Stadium': 'Durwood Stadium',

    'Moda Health Pitch Memorial Stadium': 'Seattle High School Memorial Stadium',
    'Benedictine U. Sports Complex Stadium': 'Benedictine University Sports Complex Stadium',

    'Memorial Stadium Baltimore': 'Memorial Stadium (Baltimore)',
    'Estadio Cuscatlan': 'Estadio Cuscatlán',
    'Estadio Sergio Leon Chavez': 'Estadio Sergio León Chávez',

    'Stade Sylvio Cantor': 'Stade Sylvio Cator',

    'A Luz': 'Estádio da Luz',
    'Municipal de Braga': 'Estádio Municipal de Braga',

    'José Alvalade': 'Estadio José Alvalade',
    'Ernst-Hapoel Stadion': 'Ernst-Happel-Stadion',
    'Carlos Iturralde Rivero': 'Estadio Carlos Iturralde',

    'Olimpico di Torino': 'Stadio Olimpico di Torino',
    'Caliente': 'Estadio Caliente',

    'Nsc Olympiysliy Stadium': 'Kiev Olympic Stadium',    

    'Peter Mokaba': 'Peter Mokaba Stadium',

    'Ramón Aguilera': 'Estadío Ramón Aguilera', 
    'Alejandro Serrano Aguilar': 'Estadio Alejandro Serrano Aguilar',

    'Monumental de Lima': 'Estadio Monumental "U"',
    

    'Atanasio Girardot': 'Estadio Atanasio Girardot',


    'Dinamo de Minsk': 'Dynama Stadium (Minsk)',
    
    'San Petersburgo Petrovsky': 'Petrovsky Stadium',

    'Georgios Karaiskakis': 'Georgios Karaiskakis Stadium',

    'Toyota': 'Toyota Stadium',
    'Calcio': 'Serie A',

    'San Jakob': 'St. Jakob-Park',

    'Buck Shaw': 'Buck Shaw Stadium',
    'Olímpico Atahualpa': 'Estadio Olímpico Atahualpa',

    'Olímpico de Turín': 'Stadio Olimpico di Torino',

    'Estadio Olímpico de Roma': 'Stadio Olimpico',

    'Real Bafokeng': 'Royal Bafokeng Stadium',

    'New Dallas Cowboys': 'Cowboys Stadium',
    'Cowboys Stadium': 'AT&T Stadium',

    'Eladio Rosabal Cordero': 'Estadio Eladio Rosabal Cordero',

    'Feliciano Cáceres': 'Estadio Feliciano Cáceres',

    'Ernst Happel': 'Ernst-Happel-Stadion',

    'Benito Villamarín': 'Estadio Benito Villamarín',
    'Estadio Sergio Leon Chavez': 'Estadio Sergio León Chávez',
    'Vfl Wolfsburg Arena': 'Volkswagen Arena',

    'George Capwell': 'Estadio George Capwell',
    'San Carlos de Apoquindo': 'Estadio San Carlos de Apoquindo',

    'Omnilife': 'Estadio Omnilife',

    'Artemio Franchi': 'Stadio Artemio Franchi',

    'San Paolo': 'Stadio San Paolo',

    'BANORTE': 'Estadio Banorte',
    
    'Amsterdam Arena': 'Amsterdam ArenA',
    'Mestalla Stadium': 'Estadio de Mestalla',

    'Alejandro Villanueva': 'Estadio Alejandro Villanueva',
    'Elías Aguirre': 'Estadio Elías Aguirre',
    'Marcelo Bielsa': 'Estadio Marcelo Bielsa',

    'VfB Arena': 'Mercedes-Benz Arena',


    'El Madrigal': 'Estadio El Madrigal',
    'Miguel Grau': 'Estadio Miguel Grau (Piura)', # hmm.
    #'Monumental de Lima': 
    'Estadio Nacional de Lima': 'Estadio Nacional de Peru',
    
    'Libertadores de América': 'Estadio Libertadores de América',
    'Padre Ernesto Martearena': 'Estadio Padre Ernesto Martearena',
    'San Juan del Bicentenario': 'Estadio San Juan del Bicentenario',

    'Ono Estadi': 'Iberostar Stadium',
    'Ciutat de Valencia': 'Estadi Ciutat de València',
    
    'Estadio Monumental Isidro Romero': 'Estadio Monumental Isidro Romero Carbo',
    'Asim Ferhatovic Hase Stadium': 'Asim Ferhatović Hase Stadium',
    'Estadio D. Afonso Henriques': 'Estádio D. Afonso Henriques',
    'Estadio das Antas': 'Estádio das Antas',
    'Khalifa Olympic Stadium': 'Khalifa International Stadium',
    'Utama Stadium': 'Utama Negeri Stadium',
    'Estadio Newell\'s Old Boys': 'Estadio Marcelo Bielsa',

    'Ramón Sánchez Pizjuán': 'Estadio Ramón Sánchez Pizjuán',

    'Stade Jacques Chaban-Delmas': 'Stade Chaban-Delmas',



    'El Campín': 'Estadio El Campin',
    'Estadio Nemesio Camacho': 'Estadio El Campin',
    'Estadio Jaime Moron Leon': 'Estadio Jaime Morón León',
    'Bursa Ataturk Stadium': 'Bursa Atatürk Stadium',
    'Huseyin Avni Aker Stadium': 'Hüseyin Avni Aker Stadium',
    'Ali Sami Yen Arena': 'Ali Sami Yen Stadium',
    'Shepherds Bush Stadium': 'Shepherds Bush Green',
    'Cleveland Browns Stadium': 'FirstEnergy Stadium',
    'Home Depot Center': 'StubHub Center',

    'Estadio Bella Vista': 'Estadio Bellavista',
    'Estadio Casa Blanca': 'Estadio de Liga Deportiva Universitaria',
    'Estadio Luis Loreto Lira': 'Estadio José Alberto Pérez',
    'Estadio do Arruba': 'Estádio do Arruda',
    'Estadío Tropical': 'Estadio Pedro Marrero',



    'Wankdorf': 'Wankdorf Stadium',
    'La Pontaise': 'Stade Olympique de la Pontaise',
    'Charmilles': 'Charmilles Stadium',
    'Comunale di Cornaredo': 'Cornaredo Stadium',
    'St. Jacob Park': 'St. Jakob-Park',

    'King Baudouin Stadium': 'Stade Roi Baudouin',
    'Estadío Parque Espana': 'Parque Espana',

    'Estadío Independencia': 'Estádio Independência',
    'Estadio Independencia': 'Estádio Independência',

    'Monumental David Arellano': 'Estadio Monumental David Arellano',
    'Estádio Monumental David Arellano': 'Estadio Monumental David Arellano',

    'Estadio Municipal de Concepcion': 'Estadio Municipal de Concepción',
    'Estadio Feliciano Caceres': 'Estadio Feliciano Cáceres',
    'Estadio Metropolitano Roberto Melendez': 'Estadio Metropolitano Roberto Meléndez',
    'Estadio Olimpico Luis Ramos': 'Estadio José Antonio Anzoátegui',

    'Estadio Francisco Morazan': 'Estadio Francisco Morazán',

    'Estadio Olimpico Metropolitano': 'Estadio Olímpico Metropolitano',
    'Estadio Jorge Calero Suarez': 'Estadio Jorge Calero Suárez',


    'Centro Epsortivo Miecimo da Silva': 'Centro Esportivo Miécimo da Silva',
    'Estadio General Severiano': 'Estádio de General Severiano',
    'Estadio General Severiano': 'Estádio General Severiano',
    'General Artigas Stadium': 'Estadio Parque Artigas',
    'Estadio Olimpico Patria': 'Estadio Olímpico Patria',
    'Estadio Monumental Rio Parapiti': 'Monumental Río Parapití',
    'Estadio Pascual Guerrero': 'Estadio Olímpico Pascual Guerrero',
    'Estadio Hernan Ramirez Villegas': 'Estadio Hernán Ramírez Villegas',
    'Estadio Elias Aguirre': 'Estadio Elías Aguirre',

    'Estadio Ciudad de la Plata': 'Estadio Ciudad de La Plata',
    'Estadio Brigido Iriarte': 'Estadio Brígido Iriarte',
    'Estadio Camilo Cichero': 'Estadio Alberto J. Armando',
    'Estadio Ramon Aguilera': 'Estadio Ramón Tahuichi Aguilera',
    'Estadio Olimpico Atahualpa': 'Estadio Olímpico Atahualpa',
    'Estadio Playa Ancha': 'Estadio Elías Figueroa Brander',

    'Estadio Olimpico Chateau Carreras': 'Estadio Mario Alberto Kempes',
    'Estadio Pascual Guerrero': 'Estadio Olímpico Pascual Guerrero',
    'Estadio Arequipa': 'Estadio Monumental Virgen de Chapi',

    'Estadio Metropolitano de Futbol de Lara': 'Estadio Metropolitano de Fútbol de Lara',
    'Estadio Monumental de Maturin': 'Estadio Monumental de Maturín',

    'Estadio del Bicentenario, San Juan, Argentina': 'Estadio San Juan del Bicentenario',
    'Estadio Brigadier General Estanislao Lopez': 'Estadio Brigadier General Estanislao López',
    'Estadio Jesus Bermudez': 'Estadio Jesús Bermúdez',
    'Estadio Felix Capriles': 'Estadio Félix Capriles',
    'Estadio Modelo': 'Estadio Modelo Alberto Spencer Herrera',

    'Estadio Sao Januario': 'Estádio São Januário',
    'Sportivo Barracas Stadium': 'Estadio Sportivo Barracas',
    'Estadio Gasometro': 'Estadio Gasómetro',
    'Estadio Sport de Nunoa': 'Estadio Campos de Sports de Ñuñoa',



    'Estadio Jose Maria Minella': 'Estadio José María Minella',

    'Estadio Chateau Carreras': 'Estadio Mario Alberto Kempes',



    'Jose Zorrilla': 'Estadio Nuevo José Zorrilla',

    'Benito Villamarin': 'Estadio Benito Villamarín',
    'Estadio Benito Villamarin': 'Estadio Benito Villamarín',

    'Mitsuzawa Stadium': 'Nippatsu Mitsuzawa Stadium',
    'Komazawa Stadium': 'Komazawa Olympic Park Stadium',
    'Chichibu Stadium': 'Chichibunomiya Rugby Stadium',
    'Nova Creu Alta Stadium': 'Estadi de la Nova Creu Alta',
    'La Romereda Stadium': 'La Romareda',
    'Luis Casanova': 'Estadio de Mestalla',
    'Sarria': 'Estadi de Sarrià',
    'Luis Casanova Stadium': 'Estadio de Mestalla',


    'Estadio de San Lazaro': 'Estadio Multiusos de San Lázaro',

    'Jose Rico Perez': 'Estadio José Rico Pérez',
    'Estadio Jose Rico Perez': 'Estadio José Rico Pérez',

    'Riazor': 'Estadio Riazor',
    'La Rosaleda': 'Estadio La Rosaleda',
    'La Mosson': 'Stade de la Mosson',
    'The Willem II Stadium': 'Koning Willem II Stadion',

    'Vijverberg Stadium': 'De Vijverberg',
    'The Parkstad Limburg Stadium': 'Parkstad Limburg Stadion',

    'Unive Stadion': 'Univé Stadion',

    'Arke Stadion': 'De Grolsch Veste',

    'The Galgenwaard Stadium': 'Stadion Galgenwaard',
    'Galgenwaard Stadion': 'Stadion Galgenwaard',
    
    'Rashid Al-Maktoum Stadium': 'Maktoum Bin Rashid Al Maktoum Stadium',
    'Zayed Sports City': 'Sheikh Zayed Stadium',
    'Mohammad Bin Zayed Stadium': 'Mohammed Bin Zayed Stadium',
    'Durival de Brito': 'Estádio Vila Capanema',



    'Eucaliptos': 'Estádio dos Eucaliptos',
    'Estadio dos Eucaliptos': 'Estádio dos Eucaliptos',
    'Roker Park Ground': 'Roker Park',
    'White City': 'White City Stadium',
    'Parc Lescure': 'Stade Chaban-Delmas',


    'Nou Camp Stadium': 'Camp Nou',
    'Velodrome de Vincennes': 'Vélodrome de Vincennes',

    'Olympisch': 'Amsterdam Olympic Stadium',
    'Olympia Stadion': 'Olympiastadion',
    'Highbury': 'Arsenal Stadium',


    'Olympic Park': 'Olympic Park Stadium',


    'easyCredit-Stadion': 'Frankenstadion',
    'Munsu Stadium': 'Ulsan Munsu Football Stadium',
    'Suwon Stadium': 'Suwon World Cup Stadium',
    'Daejeon Stadium': 'Daejeon World Cup Stadium',
    'Jeonju Stadium': 'Jeonju World Cup Stadium',

    'Munsu Football Stadium': 'Ulsan Munsu Football Stadium',
    'Ellis Park': 'Ellis Park Stadium',
    'Loftus Versfeld': 'Loftus Versfeld Stadium',
    'Queens Park Oval': 'Queen\'s Park Oval',

    'Estadío Francisco Morazán': 'Estadio Francisco Morazán',
    'Estadio El Campin': 'Estadio El Campín',
    'Restelo Stadium': 'Estádio do Restelo',
    'B.C. Place': 'BC Place',

    'Estadio Nacional Carias Andino': 'Estadio Tiburcio Carías Andino',
    'Estadio Nacional de Tegucigalpa': 'Estadio Tiburcio Carías Andino',
    'Tegucigalpa Estadío Nacional': 'Estadio Tiburcio Carías Andino',
    'Estadio Tiburcio Carias Andino': 'Estadio Tiburcio Carías Andino',
    'Estadio Nacional Tiburcio Carias': 'Estadio Tiburcio Carías Andino',
    'Estadio Metropolitano Tiburcio Carias': 'Estadio Tiburcio Carías Andino',

    'Maksimir Stadion': 'Stadion Maksimir',
    'Estadio Zorilla': 'Estadio Nuevo José Zorrilla',

    'Tynecastle Park': 'Tynecastle Stadium',
    'Ibrox Park': 'Ibrox Stadium',
    'Trent Bridge Ground': 'Trent Bridge',
    'Kennington Oval': 'The Oval',

    'Bislet Stadium': 'Bislett Stadion',
    'Fulton County Stadium': 'Atlanta-Fulton County Stadium',
    'Seattle Memorial Stadium': 'Seattle High School Memorial Stadium',
    'Allmend Stadium': 'Stadion Allmend',
    'Soccer and Sports Center': 'Kuntz Stadium',
    
    'Stade Municipal en Camee': 'Stade Alfred Marie-Jeanne',
    'Stade Municipal Pierre-Aliker': 'Stade Pierre-Aliker',

    'Estadio Excelsior': 'Estadio Excélsior',
    'Estadío Cuscatlán': 'Estadio Cuscatlán',
    'Estadio Cuscatlan': 'Estadio Cuscatlán',

    'Estadio Castelao (Ceara)': 'Castelão (Ceará)',

    'Navy-Marine Corps Stadium': 'Navy–Marine Corps Memorial Stadium',
    'Wildpark': 'Wildparkstadion',
    'Korte Stadium': 'Ralph Korte Stadium',
    'TD Bank Park': 'TD Bank Ballpark',

    'Estadio Universidad Nacional San Agustin': 'Estadio Monumental Virgen de Chapi',
    'Estadio Nuevo Gasometro': 'Estadio Pedro Bidegain',
    'Estadio Manuel Murrillo Toro': 'Estadio Manuel Murillo Toro',
    'Estadio Metropolitano de Cabudare': 'Estadio Metropolitano de Fútbol de Lara',
    'Estadio Eduardo Jose Farah': 'Estádio Eduardo José Farah',
    'Estadio Arquitecto Antonio Eleuterio': 'Estadio Arquitecto Antonio Eleuterio Ubilla',
    'Estadio Aliardo Soria': 'Estadio Aliardo Soria Pérez',
    'Estadio Leon': 'Estadio León',
    'Estadio Ciudad de Cumana': 'Estadio Ciudad de Cumaná',
    'Estadio Parque El Teniente': 'Estadio El Teniente',

    'Nicolás Leoz': 'Estadio Dr. Nicolás Leoz',
    'Estadio Dr. Nicolas Leoz': 'Estadio Dr. Nicolás Leoz',
    'Estadio Jose Antonio Anzoategui': 'Estadio José Antonio Anzoátegui',
    'Estadio Jose Dellagiovanna': 'Estadio José Dellagiovanna',
    'Estadio Agustin Tovar': 'Estadio Agustín Tovar',
    'Estadio La Carolina': 'Estadio Agustín Tovar',
    'Estadio Brigido Irarte': 'Estadio Brígido Iriarte',

    'St. George Cricket Grounds': 'St. George\'s Cricket Grounds',
    'La Beaujoire': 'Stade de la Beaujoire',
    'Pocitos': 'Estadio Pocitos',


    # British Virgin Islands
    'AO Shirley Recreational Grounds': 'A.O. Shirley Recreation Ground',

    # Greece
    'Karaiskaki': 'Karaiskakis Stadium',
    'Oaca Spyro Louis': 'Olympic Stadium (Athens)',

    # Suriname
    'Andre Kamperveen Stadion': 'André Kamperveen Stadion',
    'Andre Kamperveen Stadium': 'André Kamperveen Stadion',

    # Antigua
    'Sticky Wicket Stadium': 'Stanford Cricket Ground',

    # Cayman Islands
    'Truman Bodden Stadium': 'Truman Bodden Sports Complex',

    # Curacao
    'Ergilio Hato Stadium': 'Stadion Ergilio Hato',

    # Hungary
    'Nep Stadium': 'Nepstadion',

    # England
    'Arnos Vale Ground': 'Arnos Vale Stadium',
    'Loftus Road Stadium': 'Loftus Road',
    'Wembley': 'Wembley Stadium',
    'City of Coventry Stadium': 'Ricoh Arena',

    # Saudi Arabia
    'King Fahd International Stadium': 'King Fahd Stadium',
    'King Fahd II Stadium': 'King Fahd Stadium',

    # Dominican Republic
    'Estadio Olímpico Juan Pablo Duarte': 'Estadio Olímpico Félix Sánchez',
    'Estadio Olimpico Juan Pablo Duarte': 'Estadio Olímpico Félix Sánchez',

    # Brazil
    'Vila Belmiro': 'Estádio Urbano Caldeira',
    'Estadio Palestra Italia': 'Estádio Palestra Itália',
    'Estadio Raimundo Sampaio': 'Estádio Independência',
    'Centro Esportivo Miecimo da Silva': 'Centro Esportivo Miécimo da Silva',

    'Pacaembu': 'Estádio do Pacaembu',
    'Estadio Municipal Paulo Machado de Carvalho': 'Estádio do Pacaembu',
    'Estadio do Pacaembu': 'Estádio do Pacaembu',
    'Estadio Pacaembu': 'Estádio do Pacaembu',
    'Pacaembu Stadium': 'Estádio do Pacaembu',

    'Maracana': 'Estádio do Maracanã',
    'Maracana Stadium': 'Estádio do Maracanã',
    'Estadio do Maracana': 'Estádio do Maracanã',
    'Estadio Ilha do Retiro': 'Estádio Ilha do Retiro',
    'Estadio Durival Britto': 'Estádio Vila Capanema',
    'Estádio Durival Britto e Silva': 'Estádio Vila Capanema',

    'Stadío das Laranjeiras': 'Estádio das Laranjeiras',
    'Estadio das Laranjeiras': 'Estádio das Laranjeiras',

    'Atilio Paiva Olivera': 'Estadio Atilio Paiva Olivera',

    #'Morumbí (Cícero Pompeu de Toledo)': 'Estádio do Morumbi',
    'Morumbí (Cícero Pompeu de Toledo)': 'Estádio do Morumbi',
    'Estadio Morumbi': 'Estádio do Morumbi',
    'Estadio Parque do Sabia': 'Estádio Parque do Sabiá',

    'Estadio Vila Belmiro': 'Estádio Urbano Caldeira',
    'Estadio do Arruda': 'Estádio do Arruda',
    'Estadio Fonte Nova': 'Estádio Fonte Nova',
    'Mineirao': 'Mineirão',
    'Estadio Mineirao': 'Mineirão',
    'Estadio Serra Dourada': 'Estádio Serra Dourada',

    'Estadio Cicero Pompeu de Toledo': 'Estádio do Morumbi',
    'Engenhao': 'Estádio Olímpico João Havelange',

    'José Pinheiro Borda': 'Estádio Beira-Rio',
    'Estadio Jose Pinheiro Borda': 'Estádio Beira-Rio',
    'Estadio Beira Rio': 'Estádio Beira-Rio',
    'Estadio Beira-Rio': 'Estádio Beira-Rio',

    'Arena do Gremio': 'Arena do Grêmio',
    'Estadio do Morumbi': 'Estádio do Morumbi',
    'Estadio Mane Garrincha': 'Estádio Nacional de Brasília',
    'Estádio Nacional de Brasília': 'Estadio Nacional de Brasilia',
    'Estadio Mane Garrincha': 'Estádio Nacional de Brasília',
    'Estadio Durival de Britto': 'Estádio Vila Capanema',

    'Estadio Manoel Barradas': 'Estádio Manoel Barradas',
    'Estadio Ressacada': 'Estádio da Ressacada',
    'Estadio Aderbal Ramos da Silva': 'Estádio da Ressacada',
    'Estádio Aderbal Ramos da Silva': 'Estádio da Ressacada',
    'Estadio Major Antonio Couto Pereira': 'Estádio Couto Pereira',
    'Estadio Metropolitano Roberto Santos': 'Estádio de Pituaçu',
    'Estadio Orlando Scarpelli': 'Estádio Orlando Scarpelli',
    'Estadio Nacional (Brasilia)': 'Estadio Nacional de Brasilia',
    'Parque Antártica': 'Estádio Parque Antarctica',
    'Estadio Parque Antartica': 'Estádio Parque Antarctica',
    'Parque Antartica': 'Estádio Parque Antarctica',
    'Estadio Jaconi': 'Estádio Alfredo Jaconi',
    'Estádio Major Antônio Couto Pereira': 'Estádio Couto Pereira',
    'Estadio do Governo do Estadio de Goias': 'Estádio Serra Dourada',
    'Estádio Metropolitano Roberto Santos': 'Estádio de Pituaçu',
    'Estadio Olimpico Monumental': 'Estádio Olímpico Monumental',
    'Estadio Olimpico do Para': 'Mangueirão',
    'Estádio Olímpico do Pará': 'Mangueirão',
    'Mangueirao': 'Mangueirão',
    'Estadio Rei Pele': 'Estádio Rei Pelé',
    'Estadio Morumbi': 'Estádio do Morumbi',
    'Estádio Vivaldo Lima': 'Vivaldão',
    'Vivaldao': 'Vivaldão',

    'Estadio Governador Joao Castelo': 'Estádio Governador João Castelo',
    'Estadio Couto Pereira': 'Estádio Couto Pereira',
    'Estadio Olimpico Joao Havelange': 'Estádio Olímpico João Havelange',
    'Estadio Joao Havelange': 'Estádio Olímpico João Havelange',
    'Estadio Urbano Caldeira': 'Estádio Urbano Caldeira',

    # Chile
    'Estadio Santa Laura': 'Estadio Santa Laura-Universidad SEK',
    'Estadio Nacional de Chile': 'Estadio Nacional Julio Martínez Prádanos',
    'Estadio Nacional (Chile)': 'Estadio Nacional Julio Martínez Prádanos',
    'Estadio Nacional Julio Martinez': 'Estadio Nacional Julio Martínez Prádanos',
    'Estadio Nacional (Santiago)': 'Estadio Nacional Julio Martínez Prádanos',

    # France
    'Geoffrey Prichard Stadium': 'Stade Geoffroy-Guichard',
    'Felix Bollaert': 'Stade Félix-Bollaert',
    'Stade Felix Bollaert': 'Stade Félix-Bollaert',
    'Stade Felix-Bollaert': 'Stade Félix-Bollaert',
    'Stade Chapou': 'Stade Municipal de Toulouse',
    'Stade de Toulouse': 'Stade Municipal de Toulouse',
    'Stade Olympique de Colombes': 'Stade Olympique Yves-du-Manoir',
    'Stade Olympique Colombes': 'Stade Olympique Yves-du-Manoir',
    'Velodrome Municipal': 'Stade Vélodrome',
    'Stade Velodrome': 'Stade Vélodrome',
    'Pershing Park': 'Stade Pershing',
    'Stade Gerland': 'Stade de Gerland',
    'Gerland': 'Stade de Gerland',
    'Meinau': 'Stade de la Meinau',
    'Victor Boucquey': 'Stade Victor Boucquey',
    'Cavee Verte': 'Stade de la Cavée verte',
    'Stade Cavee Verte': 'Stade de la Cavée verte',
    'Fort Carree': 'Stade du Fort Carré',
    'Stade du Fort Carre': 'Stade du Fort Carré',


    # Italy
    'Stadio San Siro': 'San Siro',
    'Stadio Nazionale PNF': 'Stadio Nazionale del PNF',
    'Stadio Benito Mussolini': 'Stadio Olimpico di Torino',
    'Stadio Giovanni Berta': 'Stadio Artemio Franchi',
    'Nazionale PNF': 'Stadio Nazionale del PNF',
    'Benito Mussolini': 'Stadio Olimpico di Torino',
    'Giorgio Ascarelli': 'Stadio Giorgio Ascarelli',
    'Stadio Ardenza': 'Stadio Armando Picchi',
    'Stadio Fuorigrotta': 'Stadio San Paolo',
    'Stadio Comunale': 'Stadio Artemio Franchi',
    'Comunale': 'Stadio Artemio Franchi',
    'Giovanni Berta': 'Stadio Artemio Franchi',
    'Marc Antonio Bentegodi': 'Stadio Marc\'Antonio Bentegodi',
    'Giuseppe Meazza': 'San Siro',
    'Stadio Delle Alpi': 'Stadio delle Alpi',
    'Sant Elia': 'Stadio Sant\'Elia',
    'Friuli': 'Stadio Friuli',
    'Stadio La Favorita': 'Stadio Renzo Barbera',
    'Renato Dall Ara': 'Stadio Renato Dall\'Ara',
    'Littorale': 'Stadio Renato Dall\'Ara',
    'Stadio Littoriale': 'Stadio Renato Dall\'Ara',
    'Stadio Renato Dall\'Aria': 'Stadio Renato Dall\'Ara',
    'Littorio': 'Stadio Littorio',
    'Stadio Littorio': 'Stadio Giuseppe Grezar',
    'Luigi Ferraris': 'Stadio Luigi Ferraris',

    # Spain
    'Balaidos': 'Balaídos',
    'Estadio Ramon Sanchez Pizjuan': 'Estadio Ramón Sánchez Pizjuán',
    'Chamartin Stadium': 'Estadio Chamartín',
    'Estadio Sarria': 'Estadi de Sarrià',
    'Estadio San Mames': 'Estadio San Mamés',
    'Estadio Ciudad de Mendoza': 'Estadio Malvinas Argentinas',
    'Vicente Calderon Stadium': 'Estadio Vicente Calderón',
    'Vicente Calderon': 'Estadio Vicente Calderón',
    'Estadio Vicente Calderon': 'Estadio Vicente Calderón',

    'Santiago Bernabeu': 'Estadio Santiago Bernabéu',
    'Santiago Bernabéu': 'Estadio Santiago Bernabéu',
    'Bernabeu Stadium': 'Estadio Santiago Bernabéu',
    'Estadio Santiago Bernabeu': 'Estadio Santiago Bernabéu',

    # Netherlands
    'Olympisch Stadion': 'Amsterdam Olympic Stadium',
    'PSV Stadium': 'Philips Stadion',

    # Portugal
    'Estadio da Luz': 'Estádio da Luz',
    'Estadio Do Dragao': 'Estádio do Dragão',

    # Venezuela
    'Estadio Pueblo Nuevo': 'Estadio Polideportivo de Pueblo Nuevo',
    'Estadio Jose Pachencho Romero': 'Estadio José Pachencho Romero',
    'Estadio Jose Panchencho Romero': 'Estadio José Pachencho Romero',
    'Estadio Jose Panchenco Romero': 'Estadio José Pachencho Romero',
    'Estadio Jose Pachenco Romero': 'Estadio José Pachencho Romero',
    'Estadio Metropolitano de Merida': 'Estadio Metropolitano de Mérida',
    'Estadio Olimpico de la UCV': 'Estadio Olímpico de la UCV',
    'Estadio Olimpico UCV': 'Estadio Olímpico de la UCV',
    'Estadio Olimpico (Caracas)': 'Estadio Olímpico de la UCV',
    'Estadio Polideportivo Cachamay': 'Polideportivo Cachamay',
    'Estadio Olimpico de Caracas': 'Estadio Olímpico de la UCV',
    'Estadio Olimpico Universitario (Caracas)': 'Estadio Olímpico de la UCV',
    'Estadio Universitario (Caracas)': 'Estadio Olímpico de la UCV',
    'Estadio Olimpico (Caracas FC)': 'Estadio Olímpico de la UCV',

    # China
    'Tuo Dong Stadium': 'Kunming Tuodong Sports Center',

    # Mexico
    'Estadio Alfonso Lastras Ramirez': 'Estadio Alfonso Lastras',
    'Estadio Nemesio Diez': 'Estadio Nemesio Díez',
    'Estadio Andres Quintana Roo': 'Estadio Quintana Roo',

    'Estadio Tecnologico': 'Estadio Tecnológico',
    'Stadium Tecnologico': 'Estadio Tecnológico',
    'Tecnologico': 'Estadio Tecnológico',

    'Estadío Jalisco': 'Estadio Jalisco',
    'Jalisco Stadium': 'Estadío Jalisco',

    'Estadio Olimpico Universitario': 'Estadio Olímpico Universitario',
    'Estadio Olimpico Universitario Mexico 68': 'Estadio Olímpico Universitario',
    'Estadio Olimpico de CU': 'Estadio Olímpico Universitario',
    'Estadio de la Ciudad Universitaria': 'Estadio Olímpico Universitario',
    'Estadio Monumental de la Ciudad Universitaria': 'Estadio Olímpico Universitario',
    'Estadio Monumental de Ciudad Universitaria': 'Estadio Olímpico Universitario',
    'Estadio Universitario (UANL)': 'Estadio Universitario de Monterrey',

    'Nuevo Estadio Corona': 'Estadio TSM Corona',


    'Estadio Victor Manuel Reyna': 'Estadio Víctor Manuel Reyna',
    'Estadio Nou Camp': 'Estadio León', 
    'La Corregidora': 'Estadio Corregidora',
    'Neza': 'Estadio Neza 86',

    'Azteca': 'Estadio Azteca',
    'Azteca Stadium': 'Estadio Azteca',
    'Jalisco': 'Estadio Jalisco',
    'Cuauhtemoc': 'Estadio Cuauhtémoc',
    'Estadío Cuauhtémoc': 'Estadio Cuauhtémoc',
    'Cuauhtemoc Stadium': 'Estadío Cuauhtémoc',
    'Estadio Cuauhtemoc': 'Estadio Cuauhtémoc',
    'Estadio de la Ciudad de los Deportes': 'Estadio Azul',
    'Estadio de la Ciudad de los Deportes, México DF': 'Estadio Azul',
    'Estadio Azulgrana': 'Estadio Azul',
    'Estadio de Riazor': 'Estadio Riazor',
    #'Estadio Jose Zorrilla': 'Estadio Nuevo José Zorrilla',
    'Estadio La Corregidora': 'Estadio Corregidora',
    'Estadio Luis Dosal': 'Estadio Nemesio Díez',
    'Estadio Luis Gutierrez Dosal': 'Estadio Nemesio Díez',
    'Estadio Luis Gutiérrez Dosal': 'Estadio Nemesio Díez',

    # South Korea
    'Sangam Stadium': 'Seoul World Cup Stadium',
    'Munsu Cup Stadium': 'Ulsan Munsu Football Stadium',

    # Japan
    'Yokohama International Stadium': 'International Stadium Yokohama',
    
    'Tokio National Stadium': 'Tokyo National Olympic Stadium',
    'Tokyo National Stadium': 'Tokyo National Olympic Stadium',
    'Tokyo Olympic Stadium': 'Tokyo National Olympic Stadium',
    'National Stadium (Tokyo)': 'Tokyo National Olympic Stadium',

    'Kashima Stadium': 'Kashima Soccer Stadium',
    'Niigata Stadium Big Swan': 'Tohoku Electric Power Big Swan Stadium',
    'Saitama Stadium': 'Saitama Stadium 2002',
    'Shizuoka Ecopa Stadium': 'Shizuoka Stadium',
    'Ecopa Stadium': 'Shizuoka Stadium',
    'Oita Stadium': 'Ōita Bank Dome',
    'Oita Big Eye Stadium': 'Ōita Bank Dome',
    'Kobe Wing Stadium': 'Home\'s Stadium Kobe',
    'Niigata Stadium': 'Tohoku Electric Power Big Swan Stadium',

    # Barbados
    'Waterford National Stadium': 'Barbados National Stadium',

    #Jamaica 
    'Kingston National Stadium': 'Jamaica National Stadium',
    #'Kasarani Stadium': 'Moi International Sports Centre',


    # Thailand
    'Supachalasai Stadium': 'Thailand National Stadium',

    # Austria
    'EM Stadiom Wals-Seizenheim': 'Red Bull Arena (Salzburg)',

    'Tivoli Neu': 'Tivoli-Neu',

    'Arnold Schwarzenegger Stadion': 'UPC-Arena',
    'Ernst-Happel Stadion': 'Ernst-Happel-Stadion',
    'Ernst Happel Stadium': 'Ernst-Happel-Stadion',

    # Germany
    'Fritz Walter Stadion': 'Fritz-Walter-Stadion',
    'Gottlieb-Daimler-Stadion': 'Mercedes-Benz Arena',
    'Neckarstadion': 'Mercedes-Benz Arena',
    'Frankfurt Waldstadion': 'Commerzbank-Arena',
    'Niedersachsenstadion': 'AWD-Arena',
    'Neckerstadion': 'Mercedes-Benz Arena',
    'Rhein-Energie Stadion': 'RheinEnergieStadion',
    'Franken-Stadion': 'Frankenstadion',
    'Hanover FIFA World Cup Stadium': 'AWD-Arena',
    'Zentralstadion': 'Red Bull Arena (Leipzig)',
    'AOL Arena': 'Volksparkstadion',
    'HSH Nordbank Arena': 'Volksparkstadion',

    # Puerto Rico
    'Estadio Juan Ramón Loubriel': 'Estadio Juan Ramon Loubriel',
    'Juan Ramon Loubriel Stadium': 'Estadio Juan Ramon Loubriel',
    'Juan Ramón Loubriel Stadium': 'Estadio Juan Ramon Loubriel',
    'Bayamon Soccer Complex': 'Bayamón Soccer Complex',
    'Bayamon FC Soccer Complex': 'Bayamon Soccer Complex',

    # Uruguay
    'Centenario': 'Estadio Centenario',
    'Estadio Centenario': 'Estadío Centenario',

    'Centenario Stadium': 'Estadio Centenario',
    'Estadio Jardines del Hipodromo': 'Estadio Jardines Del Hipódromo',
    'Estadio Jardines Del Hipodromo': 'Estadio Jardines Del Hipódromo',
    'Estadio Gran Parque Central': 'Parque Central',
    'Estadío Parque Central': 'Parque Central',
    'Estadio Parque Central': 'Parque Central',
    'Gran Parque Central': 'Parque Central',

    # Belize
    'FFB Field': 'FFB Stadium',

    # Australia
    'Latrobe City Stadium': 'LaTrobe City Stadium',
    'WIN Jubilee Oval': 'Jubilee Oval',
    'Patersons Stadium': 'Subiaco Oval',
    'Allianz Stadium': 'Sydney Football Stadium',
    'Hunter Stadium': 'Newcastle International Sports Centre',
    'Ausgrid Stadium': 'Newcastle International Sports Centre',
    'AAMI Park': 'Melbourne Rectangular Stadium',
    'Bluetongue Stadium': 'Central Coast Stadium',
    'Skilled Park': 'Robina Stadium',
    'Dairy Farmers Stadium': 'Willows Sports Complex',
    'Melbourne Etihad Stadium': 'Docklands Stadium',
    'Telstra Dome': 'Docklands Stadium',
    'nib Stadium': 'Perth Oval',
    'Members Equity Stadium': 'Perth Oval',
    'ME Bank Stadium': 'Perth Oval',
    'Aussie Stadium': 'Sydney Football Stadium',
    'EnergyAustralia Stadium': 'Newcastle International Sports Centre',
    'Lang Park': 'Suncorp Stadium',

    'Bruce Stadium': 'Canberra Stadium',
    'Aurora Stadium': 'York Park',

    # UAE
    'Al-Nuhayyan Stadium': 'Al Nahyan Stadium',

    # Panama
    'Estadio Agustin Muquita Sanchez': 'Estadio Agustín Sánchez',
    'Estadio Agustin Sanchez': 'Estadio Agustín Sánchez',
    'Estadio Armando Dely Valdes': 'Estadio Armando Dely Valdés',

    'Estadio Rommel Fernandez': 'Estadio Rommel Fernández',

    # Switzerland
    'Stadium Espenmoos': 'Espenmoos',
    'Hardturm Stadium': 'Hardturm',
    'St. Jakob Stadium': 'St. Jakob-Park',

    # Scotland
    'Easter Road Stadium': 'Easter Road',
    'Ibrox': 'Ibrox Stadium',

    # Libya
    'Libya National Stadium': 'June 11 Stadium',

    # Finland
    'Pallokenttä': 'Töölön Pallokenttä',
    'Ratina Stadium': 'Tampere Stadium',

    # Czech Republic
    'Na Stinadlech': 'Na Stínadlech',

    # South Africa
    'ABSA Stadium': 'Kings Park Stadium',
    'Durban Stadium': 'Moses Mabhida Stadium',

    # Estonia
    'A. Le Coq Stadium': 'A. Le Coq Arena',

    # Ukraine
    'Valeriy Lobanovskyi Stadium': 'Valeriy Lobanovskyi Dynamo Stadium',

    # Turkey
    'Antalya Ataturk Stadyumu': 'Antalya Atatürk Stadium',

    # Qatar
    'Khalifa Stadium': 'Khalifa International Stadium',

    # Sweden
    'Rasunda Stadium': 'Råsunda Stadium',
    'Rasunda': 'Råsunda Stadium',
    'Jarnvallen': 'Jernvallen',
    'Nya Ullevi': 'Ullevi',

    'Orjans Vall': 'Örjans Vall',
    'Behrn Arena': 'Eyravallen',
    'Malmo Stadion': 'Malmö Stadion',

    # Chile
    'Estadio Nacional Julio Martinez Pradanos': 'Estadio Nacional Julio Martínez Prádanos',
    'Estadio Nacional Julio Martinez Pradanos': 'Estadio Nacional Julio Martínez Prádanos',

    # Argentina
    'Estadio Brigadier Estanislao Lopez': 'Estadio Brigadier General Estanislao López',
    
    'Dr. José Luis Meiszner': 'Estadio Centenario Dr. José Luis Meiszner',
    'Estadio Jose Luis Meiszner': 'Estadio Centenario Dr. José Luis Meiszner',
    'Estadio Centenario (Quilmes)': 'Estadio Centenario Dr. José Luis Meiszner',
    'La Doble Visera': 'Estadio Libertadores de América',
    'Estadio Libertadores de America': 'Estadio Libertadores de América',
    'El Cilindro': 'Estadio Presidente Juan Domingo Perón',
    'Estadio Juan Domingo Peron': 'Estadio Presidente Juan Domingo Perón',
    'Estadio Presidente Juan Domingo Peron': 'Estadio Presidente Juan Domingo Perón',

    'Antonio Vespucio Liberti': 'Estadio Monumental Antonio Vespucio Liberti',
    'Estadio Monumental Nunez': 'Estadio Monumental Antonio Vespucio Liberti',
    'El Monumental': 'Estadio Monumental Antonio Vespucio Liberti',
    'Estadio Monumental Antonio Vespuci Liberti': 'Estadio Monumental Antonio Vespucio Liberti',
    'Estadio Antonio V. Liberti': 'Estadio Monumental Antonio Vespucio Liberti',
    'River Plate Stadium': 'Estadio Monumental Antonio Vespucio Liberti',
    'Estadio Monumental de Nunez': 'Estadio Monumental Antonio Vespucio Liberti',
    'Estadio Presidente Juan Domingo Peron': 'Estadio Presidente Juan Domingo Perón',
    'Estadio Juan Domingo': 'Estadio Presidente Juan Domingo Perón',
    'Palacio Duco': 'Estadio Tomás Adolfo Ducó',
    'La Bombonera': 'Estadio Alberto J. Armando',
    'Estadio La Bombonera': 'Estadio Alberto J. Armando',
    
    'Néstor Díaz Pérez': 'Estadio Ciudad de Lanús',
    'Estadio Ciudad de Lanus': 'Estadio Ciudad de Lanús',



    # Bolivia
    'Estadio Victor Agustin Ugarte': 'Estadio Víctor Agustín Ugarte',

    # Paraguay
    'General Pablo Rojas': 'Estadio General Pablo Rojas',
    'Estadio Defensores Del Chaco': 'Estadio Defensores del Chaco',
    'Defensores del Chaco': 'Estadio Defensores del Chaco',
    'Estadio de los Defensores del Chaco': 'Estadio Defensores del Chaco',

    # Ecuador
    'Estadio La Casa Blanca': 'Estadio de Liga Deportiva Universitaria',
    'Estadio de LDU': 'Estadio de Liga Deportiva Universitaria',
    

    # Peru
    'Estadio Garcilaso de la Vega': 'Estadio Garcilaso',
    'Estadio San Martin de Porres': 'Estadio Alberto Gallardo',
    'Estadio Nacional (Lima)': 'Estadio Nacional de Peru',
    'Estadio Nacional (Peru)': 'Estadio Nacional de Peru',
    'Estadio Monumental U': 'Estadio Monumental "U"',

    # Bolivia
    'Estadío Ramón Aguilera': 'Estadio Ramón Tahuichi Aguilera',
    'Estadio Ramon Tahuichi Aguilera': 'Estadio Ramón Tahuichi Aguilera',

    # Costa Rica
    'Estadio Alejandro Morera Soto': 'Estadío Alejandro Morera Soto',
    'Estadio Ricardo Saprisa': 'Estadio Ricardo Saprissa', 
    'Estadio Ricardo Saprissa Aymá': 'Estadio Ricardo Saprissa',
    'Estadio Saprissa': 'Estadio Ricardo Saprissa',

    # Canada
    'Centre Claude-Robillard': 'Complexe Sportif Claude-Robillard',
    'Claude Robillard Sports Complex': 'Complexe Sportif Claude-Robillard',
    'McMaster Stadium': 'Ron Joyce Stadium',

    'BC Place Stadium': 'BC Place',
    'Montreal Stade Saputo': 'Stade Saputo',
    'Stade Saputo': 'Saputo Stadium',

    # Guatemala
    'Mateo Flores Stadium': 'Estadio Mateo Flores',
    'Estadio Nacional Mateo Flores': 'Estadio Mateo Flores',
    'Estadio Mateo Flores': 'Estadío Mateo Flores',
}

united_states = {

    'Cardinal Park Stadium': 'Cardinal Stadium (Louisville)',
    'Cardinal Park Soccer and Track Stadium': 'Cardinal Stadium (Louisville)',
    'ODU Soccer Complex': 'Old Dominion Soccer Complex',

    # United States
    'Bank One Ballpark': 'Chase Field',
    'NSC Stadium': 'National Sports Center Stadium',
    'JFK Stadium': 'John F. Kennedy Stadium',
    'Eagle State Street Grounds': 'Eagle Street Grounds',
    'East State St Grounds': 'East State Street Grounds',
    'Hermann Stadium': 'Robert R. Hermann Stadium',
    'Kezar Field': 'Kezar Stadium',
    'Casa Grande Soccer Complex': 'Grande Sports World',
    'Premier Sports Campus at Lakewood Ranch': 'Premier Sports Campus',
    'Hal Sherbeck Field House': 'Sherbeck Field',
    'Hal Sherbeck Field': 'Sherbeck Field',
    'Ultimate Soccer Arena': 'Ultimate Soccer Arenas',
    'Collins Perley Sports Complex': 'Collins Perley Sports Center',
    'Molson Stadium': 'Percival Molson Memorial Stadium',
    'Albert/Daly Stadium': 'Albert-Daly Field',
    'Cara McGrane Stadium': 'Cara McGrane Memorial Stadium',
    'Calder Stadium': 'Nathan Calder Stadium',
    #'Cardinal Stadium': 'Benedetti–Wehrli Stadium',
    'UBC Thunderbird Stadium': 'Thunderbird Stadium',
    'Balboa Park Stadium': 'Boxer Stadium',
    'UBC Thunderbird Stadium': 'Thunderbird Stadium',
    'Montclair St. University': 'Montclair State University',
    'Foothills Park': 'Foothills Stadium',
    'Hanson Park': 'Hanson Stadium',
    'Tony Glavin Complex': 'Tony Glavin Soccer Complex',
    'Crescent Grounds': 'Crescent Athletic Club Grounds',
    'Staten Island Cricket Club Grounds': 'Staten Island Cricket Grounds',
    'Macomb\'s Dam Park': 'Macombs Dam Park',
    'RSL Training Field': 'America First Field',
    #'Kino Veterans Memorial Stadium': 'Kino Veterans Memorial Stadium',
    'Kino Sports Complex': 'Kino Veterans Memorial Stadium',
    'A.J. Siemon Stadium': 'A.J. Simeon Stadium',
    'Lehigh Stadium': 'Taylor Field',
    'Legion Sports Complex': 'Legion Stadium',
    'Krenzler Stadium': 'Krenzler Field',
    'Belson Stadium (St. John\'s University)': 'Belson Stadium',
    'Citibank Park': 'Bethpage Ballpark',
    'Stony Brook University Stadium': 'Kenneth P. LaValle Stadium',
    'Peter Johansen Stadium': 'Peter Johansen High School Stadium',
    'Collins-Perley Sports Complex': 'Collins Perley Sports Center',
    'Consol Energy Park': 'Falconi Field',
    'North Ends Field': 'North Ends Grounds',
    'Wanderers Park': 'Wanderers Grounds',
    'East End Grounds': 'East End Park',
    'Visitation Oval': 'Visitation Park',
    'Harlem Field': 'Harlem Oval',
    'Walsh Stadium': 'Walsh Memorial Stadium',
    'Aquinas Stadium': 'Holleder Memorial Stadium',
    'Edinboro University Stadium': 'Sox Harrison Stadium',
    'Middlefield Cheese Stadium (Bedford)': 'Middlefield Cheese Stadium',
    'Richard Montgomery HS': 'Richard Montgomery High School',
    'Legion Stadium': 'Buck Hardee Field at Legion Stadium',
    'Paul Angelo Russo Stadium Field': 'Paul Angelo Russo Stadium',
    'Carl Lewis Field': 'Carl Lewis Track & Field Stadium',
    'Centennial Stadium': 'Centennial Park Stadium',
    'P & C Stadium': 'Alliance Bank Stadium',
    'Uihlein Park': 'Uihlein Soccer Park',
    'Kuntz Memorial Stadium': 'Kuntz Stadium',
    'The Polo Grounds': 'Polo Grounds',
    'Capitoline Lake': 'Capitoline Grounds',
    'Sparta Stadium': 'Sparta Field',
    'Blue Valley Athletic Complex': 'Blue Valley Sports Complex',
    'Chartiers Valley High School': 'Chartiers Valley Stadium',
    'Tacony Baseball Park': 'Tacony Baseball Grounds',

    'National Sports Center': 'National Sports Center Stadium',
    'Husky Soccer Field': 'Husky Soccer Stadium',

    # Michigan
    'Pontiac Silverdome': 'Silverdome',

    # Kansas

    'Sporting Park': 'Sporting Kansas City Park',
    'Sporting Park (Kansas City)': 'Sporting Kansas City Park',
    'Livestrong Sporting Park': 'Sporting Kansas City Park',

    'Community America Ballpark': 'CommunityAmerica Ballpark',

    # Nevada
    'Las Vegas Stadium': 'Sam Boyd Stadium',

    # Minnesota
    'Hubert H. Humphrey Metrodome': 'Metrodome',

    # Georgia
    'RE/MAX Greater Atlanta Stadium': 'Atlanta Silverbacks Park',
    'Silverbacks Stadium': 'Atlanta Silverbacks Park',
    'Atlanta Stadium': 'Atlanta-Fulton County Stadium',
    'Atlanta Fulton County Stadium': 'Atlanta-Fulton County Stadium',
    'Silverbacks Park': 'Atlanta Silverbacks Park',

    # North Carolina

    'Queens Sports Complex': 'Queens University Stadium',

    'SAS Stadium': 'WakeMed Soccer Park',
    'SAS Soccer Park': 'WakeMed Soccer Park',
    'Wakemed Soccer Park': 'WakeMed Soccer Park',

    # Colorado
    'DSG Park': 'Dick\'s Sporting Goods Park',
    'Sports Authority Field': 'Sports Authority Field at Mile High',
    'Invesco Field': 'Sports Authority Field at Mile High',
    'INVESCO Field': 'Sports Authority Field at Mile High',

    # Rhode Island
    'Marks Stadium': 'Mark\'s Stadium',
    'Coats Field': 'Coates Field',

    # Ohio
    'Crew Stadium': 'Columbus Crew Stadium',

    'Beaver Creek High School': 'Dayton Outpatient Center Stadium',
    'Beavercreek High School': 'Dayton Outpatient Center Stadium',
    'DOC Stadium': 'Dayton Outpatient Center Stadium',

    # Oregon
    'JELD-WEN Field': 'Jeld-Wen Field',
    'PGE Park': 'JELD-WEN Field',
    'Portland Civic Stadium': 'Jeld-Wen Field',
    'Civic Stadium': 'Jeld-Wen Field', # There's another Civic Stadium in Eugene, OR; this is way over.
    'JELD-WEN Park': 'Jeld-Wen Field',
    'Jeld-Wen Field': 'Providence Park',
    
    # Tennessee
    'Nashville Coliseum': 'LP Field',

    # Florida

    'ESPN Wide World of Sports': 'ESPN Wide World of Sports Complex',
    'Florida Citrus Bowl': 'Citrus Bowl',
    'Orange Bowl': 'Miami Orange Bowl',
    'Alltel Stadium': 'EverBank Field',
    'Al Lang Stadium': 'Progress Energy Park',
    'Al Lang Field': 'Progress Energy Park',

    # Missouri
    'The Anheuser Busch Soccer Park': 'Anheuser-Busch Soccer Park',
    'Big Arch Stadium': 'Busch Memorial Stadium',

    # Maryland
    'Maryland Soccerplex Stadium': 'Maryland SoccerPlex',
    'Maryland Soccerplex': 'Maryland SoccerPlex',
    'Maryland Soccer Plex': 'Maryland SoccerPlex',

    # Oklahoma
    'Skelly Field': 'Skelly Field at H. A. Chapman Stadium',
    'Skelly Stadium': 'Skelly Field at H. A. Chapman Stadium',
    'Chapman Stadium': 'Skelly Field at H. A. Chapman Stadium',

    # Washington DC
    'Robert F. Kennedy Stadium': 'Robert F. Kennedy Memorial Stadium',
    'RFK Stadium': 'Robert F. Kennedy Memorial Stadium',
    'RFK Memorial Stadium': 'Robert F. Kennedy Memorial Stadium',
    'Robert F. Kennedy Stadium': 'Robert F. Kennedy Memorial Stadium',
    'R.F.K. Stadium': 'Robert F. Kennedy Memorial Stadium',
    'Robert F. Kennedy Memorial': 'Robert F. Kennedy Memorial Stadium',

    # California

    'Cagan Stadium': 'Laird Q. Cagan Stadium',

    'Hughes Stadium': 'Charles C. Hughes Stadium',
    'Anteater Stadium at UCI': 'Anteater Stadium',

    'Rancho La Cienega Stadium': 'Rancho La Cienga Stadium',
    'Cal State Fullerton Titan Stadium': 'Titan Stadium',
    'Fullerton Stadium': 'Titan Stadium',

    'Oakland-Alameda County Coliseum': 'Oakland Coliseum',
    'San Diego Stadium': 'Qualcomm Stadium',
    'Home Depot Center Track': 'Home Depot Center Track & Field Stadium',
    'San Diego Sports Arena': 'Valley View Casino Center',
    #'Los Angeles Memorial Coliseum': 'Memorial Coliseum (Los Angeles)',
    'Los Angeles Coliseum': 'Los Angeles Memorial Coliseum',
    'Los Angeles Memorial Stadium': 'Los Angeles Memorial Coliseum',
    'The Home Depot Center': 'Home Depot Center',
    'Jack Murphy Stadium': 'Qualcomm Stadium',

    # Connecticut
    'Willow Memorial Park Stadium': 'New Britain Veterans Stadium',
    'Willowbrook Memorial Park': 'New Britain Veterans Stadium',

    # Indiana
    'Invaders Complex': 'Indiana Invaders Soccer Complex',

    # New York


    'Thrift Field': 'Thrift Oval',

    'Todd\'s Field': 'Todd Field',
    'Lenox Field': 'Lenox Oval', # caledonian grounds?

    'New York Indiana Oval': 'New York Oval',
    'Indiana-New York Oval': 'New York Oval',

    '110th & 8th Ave Park': '110th and 8th Ave Park',
    'Ridgewood Baseball Park': 'Ridgewood Baseball Grounds',

    'PAETEC Park': 'Sahlen\'s Stadium',
    'PAETEC Park': 'Sahlen\'s Stadium',
    'Marina Auto Stadium': 'Sahlen\'s Stadium',
    'Marina Auto Stadium, Rochester, NY': 'Sahlen\'s Stadium',
    'Rochester Rhinos Stadium': 'Sahlen\'s Stadium',

    'Yankee Stadium': 'Yankees Stadium',

    'Triborough Stadium': 'Downing Stadium',
    'Randall\'s Island Stadium': 'Downing Stadium',
    'Randall\s Island Stadium': 'Downing Stadium',
    'Randall\s Island': 'Downing Stadium',

    # Illinois

    'Winnemac Park Stadium': 'Winnemac Park',

    # Pennsylvania

    # 'Yellow Jacket Stadium': 'Frankford Stadium', multiple Yellow Jacket Stadiums existed.
    'Cambria Stadium': 'Cambria Field',

    'Phillies Park': 'Baker Bowl',
    'Phillies Ball Park': 'Baker Bowl',

    'City Island Stadium': 'Skyline Sports Complex',
    'Philadelphia Municipal Stadium':  'John F. Kennedy Stadium',
    'Fedex Field': 'FedEx Field',
    'Tacony Ball Park': 'Tacony Baseball Grounds',
    'Bethlehem Steel Field': 'Steel Field',

    # Texas    
    'Soccorro Stadium': 'SISD Student Activities Complex',
    'Socorro Stadium': 'SISD Student Activities Complex',
    

    'Texas A&M Intl Univ Soccer Complex': 'TAMIU Soccer Complex',
    'WoodForest Stadium': 'Woodforest Bank Stadium',
    'Sun Bowl (UTEP)': 'Sun Bowl Stadium',
    'Dal-Hi Stadium': 'P.C. Cobb Stadium',
    'Fair Park Stadium': 'Cotton Bowl',
    'Gardner Park': 'Burnett Field',
    'Old Panther Stadium, Duncanville': 'Old Panther Field, Duncanville',
    'adidas Field at Pizza Hut Park': 'adidas Field',
    'Pizza Hut Park': 'FC Dallas Stadium',

    # Washington
    'Memorial Stadium (Seattle)': 'Seattle Memorial Stadium',
    'Seahawk Stadium': 'CenturyLink Field',

    'Starfire Sports Stadium': 'Starfire Sports Complex',
    'Starfire Complex': 'Starfire Sports Complex',
    'Starfire Stadium': 'Starfire Sports Complex',

    'Seahawks Stadium': 'CenturyLink Field',
    'Qwest Field': 'CenturyLink Field',

    # Massachusetts
    'Schaefer Stadium': 'Foxboro Stadium',
    'Sullivan Stadium': 'Foxboro Stadium',
    'Soldiers Field': 'Harvard Stadium',
    'Soldier\'s Field': 'Harvard Stadium',

    # New Jersey

    'Ironbound Park': 'Ironbound Field',

    'Lubetkin Field @ NJIT': 'Lubetkin Field',
    'ONT AA Grounds': 'Clark ONT Field',
    'Clark Field': 'Clark ONT Field',
    'Clark\'s Field': 'Clark ONT Field',


    'New Meadowlands Stadium': 'Giants Stadium', # Huh?
    'Freulinghausen Ave Grounds': 'Frelinghuysen Grounds',
    'Yurcak Field Stadium': 'Yurcak Field',
    'Rutgers Stadium': 'High Point Solutions Stadium',
    'ONT Grounds': 'Clark Field',
    'Clark\'s Athletic Field': 'Clark Field',
    'Frelinghuysen Avenue Grounds': 'Frelinghuysen Grounds',
    'Frelinghuysen Avenue Ground': 'Frelinghuysen Grounds',
    'Clark\'s Athletic Field': 'Clark\'s Field',

    'Colombus Crew Staduim': 'Columbus Crew Stadium',
    'Río Tinto Stadium':        'Rio Tinto Stadium',
    'Rio Tinto Satadium': 'Rio Tinto Stadium',
    'AT&T; Park': 'AT&T Park',
    'LIVESTRONG Sporting Park': 'Livestrong Sporting Park',

    'Olímpico Universitario': 'Estadio Olímpico Universitario',
    'Tecnológico': 'Estadio Tecnológico',
    'Jorge Calero Suárez': 'Estadio Jorge Calero Suárez',
    'Nacional Tiburcio Carías Andino': 'Estadio Tiburcio Carías Andino',
    'Juan Ramón Loubriel': 'Estadio Juan Ramon Loubriel',
    'Saputo': 'Saputo Stadium',
    'Marvin Lee': 'Marvin Lee Stadium',
    'Estadio Corona': 'Estadio TSM Corona',
    'Hasely Crawford': 'Hasely Crawford Stadium',
    'Andrés Quintana Roo': 'Estadio Quintana Roo',
    'Complexe sportif Claude-Robillard': 'Complexe Sportif Claude-Robillard',

}

sd.update(misc)
sd.update(world)
sd.update(united_states)

    
