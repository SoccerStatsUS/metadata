#!/usr/local/bin/env python
# -*- coding: utf-8 -*-



import datetime

l = [

    {
        'name': 'Saint Louis University',
        'city': 'St. Louis, MO',
        },

    {
        'name': 'Houston Baptist University',
        'city': 'Houston, TX',
        },

    {
        'name': 'San Jacinto College',
        'city': 'Pasadena, TX',
        },

    {
        'name': 'Roberts Wesleyan College',
        'city': 'Rochester, NY',
        },

    {
        'name': 'Vanier College',
        'city': 'Montreal, QC',
        },

    {
        'name': 'University of Maryland Baltimore County',
        'city': 'Baltimore, MD',
        },


    {
        'name': 'West Chester University of Pennsylvania',
        'city': 'West Chester, PA',
        },

    {
        'name': 'Wofford College',
        'city': 'Spartanburg, South Carolina',
        },

    {
        'name': 'Haverford College',
        'city': 'Haverford, PA',
        },

    {
        'name': 'Pratt Institute',
        'city': 'Brooklyn, NY',
        },

    {
        'name': 'Loyola University Chicago',
        'city': 'Chicago, IL',
        },    
    {
        'name': 'University of California Berkeley',
        'city': 'Berkeley, CA',
        },

    {
        'name': 'University of Massachusetts',
        'city': 'Amherst, MA',
        },

    {
        'name': 'University of North Carolina',
        'city': 'Chapel Hill, NC',
        },

    {
        'name': 'University of Virginia',
        'city': 'Charlottesville, VA',
        },


    {
        'name': 'UCLA', 
        'city': 'Los Angeles, CA',
        },

    {
        'name': 'Boston College',
        'city': 'Boston, MA',
        },

    {
        'name': 'University of San Diego',
        'city': 'San Diego, CA',
        },


    {
        'name': 'Florida International University',
        'city': 'Miami, FL',
        },

    {
        'name': 'University of Wisconsin',
        'city': 'Madison, WI',
        },

    {
        'name': 'Clemson University',
        'city': 'Clemson, SC',
        },

    {
        'name': 'Butler University',
        'city': 'Indianapolis, IN',
        },

    {
        'name': 'Indiana University-Purdue University Indianapolis',
        'city': 'Indianapolis, IN',
        },

    {
        'name': 'Rockhurst University',
        'city': 'Kansas City, MO',
        },

    {
        'name': 'College of William and Mary',
        'city': 'Williamsburg, VA',
        },

    {
        'name': 'Oakland University',
        'city': 'Rochester, MI',
        },

    {
        'name': 'Cornell University',
        'city': 'Ithaca, NY',
        },

    {
        'name': 'University of Pennsylvania',
        'city': 'Philadelphia, PA',
        },

    {
        'name': 'Rutgers University',
        'city': 'New Brunswick, NJ',
        },

    {
        'name': 'Park University',
        'city': 'Parkville, MO',
        },

    {
        'name': 'University of Rhode Island',
        'city': 'Kingston, RI',
        },

    {
        'name': 'University of Hartford',
        'city': 'West Hartford, CT',
        },


    {
        'name': 'Appalachian State University',
        'city': 'Boone, NC',
        },

    {
        'name': 'University of New England',
        'city': 'Biddeford, ME',
        },

    {
        'name': 'Vanderbilt University',
        'city': 'Nashville, TN',
        },

    {
        'name': 'Duquesne University',
        'city': 'Pittsburgh, PA',
        },


    {
        'name': 'Sacred Heart University',
        'city': 'Fairfield, CT',
        },

    {
        'name': 'Amherst College',
        'city': 'Amherst, MA',
        },

    {
        'name': 'Georgia Southern University',
        'city': 'Statesboro, GA',
        },

    {
        'name': 'Macalester College',
        'city': 'St. Paul, MN',
        },


    {
        'name': 'Southern Methodist University',
        'city': 'Dallas, TX',
        },

    {
        'name': 'East Stroudsburg University',
        'city': 'East Stroudsburg, PA',
        },

    {
        'name': 'University of San Francisco',
        'city': 'San Francisco, CA',
        },

    {
        'name': 'Northern Kentucky University',
        'city': 'Highland Heights, KY',
        },


    {
        'name': 'Midwestern State University',
        'city': 'Wichita Falls, TX',
        },

    {
        'name': 'Georgetown University',
        'city': 'Washington DC',
        },

    {
        'name': 'University of Maryland',
        'city': 'College Park, MD',
        },

    {
        'name': 'George Mason University',
        'city': 'Fairfax, VA',
        },


    {
        'name': 'University of South Carolina',
        'city': 'Columbia, SC',
        },

    {
        'name': 'North Carolina State University',
        'city': 'Raleigh, NC',
        },

    {
        'name': 'University of Portland',
        'city': 'Portland, OR',
        },

    {
        'name': 'Brown University',
        'city': 'Providence, RI',
        },

    {
        'name': 'University of Washington',
        'city': 'Seattle, WA',
        },

    {
        'name': 'University of Tampa',
        'city': 'Tampa, FL',
        },

    {
        'name': 'La Salle University',
        'city': 'Philadelphia, PA',
        },

    {
        'name': 'Azusa Pacific University',
        'city': 'Azusa, CA',
        },


    {
        'name': 'University of Connecticut',
        'city': 'Storrs, CT',
        },

    {
        'name': 'Fordham University',
        'city': 'New York, NY',
        },

    {
        'name': 'Lehigh University',
        'city': 'Bethlehem, PA',
        },

    {
        'name': 'James Madison University',
        'city': 'Harrisonburg, VA',
        },

    {
        'name': 'Stanford University',
        'city': 'Stanford, CA',
        },

    {
        'name': 'Lynn University',
        'city': 'Boca Raton, FL',
        },

    {
        'name': 'Wingate University',
        'city': 'Wingate, NC',
        },

    {
        'name': 'Dartmouth College',
        'city': 'New Hanover, NH',
        },

    {
        'name': 'Penn State',
        'city': 'College Park, PA',
        },

    {
        'name': 'University of Central Florida',
        'city': 'Orlando, FL',
        },

    {
        'name': 'Cleveland State University',
        'city': 'Cleveland, OH',
        },

    {
        'name': 'Syracuse University',
        'city': 'Syracuse, NY',
        },
    {
        'name': 'Adelphi University',
        'city': 'Garden City, NY',
        },

    {
        'name': 'University of Akron',
        'city': 'Akron, OH',
        },

    {
        'name': 'Yale University',
        'city': 'New Haven, CT',
        },

    {
        'name': 'Western Illinois University',
        'city': 'Macomb, IL',
        },
    {
        'name': 'Old Dominion University',
        'city': 'Norfolk, VA',
        },


    {
        'name': 'University of Texas at El Paso',
        'city': 'El Paso, TX',
        },

    {
        'name': 'University of Pittsburgh',
        'city': 'Pittsbugh, PA',
        },

    {
        'name': 'Belmont University',
        'city': 'Nashville, TN',
        },
    {
        'name': 'Houghton College',
        'city': 'Houghton, NY',
        },

    {
        'name': 'University of Tulsa',
        'city': 'Tulsa, OK',
        },

    {
        'name': 'University of Puget Sound',
        'city': 'Tacoma, WA',
        },

    {
        'name': 'Oregon State University',
        'city': 'Corvallis, OR',
        },

    {
        'name': 'Emory University',
        'city': 'Atlanta, GA',
        },

    {
        'name': 'Ohlone College',
        'city': 'Fremont, CA',
        },

    {
        'name': 'Georgia Perimeter College',
        'city': 'Atlanta, GA',
        },

    {
        'name': 'University of New Hampshire',
        'city': 'Durham, NH',
        },

    {
        'name': 'University of Buffalo',
        'city': 'Buffalo, NY',
        },


    {
        'name': 'Fairfield University',
        'city': 'Fairfield, CT',
        },

    {
        'name': 'Plattsburgh College',
        'city': 'Plattsburgh, NY',
        },

    {
        'name': 'Coastal Carolina University',
        'city': 'Conway, SC',
        },

    {
        'name': 'University of Alabama',
        'city': 'Tuscaloosa, AL',
        },

    {
        'name': 'Mercyhurst University',
        'city': 'Erie, PA',
        },

    {
        'name': 'UNC Charlotte',
        'city': 'Charlotte, NC',
        },


    {
        'name': 'Santa Clara University',
        'city': 'Santa Clara, CA',
        },

    {
        'name': 'California State University, Sacramento',
        'city': 'Sacramento, CA',
        },


    {
        'name': 'Duke University',
        'city': 'Durham, NC',
        },


    {
        'name': 'University of South Florida',
        'city': 'Tampa, FL',
        },

    {
        'name': 'Creighton University',
        'city': 'Omaha, NE',
        },

    {
        'name': 'Indiana University',
        'city': 'Bloomington, IN',
        },

    {
        'name': 'Rollins College',
        'city': 'Winter Park, FL',
        },

    {
        'name': 'Harvard University',
        'city': 'Cambridge, MA',
        },

    {
        'name': 'Alabama A&M University',
        'city': 'Normal, AL',
        },

    {
        'name': 'Southern Connecticut State University',
        'city': 'New Haven, CT',
        },

    {
        'name': 'Bowling Green State University',
        'city': 'Bowling Green, OH',
        },

    {
        'name': 'Robert Morris University',
        'city': 'Pittsburgh, PA',
        },

    {
        'name': 'California State University, Bakersfield',
        'city': 'Bakersfield, CA',
        },

    {
        'name': 'St. John\'s University',
        'city': 'Queens, NY',
        },

    {
        'name': 'Seattle University',
        'city': 'Seattle, WA',
        },

    {
        'name': 'Missouri State University',
        'city': 'Springfield, MO',
        },


    {
        'name': 'San Jose State University',
        'city': 'San Jose, CA',
        },

    {
        'name': 'San Diego State University',
        'city': 'San Diego, CA',
        },

    {
        'name': 'California State University, Fullerton',
        'city': 'Fullerton, CA',
        },

    {
        'name': 'University of Evansville',
        'city': 'Evansville, IN',
        },

    {
        'name': 'Murray State University',
        'city': 'Murray, KY',
        },

    {
        'name': 'Long Island University',
        'city': 'Brookville, NY',
        },

    {
        'name': 'University of North Texas',
        'city': 'Denton, TX',
        },

    {
        'name': 'Avila University',
        'city': 'Kansas City, MO',
        },

    {
        'name': 'Texas Tech University',
        'city': 'Lubbock, TX',
        },

    {
        'name': 'El Camino College',
        'city': 'Torrance, CA',
        },

    {
        'name': 'Eastern Illinois University',
        'city': 'Charleston, IL',
        },

    {
        'name': 'California State University, Chico',
        'city': 'Chico, CA',
        },


    {
        'name': 'Erskine University',
        'city': 'Due West, SC',
        },

    {
        'name': 'University of Missouri',
        'city': 'Columbia, MO',
        },

    {
        'name': 'Hartwick College',
        'city': 'Oneonta, NY',
        },

    {
        'name': 'University of Southern California',
        'city': 'Los Angeles, CA',
        },

    {
        'name': 'University of Vermont',
        'city': 'Burlington, VT',
        },


    {
        'name': 'University of Illinois at Springfield',
        'city': 'Springfield, IL',
        },

    {
        'name': 'Furman University',
        'city': 'Greenville, SC',
        },

    {
        'name': 'Spartanburg Methodist College',
        'city': 'Spartanburg, SC',
        },

    {
        'name': 'Marquette University',
        'city': 'Milwaukee, WI',
        },

    {
        'name': 'Monmouth University',
        'city': 'Long Branch, NJ',
        },
    {
        'name': 'Elon University',
        'city': 'Elon, NC',
        },

    {
        'name': 'Campbell University',
        'city': 'Buies Creek, NC',
        },

    {
        'name': 'Winthrop University',
        'city': 'Rock Hill, SC',
        },

    {
        'name': 'University of Kentucky',
        'city': 'Lexington, KY',
        },

    {
        'name': 'Gonzaga University',
        'city': 'Spokane, WA',
        },

    {
        'name': 'University of New Mexico',
        'city': 'Albuquerque, NM',
        },

    {
        'name': 'Fort Lewis College',
        'city': 'Durango, CO',
        },

    {
        'name': 'Mercer University',
        'city': 'Macon, GA',
        },

    {
        'name': 'Wichita State University',
        'city': 'Wichita, KS',
        },

    {
        'name': 'Regis University',
        'city': 'Denver, CO',
        },


    {
        'name': 'Montreat College',
        'city': 'Montreat, NC',
        },


    {
        'name': 'Oglethorpe University',
        'city': 'Atlanta, GA',
        },

    {
        'name': 'Piedmont College',
        'city': 'Demorest, GA',
        },

    {
        'name': 'DePaul University',
        'city': 'Chicago, IL',
        },



    {
        'name': 'University of Rochester',
        'city': 'Rochester, NY',
        },



    {
        'name': 'Queens University of Charlotte',
        'city': 'Charlotte, NC',
        },



    {
        'name': 'Fairleigh Dickinson University',
        'city': 'Teaneck, NJ',
        },


    {
        'name': 'Auburn University at Montgomery',
        'city': 'Montgomery, AL',
        },

    {
        'name': 'New Mexico State University',
        'city': 'Las Cruces, NM',
        },

    {
        'name': 'St. Olaf College',
        'city': 'Northfield, MN',
        },

    {
        'name': 'University of Mobile',
        'city': 'Mobile, AL',
        },

    {
        'name': 'Longwood University',
        'city': 'Farmville, VA',
        },

    {
        'name': 'Binghamton University',
        'city': 'Binghamton, NY',
        },

    {
        'name': 'Columbia University',
        'city': 'Columbia, NY',
        },

    {
        'name': 'University of Montevallo',
        'city': 'Montevallo, AL',
        },

    {
        'name': 'Stony Brook University',
        'city': 'Stony Brook, NY',
        },

    {
        'name': 'Colorado School of Mines',
        'city': 'Golden, CO',
        },

    {
        'name': 'Valparaiso University',
        'city': 'Valparaiso, IN',
        },


    {
        'name': 'Providence College',
        'city': 'Providence, RI',
        },


    {
        'name': 'Dowling College',
        'city': 'Oakdale, NY',
        },


    {
        'name': 'Hofstra University',
        'city': 'Hempstead, NY',
        },


    {
        'name': 'Loyola Marymount University',
        'city': 'Los Angeles, CA',
        },

    {
        'name': 'College of Charleston',
        'city': 'Charleston, SC',
        },


    {
        'name': 'Florida Atlantic University',
        'city': 'Boca Raton, FL',
        },



    {
        'name': 'California State University, East Bay',
        'city': 'Hayward, CA',
        },

    {
        'name': 'SIU Edwardsville',
        'city': 'Edwardsville, IL',
        },

    {
        'name': 'Jacksonville University',
        'city': 'Jacksonville, FL',
        },

    {
        'name': 'University of Notre Dame',
        'city': 'South Bend, IN',
        },

    {
        'name': 'University of Michigan',
        'city': 'Ann Arbor, MI',
        },

    {
        'name': 'University of Dayton',
        'city': 'Dayton, OH',
        },

    {
        'name': 'Franklin Pierce University',
        'city': 'Rindge, NH',
        },

    {
        'name': 'Boston University',
        'city': 'Boston, MA',
        },

    {
        'name': 'Drexel University',
        'city': 'Philadelphia, PA',
        },

    {
        'name': 'Wright State University',
        'city': 'Dayton, OH',
        },

    {
        'name': 'Fresno Pacific University',
        'city': 'Fresno, CA',
        },

    {
        'name': 'Virginia Commonwealth University',
        'city': 'Richmond, VA',
        },

    {
        'name': 'Birmingham-Southern College',
        'city': 'Birmingham, AL',
        },

    {
        'name': 'Michigan State University',
        'city': 'East Lansing, MI',
        },

    {
        'name': 'Virginia Tech',
        'city': 'Blacksburg, VA',
        },

    {
        'name': 'Lee University',
        'city': 'Cleveland, TN',
        },

    {
        'name': 'University of West Florida',
        'city': 'Pensacola, FL',
        },

    {
        'name': 'Liberty University',
        'city': 'Lynchburg, VA',
        },

    {
        'name': 'University at Albany, SUNY',
        'city': 'Albany, NY',
        },

    {
        'name': 'University of Redlands',
        'city': 'Redlands, CA',
        },

    {
        'name': 'Colgate University',
        'city': 'Hamilton, NY',
        },

    {
        'name': 'Lindsey Wilson College',
        'city': 'Columbia, KY',
        },

    {
        'name': 'West Virginia University',
        'city': 'Morgantown, WV',
        },

    {
        'name': 'Xavier University',
        'city': 'Cincinnati, OH',
        },

    {
        'name': 'Northeastern University',
        'city': 'Boston, MA',
        },

    {
        'name': 'Drake University',
        'city': 'Des Moines, IA',
        },

    {
        'name': 'Bucknell University',
        'city': 'Lewisburg, PA',
        },

    {
        'name': 'Temple University',
        'city': 'Philadelphia, PA',
        },

    {
        'name': 'Howard University',
        'city': 'Washington DC',
        },

    {
        'name': 'Western Kentucky University',
        'city': 'Bowling Green, KY',
        },

    {
        'name': 'Towson University',
        'city': 'Towson, MD',
        },

    {
        'name': 'Westmont College',
        'city': 'Santa Barbara, CA',
        },

    {
        'name': 'Nyack College',
        'city': 'Nyack, NY',
        },

    {
        'name': 'Schoolcraft College',
        'city': 'Livonia, MI',
        },

    {
        'name': 'High Point University',
        'city': 'High Point, NC',
        },

    {
        'name': 'Bethel University',
        'city': 'St. Paul, MN',
        },

    {
        'name': 'University of Delaware',
        'city': 'Newark, DE',
        },

    {
        'name': 'Niagara University',
        'city': 'Lewiston, NY',
        },

    {
        'name': 'Hastings College',
        'city': 'Hastings, NE',
        },

    {
        'name': 'Babson College',
        'city': 'Wellesley, MA',
        },

    {
        'name': 'Pfeiffer University',
        'city': 'Misenheimer, NC',
        },

    {
        'name': 'William Carey University',
        'city': 'Hattiesburg, MS',
        },

    {
        'name': 'Grand Canyon University',
        'city': 'Phoenix, AZ',
        },

    {
        'name': 'George Washington University',
        'city': 'Washington DC',
        },

    {
        'name': 'Western Michigan University',
        'city': 'Kalamazoo, MI',
        },

    {
        'name': 'University of Rio Grande',
        'city': 'Rio Grande, OH',
        },

    {
        'name': 'Mount Senario College',
        'city': 'Ladysmith, WI',
        'dissolved': 2002,
        },

    {
        'name': 'Francis Marion University',
        'city': 'Florence, SC',
        },

    {
        'name': 'Cornerstone University',
        'city': 'Grand Rapids, MI',
        },

    {
        'name': 'Judson University',
        'city': 'Elgin, IL',
        },

    {
        'name': 'Wake Forest University',
        'city': 'Winston-Salem, NC',
        },

    {
        'name': 'Bradley University',
        'city': 'Peoria, IL',
        },

    {
        'name': 'University of Richmond',
        'city': 'Richmond, VA',
        },

    {
        'name': 'Villanova University',
        'city': 'Villanova, PA',
        },

    {
        'name': 'American University',
        'city': 'Washington DC',
        },

    {
        'name': 'Davidson College',
        'city': 'Davidson, NC',
        },

    {
        'name': 'University of Denver',
        'city': 'Denver, CO',
        },


    {
        'name': 'Williams College',
        'city': 'Williamstown, MA',
        },


    {
        'name': 'Messiah College',
        'city': 'Grantham, PA',
        },

    {
        'name': 'Barry University',
        'city': 'Miami, FL',
        },

    {
        'name': 'Ohio State University',
        'city': 'Columbus, OH',
        },

    {
        'name': 'Marshall University',
        'city': 'Huntington, WV',
        },

    {
        'name': 'University of Cincinnati',
        'city': 'Cincinnati, OH',
        },

    {
        'name': 'University of Louisville',
        'city': 'Louisville, KY',
        },

    {
        'name': 'Auburn University',
        'city': 'Auburn, AL',
       },

    {
        'name': 'Seattle Pacific University',
        'city': 'Seattle, WA',
       },

    {
        'name': 'Princeton University',
        'city': 'Princeton, NJ',
       },

    {
        'name': 'Fresno State University',
        'city': 'Fresno, CA',
       },

    {
        'name': 'St. Lawrence University',
        'city': 'Canton, NY',
       },


    {
        'name': 'Corban University',
        'city': 'Salem, OR',
       },


    {
        'name': 'Seton Hall University',
        'city': 'South Orange, NJ',
       },

    {
        'name': 'Northwestern University',
        'city': 'Evanston, IL',
       },


    {
        'name': 'University of Missouri-Kansas City',
        'city': 'Evanston, IL',
       },


    {
        'name': 'University of Memphis',
        'city': 'Memphis, TN',
       },

    {
        'name': 'Hawaii Pacific University',
        'city': 'Honolulu, HI',
       },

    {
        'name': 'Embry-Riddle',
        'city': 'Daytona Beach, FL',
       },

    {
        'name': 'Marist College',
        'city': 'Poughkeepsie, NY',
       },

    {
        'name': 'University of North Carolina at Greensboro',
        'city': 'Greensboro, NC',
       },

    {
        'name': 'University of Alabama at Birmingham', 
        'city': 'Birmingham, AL',
       },

    {
        'name': 'Cal State Fullerton',
        'city': 'Fullerton, CA',
       },

    {
        'name': 'Santa Ana College',
        'city': 'Santa Ana, CA',
       },

    {
        'name': 'Loyola University Maryland',
        'city': 'Baltimore, MD',
       },
    {
        'name': 'Air Force Academy',
        'city': 'Colorado Springs, CO',
       },

    {
        'name': 'University of Illinois at Chicago',
        'city': 'Chicago, IL',
       },
    {
        'name': 'Nova Southeastern',
        'city': 'Fort Lauderdale, FL',
       },

    {
        'name': 'West Texas A&M',
        'city': 'Canyon, TX',
       },
    {
        'name': 'Richard Stockton College',
        'city': 'Galloway, NJ',
       },
    {
        'name': 'University of California, Santa Barbara',
        'city': 'Santa Barbara, CA',
       },

    {
        'name': 'University of Wisconsin-Milwaukee',
        'city': 'Milwaukee, WI',
       },
    {
        'name': 'UNLV',
        'city': 'Las Vegas, NV',
       },
    {
        'name': 'Pasadena City College',
        'city': 'Pasadena, CA',
       },
    {
        'name': 'University of California, Davis',
        'city': 'Davis, CA',
       },
    {
        'name': 'University of the Incarnate Word',
        'city': 'San Antonio, TX',
       },
    {
        'name': 'Ohio University',
        'city': 'Athens, OH',
       },
    {
        'name': 'Davis & Elkins College',
        'city': 'Elkins, WV',
       },
    {
        'name': 'Belmont Abbey College',
        'city': 'Belmont, NC',
       },
    {
        'name': 'University of Mount Union',
        'city': 'Alliance, OH',
       },
    {
        'name': 'Raritan Valley Community College',
        'city': 'Branchburg, NJ',
       },
    {
        'name': 'Cal State Dominguez Hills',
        'city': 'Carson, CA',
       },
    {
        'name': 'Cal State Northridge',
        'city': 'Northridge, CA',
       },
    {
        'name': 'Westminster College (Utah)',
        'city': 'Salt Lake City, UT',
       },

    {
        'name': 'Trinity University',
        'city': 'San Antonio, TX',
       },
    {
        'name': 'UNC Wilmington',
        'city': 'Wilmington, NC',
       },

    {
        'name': 'Canada College',
        'city': 'Redwood City, CA',
       },
    {
        'name': 'Myers University',
        'city': 'Seven Hills, OH',
       },
    {
        'name': 'Algonquin College',
        'city': 'Ottawa, ON',
       },
    {
        'name': 'University of Wisconsin-Green Bay',
        'city': 'Green Bay, WI',
       },
    {
        'name': 'Cal State Los Angeles',
        'city': 'Los Angeles, CA',
       },
    {
        'name': 'UNC Pembroke',
        'city': 'Pembroke, NC',
       },
    {
        'name': 'University of South Carolina Upstate',
        'city': 'Spartanburg, SC',
       },
    {
        'name': 'University of Wisconsin-Parkside',
        'city': 'Kenosha, WI',
       },
    {
        'name': 'Simon Fraser University',
        'city': 'Burnaby, BC',
       },
    {
        'name': 'Foothill College',
        'city': 'Los Altos, CA',
       },
    {
        'name': 'SUNY Cortland',
        'city': 'Cortland, NY',
       },
    {
        'name': 'New Jersey Institute of Technology',
        'city': 'Newark, NJ',
       },
    {
        'name': 'DeAnza College',
        'city': 'Cupertino, CA',
       },
    {
        'name': 'Oneonta State College',
        'city': 'Oneonta, NY',
       },
    {
        'name': 'Plymouth State University',
        'city': 'Plymouth, NH',
       },
    {
        'name': 'Colorado College',
        'city': 'Colorado Springs, CO',
       },

    {
        'name': 'University of Colorado at Colorado Springs',
        'city': 'Colorado Springs, CO',
       },
    {
        'name': 'Lock Haven University',
        'city': 'Lock Haven, PA',
       },
    {
        'name': 'SUNY Brockport',
        'city': 'Brockport, NY',
       },
    {
        'name': 'University of Maine',
        'city': 'Orono, ME',
       },
    {
        'name': 'Spring Arbor University',
        'city': 'Spring Arbor, MI',
       },
    {
        'name': 'University of Southern Maine',
        'city': 'Portland, ME',
       },
    {
        'name': 'Massachusetts College of Liberal Arts',
        'city': 'North Adams, MA',
       },
    {
        'name': 'San Francisco State University',
        'city': 'San Francisco, CA',
       },
    {
        'name': 'Keene State College',
        'city': 'Keene, NH',
       },
    {
        'name': 'Alderson-Broaddus College',
        'city': 'Philippi, WV',
       },

    {
        'name': 'Brandeis University',
        'city': 'Waltham, MA',
       },
    {
        'name': 'University of Bridgeport',
        'city': 'Bridgeport, CT',
       },

    {
        'name': 'University of Oklahoma',
        'city': 'Norman, OK',
       },
    {
        'name': 'Denison University',
        'city': 'Granville, OH',
       },
    {
        'name': 'Bowdoin College',
        'city': 'Brunswick, ME',
       },
    {
        'name': 'Florida Institute of Technology',
        'city': 'Melbourne, FL',
       },
    {
        'name': 'Northern Illinois University',
        'city': 'DeKalb, IL',
       },
    {
        'name': 'Lewis University',
        'city': 'Romeoville, IL',
       },
    {
        'name': 'Quincy University',
        'city': 'Quincy, IL',
       },
    {
        'name': 'Rowan University',
        'city': 'Glassboro, NJ',
       },
    {
        'name': 'Lehman College',
        'city': 'New York, NY',
       },
    {
        'name': 'Kutztown University',
        'city': 'Kutztown, PA',
       },

    {
        'name': 'University of Houston',
        'city': 'Houston, TX',
       },
    {
        'name': 'Brigham Young University',
        'city': 'Provo, UT',
       },
    {
        'name': 'Union College',
        'city': 'Schenectady, NY',
       },
    {
        'name': 'Whittier College',
        'city': 'Whittier, PA',
       },

    {
        'name': 'Wheaton College (MA)',
        'city': 'Norton, MA',
       },
    {
        'name': 'Gettysburg College',
        'city': 'Gettysburg, PA',
       },
    {
        'name': 'University of Oregon',
        'city': 'Eugene, OR',
       },
    {
        'name': 'University of Massachusetts Amherst',
        'city': 'Amherst, MA',
       },
    {
        'name': 'Montclair State University',
        'city': 'Montclair, NJ',
       },
    {
        'name': 'Florida Gulf Coast University',
        'city': 'Fort Myers, FL',
       },
    {
        'name': 'Eckerd College',
        'city': 'St. Petersburg, FL',
       },
    {
        'name': 'Clayton State University',
        'city': 'Morrow, GA',
       },
    {
        'name': 'Georgia State University',
        'city': 'Atlanta, GA',
       },
    {
        'name': 'Saint Leo University',
        'city': 'St. Leo, FL',
       },

    {
        'name': 'University of California, Irvine',
        'city': 'Irvine, CA',
       },

    {
        'name': 'University of Nebraska Omaha',
        'city': 'Omaha, NE',
       },

    {
        'name': 'Virginia Military Institute',
        'city': 'Lexington, VA',
       },

    {
        'name': 'Iowa State University',
        'city': 'Ames, IA',
       },


    {
        'name': 'Shurtleff College',
        'city': 'Alton, IL',
       },

    {
        'name': 'Washburn University',
        'city': 'Topeka, KS',
       },

    {
        'name': 'University of Minnesota',
        'city': 'Minneapolis, MN',
       },


    {
        'name': 'Hamline University',
        'city': 'Saint Paul, MN',
       },


    {
        'name': 'Washington and Lee University',
        'city': 'Lexington, VA',
       },

    {
        'name': 'Case Western Reserve University',
        'city': 'Cleveland, OH',
       },

    {
        'name': 'Middlebury College',
        'city': 'Middlebury, VT',
       },

    {
        'name': 'Stevens Institute of Technology',
        'city': 'Hoboken, NJ',
       },

    {
        'name': 'Tufts University',
        'city': 'Medford, MA',
       },

    {
        'name': 'Dickinson College',
        'city': 'Carlisle, PA',
       },

    {
        'name': 'City College of New York',
        'city': 'New York, NY',
       },

    {
        'name': 'Wesleyan Universiyt',
        'city': 'Middletown, CT',
       },

    {
        'name': 'Randolph-Macon College',
        'city': 'Ashland, VA',
       },

    {
        'name': 'Olivet College',
        'city': 'Olivet, MI',
       },

    {
        'name': 'Albion College',
        'city': 'Albion, MI',
       },





    {
        'name': 'Santa Barbara City College',
        'city': 'Santa Barbara, CA',
        },


    {
        'name': 'University of California, Santa Cruz',
        'city': 'Santa Cruz, CA',
        },


    {
        'name': 'Cal Poly Pomona',
        'city': 'Pomona, CA',
        },



    {
        'name': 'University of California, Riverside',
        'city': 'Riverside, CA',
        },






]
