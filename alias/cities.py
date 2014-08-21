#!/usr/local/bin/env python
# -*- coding: utf-8 -*-




def get_city(s):

    s = s.strip()
    if s in cities:
        return get_city(cities[s])
    else:
        return s
    



cities = {

    # Honduras
    'Puerto Cortes, Honduras': 'Puerto Cortés, Honduras',
    'Tegucigalpa': 'Tegucigalpa, Honduras',
    'San Pedro Sula': 'San Pedro Sula, Honduras',

    # Saint Vincent and the Grenadines
    'Layou, StVincent&amp;Grenadines': 'Layou, St. Vincent and Grenadines',

    # El Salvador
    'Chaletenango, El Salvador': 'Chalatenango, El Salvador',
    'Metapan, El Salvador': 'Metapán, El Salvador',

    # Panama

    'Colon, Panama': 'Colón, Panama',

    'Cd Panama, Panama': 'Ciudad de Panamá, Panama',
    'Ciudad de Panama, Panama': 'Ciudad de Panamá, Panama',
    #'Ciudad de Panamá, Panama': 'Panama City, Panama',
    'Panama City, Panama': 'Ciudad de Panamá, Panama',

     # Nicaragua
    'Esteli, Nicaragua': 'Estelí, Nicaragua',


    # Trinidad and Tobago
    'Point Fortin, Trinidad & Tobago': 'Point-Fortin, Trinidad & Tobago',
    'Port-of-Spain, Trinidad & Tobago': 'Port of Spain, Trinidad and Tobago',
    'Port of Spain, Trinidad & Tobago': 'Port of Spain, Trinidad and Tobago',
    'Port of Spain, Trinidad': 'Port of Spain, Trinidad and Tobago',
    'Port of Spain': 'Port of Spain, Trinidad and Tobago',

    # Curacao
    'Bandabou, Curacao': 'Bándabou, Curacao',

    # Costa Rica

    'San Jose, Costa Rica': 'San José, Costa Rica',

    # Haiti
    'Leogane, Haiti': 'Léogâne, Haiti',
    'Port au Prince, Haiti': 'Port-au-Prince, Haiti',
    'Port-au-Prince': 'Port-au-Prince, Haiti',

    # Martinique
    'Rivière-Pilote, Martinique': 'Rivière-Pilote, Martinique,',
    'La Trinite, Martinique': 'La Trinité, Martinique',
    'Fort de France, Martinique': 'Fort-de-France, Martinique',

    # Cuba
    'Havana': 'Havana, Cuba',
    'La Habana': 'Havana, Cuba',

    # Suriname
    'Paramaribo': 'Paramaribo, Suriname',

    # Antigua
    'Antigua': 'Antigua, Antigua and Barbuda',

    # Puerto Rico
    'San Juan, PR': 'San Juan, Puerto Rico',

    'Bayamon, PR': 'Bayamón, Puerto Rico',
    'Bayamón, PR': 'Bayamón, Puerto Rico',
    'Bayamon, Puerto Rico': 'Bayamón, Puerto Rico',

    # Mexico

    #'León, Mexico': 'León, México',
    'Leon, Mexico': 'León, Mexico',

    'Ciudad Juarez, Mexico': 'Ciudad Juárez, Mexico',
    'Tuxtla Gutierrez, Mexico': 'Tuxtla Gutiérrez, Mexico',

    'Queretaro, Mexico': 'Querétaro, Mexico',
    'Queretaro': 'Querétaro, Mexico',
    'Querétaro': 'Querétaro, Mexico',

    'Cancun, Mexico': 'Cancún, Mexico',
    'Culiacan, Mexico': 'Culiacán, Mexico',
    'San Luis Potosi, Mexico': 'San Luis Potosí, Mexico',

    'México City, Mexico': 'Mexico City, Mexico',
    'San Luis Potosi, Mexico': 'San Luis Potosí, Mexico',
    'Leon, Mexico': 'León, Mexico',
    'Mexico City, MX': 'Mexico City, Mexico',
    'Mexico City': 'Mexico City, Mexico',
    'Ciudad de México': 'Mexico City, Mexico',
    'Ciudad de México': 'Mexico City, Mexico',
    'Guadalajara': 'Guadalajara, Mexico',

    # Guatemala
    'Ciudad de Guatemala': 'Guatemala City, Guatemala',
    'Ciudad de Guatemala, Guatemala': 'Guatemala City, Guatemala',
    'Guatemala City': 'Guatemala City, Guatemala',


    # CONMEBOL


    # Chile
    'Concepcion, Chile': 'Concepción, Chile',
    'Vina del Mar, Chile': 'Viña del Mar, Chile',
    'Vina del Mar, Chile': 'Viña del Mar, Chile',
    'Concepcion, Chile': 'Concepción, Chile',
    'Valparaiso, Chile': 'Valparaíso, Chile',


    # Ecuador
    'Quito': 'Quito, Ecuador',


    # Venezuela
    'San Cristobal, Venezuela': 'San Cristóbal, Venezuela',
    'Merida, Venezuela': 'Mérida, Venezuela',
    'Maturin, Venezuela': 'Maturín, Venezuela',
    'San Cristobal, Venezuela': 'San Cristóbal, Venezuela',
    'Merida, Venezuela': 'Mérida, Venezuela',
    'Caracas': 'Caracas, Venezuela',

    # Colombia
    'Cucuta, Colombia': 'Cúcuta, Colombia',

    'Bogota, Colombia': 'Bogotá, Colombia',
    'Medellin, Colombia': 'Medellín, Colombia',
    'Medellin, Colombia': 'Medellín, Colombia',
    'Ibague, Colombia': 'Ibagué, Colombia',
    'Acandi, Colombia': 'Acandí, Colombia',
    'Bogota, Colombia': 'Bogotá, Colombia',
    'Bogota': 'Bogota, Colombia',
    'Medellin, Colombia': 'Medellín, Colombia',

    # Argentina
    'San Martin, Argentina': 'San Martín, Argentina',
    'Mar Del Plata, Argentina': 'Mar del Plata, Argentina', 
    'Cordoba, Argentina': 'Córdoba, Argentina',
    'San Martin, Argentina': 'San Martín, Argentina', # real city?
    'Mar Del Plata, Argentina': 'Mar del Plata, Argentina',
    'Cordoba, Argentina': 'Córdoba, Argentina',

    # Paraguay
    'Asuncion, Paraguay': 'Asunción, Paraguay',
    'Asuncion, Paraguay': 'Asunción, Paraguay',


    # Brazil

    'Santo Andre, Brazil': 'Santo André, Brazil',
    'Rio de Janeiro, Brazil': 'Río de Janeiro, Brazil',
    'Rio de Janeiro, Brazil': 'Río de Janeiro, Brazil',
    'Goiania, Brazil': 'Goiânia, Brazil',

    'Rio De Janeiro, Brazil': 'Rio de Janeiro, Brazil',
    'Rio de Janeiro': 'Rio de Janeiro, Brazil',
    'Curitiba': 'Curitiba, Brazil',
    'Belo Horizonte': 'Belo Horizonte, Brazil',
    'Recife': 'Recife, Brazil',
    'Rio De Janeiro, Brazil': 'Rio de Janeiro, Brazil',
    'Mogi Mirim, Brazil': 'Mogi-Mirim, Brazil',

    'Sao Paulo': 'São Paulo, Brazil',
    'São Paulo': 'São Paulo, Brazil',
    'Sao Paulo, Brazil': 'São Paulo, Brazil',
    'Sao Caetano do Sul, Brazil': 'São Caetano do Sul, Brazil',

    'Santo Andre, Brazil': 'Santo André, Brazil',
    'Belem, Brazil': 'Belém, Brazil',
    'Goiania, Brazil': 'Goiânia, Brazil',
    'Brasilia, Brazil': 'Brasília, Brazil',
    'Sao Paulo, Brazil': 'São Paulo, Brazil',
    'Sao Luis, Brazil': 'São Luís, Brazil',
    'Sao Paulo, Brazil': 'São Paulo, Brazil',


    # CAF

    # Morocco
    'Marrakech': 'Marrakech, Morocco',

    # Egypt
    'Cairo': 'Cairo, Egypt',


    # Cameroon
    'Yaounde, Cameroon': 'Yaoundé, Cameroon',
    'Yaounde, Cameroon': 'Yaoundé, Cameroon',

    # UEFA

    # Poland
    'Krakow, Poland': 'Kraków, Poland',
    'Chorzow, Poland': 'Chorzów, Poland',
    'Chorzow, Poland': 'Chorzów, Poland',
    'Warsaw': 'Warsaw, Poland',


    # Switzerland
    'Zurich, Switzerland': 'Zürich, Switzerland',
    'Zurich, Switzerland': 'Zürich, Switzerland',

    # England
    'Newcastle-upon-Tyne, England': 'Newcastle upon Tyne, England',
    'London': 'London, England',

    # Germany
    'Dusseldorf, Germany': 'Düsseldorf, Germany',
    'Dusseldorf': 'Dusseldorf, Germany',
    'Frankfurt': 'Frankfurt, Germany',

    # Portugal
    'Setubal, Portugal': 'Setúbal, Portugal',



    # Ireland
    'Dublin Ireland': 'Dublin, Ireland',
    'Belfast': 'Belfast, Northern Ireland',
    'Dublin': 'Dublin, Ireland',

    # Uruguay
    'Paysandu, Uruguay': 'Paysandú, Uruguay',
    'Montevideo': 'Montevideo, Uruguay',


    # Serbia
    'Backa Topola, Serbia': 'Bačka Topola, Serbia',

    #Sweden

    'Vasteras, Sweden': 'Västerås, Sweden',

    'Goteborg, Sweden': 'Göteborg, Sweden',
    'Gothenburg': 'Gothenburg, Sweden',
    'Gothenborg': 'Gothenburg, Sweden',

    'Malmo, Sweden': 'Malmö, Sweden',
    'Malmo': 'Malmö, Sweden',

    'Norrkoping, Sweden': 'Norrköping, Sweden',
    'Norrkoping': 'Norrköping, Sweden',
    'Boras, Sweden': 'Borås, Sweden',
    'Boras': 'Borås, Sweden',

    'Stockholm': 'Stockholm, Sweden',
    'Gavle': 'Gävle, Sweden',
    'Helsinburg': 'Helsingborg, Sweden',
    'Helsinborg': 'Helsingborg, Sweden',


    # Norway
    'Kristiana, Norway': 'Oslo, Norway',

    # Denmark
    'Copenhagen': 'Copenhagen, Denmark',
    
    # Italy
    'Rome': 'Rome, Italy',
    'Florence': 'Florence, Italy',

    # France
    'Lyons, France': 'Lyon, France',
    'Nantes': 'Nantes, France',
    'Paris': 'Paris, France',

    #Scotland
    'Dunfermlime, Scotland': 'Dunfermline, Scotland',
    'Glasgow': 'Glasgow, Scotland',
    'Edinburgh': 'Edinburgh, Scotland',    

    # Iceland
    'Reykjavik': 'Reykjavik, Iceland',

    # Austria
    'Vienna': 'Vienna, Austria',

    # Slovenia
    'Ljubljana': 'Ljubljana, Slovenia',

    # Belgium
    'Brussels': 'Brussels, Belgium',

    # Netherlands
    'Amsterdam': 'Amsterdam, Netherlands',
    'Amsterdam, Holland': 'Amsterdam, Netherlands',
    'Breskens, Holland': 'Breskens, Netherlands',


    # Hungary
    'Budapest': 'Budapest, Hungary',


    # AFC

     #Saudi Arabia
    'Riyadh': 'Riyadh, Saudi Arabia',


    # Japan
    'Tokyo': 'Tokyo, Japan',

    # India
    'Calcutta': 'Calcutta, India',    

    # China
    'Hong Kong': 'Hong Kong, China',

    # Israel
    'Jerusalem': 'Jerusalem, Israel',

    # OFC

    # Australia
    'Adelaide': 'Adelaide, Australia',

    # Canada
    'Vancouver, B.C.': ' Vancouver, BC',
    'Montreal, QUE': 'Montreal, QC',
    'Montreal, Que': 'Montreal, QC',
    'Montreal, Quebec': 'Montreal, QC',
    'Montreal': 'Montreal, QC',
    'Montreal, Canada': 'Montreal, Quebec',
    'Monteal, PQ': 'Montreal, QC',

    'Quebec, Canada': 'Quebec',

    'Vancouver': 'Vancouver, BC',
    'Vancouver, B.C.': 'Vancouver, BC',

    'Hamilton, Ont': 'Hamilton, ON',

    'Ottawa': 'Ottawa, ON',
    'Ottawa, Canada': 'Ottawa, ON',

    'Calbary': 'Calgary, AB',
    'Calbary, Alb': 'Calgary, AB',

    'Edmonton': 'Edmonton, AB',

    'Toronto, Canada': 'Toronto, ON',

    'Victoria, B.C.': 'Victoria, BC',


    # United States
    'Randalls Island, NY': 'Randall\'s Island, NY', 

    'Newport Beach , California': 'Newport Beach, CA',

    'Kearny NJ': 'Kearny, New Jersey',
    'Kearny, N.J.': 'Kearny, New Jersey',

    'Manhattan, NY': 'New York, NY',
    'New York, N.Y.': 'New York, New York',

    'San José, California': 'San Jose, California',
    'San José, CA': 'San Jose, CA',

    'Washington DC': 'Washington D.C.',
    'Washington, DC': 'Washington D.C.',
    'Washington, D.C.': 'Washington D.C.',
    'Washington DC': 'Washington D.C.',
    'Los Ángeles, CA': 'Los Angeles, CA',

    'New Bedford': 'New Bedford, MA',
    'Pawtucket': 'Pawtucket, RI',
    'Providence': 'Providence, RI',

    'Cleveland': 'Cleveland, OH',
    'Toronto': 'Toronto, ON',
    'Worcester': 'Worcester, MA',
    'Winnipeg': 'Winnipeg, MB',
    'Detroit': 'Detroit, MI',
    'Bronx': 'Bronx, NY',
    'Kearny': 'Kearny, NJ',
    'Dallas': 'Dallas, TX',
    'Ft. Lauderdale': 'Fort Lauderdale, FL',


    'Milwaukee': 'Milwaukee, WI',

    'San Francisco': 'San Francisco, CA',


    'Houston': 'Houston, TX',
    'Jersey City, N.J.': 'Jersey City, NJ',
    'Los Angeles': 'Los Angeles, CA',

    'Minneapolis': 'Minneapolis, MN',

    'New Haven': 'New Haven, CT',

    
    'Miami': 'Miami, FL',
    'Denver': 'Denver, CO',
    'Boston': 'Boston, MA',
    'San Francisco': 'San Francisco, CA',
    'Tampa Bay': 'Tampa, FL',
    'Tampa Bay, FL': 'Tampa, FL',
    'San José, CA': 'San Jose, CA',
    'Fort Lauderdale': 'Fort Lauderdale, FL',
    'Fort Worth': 'Fort Worth, TX',
    'Anaheim': 'Anaheim, CA',
    'Philadelphia, Pa.': 'Philadelphia, PA',
    'Germantown, Pa.': 'Germantown, PA',
    'Brooklyn': 'Brooklyn, NY',
    'Philadelphia': 'Philadelphia, PA',
    'St. Louis': 'St. Louis, MO',
    'Seattle': 'Seattle, WA',
    'Chicago': 'Chicago, IL',
    'San Diego': 'San Diego, CA',
    'Tulsa': 'Tulsa, OK',
    'Rochester': 'Rochester, NY',
    'Cincinnati': 'Cincinnati, OH',
    'Trenton': 'Trenton, NJ',
    'Newark': 'Newark, NJ',
    'Baltimore': 'Baltimore, MD',
    'Toronto': 'Toronto, ON',
    'Jersey City': 'Jersey City, NJ',
    'Jersey City, N.J.': 'Jersey City, NJ',
    'Bethlehem': 'Bethlehem, PA',
    'Bayonne': 'Bayonne, NJ',
    'New York, New York': 'New York, NY',
    'New York': 'New York, NY',
    'New York City': 'New York, NY',
    'East Newark': 'East Newark, NJ',
    'Foxboro, MA': 'Foxborough, MA',
    'Oakland': 'Oakland, CA',
    'Pasadena': 'Pasadena, CA',
    'Las Vegas': 'Las Vegas, NV',
    'Newport Beach , CA': 'Newport Beach, CA',
    'Ft. Lauderdale, FL': 'Fort Lauderdale, FL',
    'Ft Lauderdale, FL': 'Fort Lauderdale, FL',
    'Washington, D.C.': 'Washington DC',


}
