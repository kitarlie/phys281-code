"""

Scrapes the data from which to build the simulation.
Data is from JPL Horizons.
Solar System Barycentre.

"""

from astropy.time import Time
from astropy.coordinates import get_body_barycentric_posvel
from poliastro import constants
from astropy.constants import G
from spiceypy import sxform, mxvg
import numpy as np

def date_convert(day, month, year):
    """
    Converts three numbers (dd, mm, yyyy) into a 'date string' compatible with astropy 'yyyy-mm-dd 00:00:00:0'.

        Parameters:
            day (int): The day number

            month (int): The month number

            year (int): The year number

        Returns:
            dateString (str): A text representation of the chosen date in a format compatible with astropy.
    """

    #Converts numbers into text.
    day = str(day)
    month = str(month)
    year = str(year)

    #Checks that numbers aren't too long
    if len(year) > 4:
        raise ValueError('Year must be a 4 digit number')
    
    if len(month) > 2:
        raise ValueError('Month must be a 2 digit number')

    if len(day) > 2:
        raise ValueError('Day must be a 2 digit number')

    #Ensures the date is in the form yyyy, i.e. converts year 14 to year 0014.
    for i in range(4 - len(year)):
            year = '0' + year

    #Ensures the month is in the form mm, i.e.e converts month 4 to month 04:
    for i in range(2 - len(month)):
            month = '0' + month

    #Ensures the day is in the form dd, i.e.e converts day 4 to day 04:
    for i in range(2 - len(day)):
            day = '0' + day

    #Formats the year, month and day into a string compatible with astropy
    return(year + '-' + month + '-' + day + ' 00:00:00.0')

def time_difference(dateString1, dateString2):
    """

    Takes two datetimes and returns the difference between them in seconds.

        Parameters:
            dateString1 (str): The start datetime, yyyy-mm-dd hh:mm:ss:ms

            dateString2 (str): The end datetime, yyyy-mm-dd hh:mm:ss:ms

        Returns:
            dt (float): The difference between the two datetimes in seconds.

    """
    #Converts datestrings into Time objects.
    t1 = Time(dateString1)
    t2 = Time(dateString2)

    #Returns the difference between the times in seconds.
    dt = (t2 - t1).sec

    #Conversion from numpy float to python float
    return(dt.item())
    

def jpl_scrape(dateString):
    """

    Scrapes the JPL data from astropy and poliastro, and returns it in list of dictionaries.

        Parameters:
            dateString (str): The start datetime, yyyy-mm-dd hh:mm:ss:ms

        Returns:
            jplData (list-like): A list of data organised into separate dictionaries for each ephemeride.

    """

    #Creates a list in which to store the JPL data
    jplData = []

    #Get the time at 0:00:00.0 on the 4th December 2023
    t = Time(dateString, scale="tdb")

    #Loops across the bodies in the list, and enumerates to index the colour list later.
    for count, body in enumerate(ephemerides):

        #Get positions of velocities for the current body
        pos, vel = get_body_barycentric_posvel(body, t, ephemeris="jpl")

        #Make a "state vector" of positions and velocities (in metres and metres/second, respectively)
        statevec = [
            pos.xyz[0].to("m").value,
            pos.xyz[1].to("m").value,
            pos.xyz[2].to("m").value,
            vel.xyz[0].to("m/s").value,
            vel.xyz[1].to("m/s").value,
            vel.xyz[2].to("m/s").value,
        ]

        #Get transformation matrix to the ecliptic (use time in Julian Days)
        trans = sxform("J2000", "ECLIPJ2000", t.jd)

        #Transform state vector to ecliptic
        statevececl = mxvg(trans, statevec)

        #Get mass - gets the GM constant using the body string
        mass = (getattr(constants, ('GM_'+body))/G).value

        #Get positions and velocities
        position = [statevececl[0], statevececl[1], statevececl[2]]
        velocity = [statevececl[3], statevececl[4], statevececl[5]]

        jplData.append(
            #Dictionary storing each required data point that I need
            {
                'Name': body,
                'Mass': mass,
                'Radius': radii[count],
                'Position': position,
                'Velocity': velocity,
                'Colour': colours[count]
            },
        )

    return(jplData)


#Stores the names of each JPL ephemeride
ephemerides = [
    'sun',
    'mercury',
    'venus',
    'earth',
    'moon',
    'mars',
    'jupiter',
    'saturn',
    'uranus',
    'neptune',
    'pluto',
    ]

#Stores the colours of each planet as hex codes - picked from PaletteMaker
colours = [
    '#FDB813', #Sun - orange-y yellow
    '#B7B8B9', #Mercury - grey
    '#EECB8B', #Venus - tan
    '#6B93D6', #Earth, blue
    '#F6F1D5', #Moon, grey
    '#C1440E', #Mars, red
    '#D8CA9D', #Jupiter, light tan
    '#EAD6B8', #Saturn, cream
    '#8DC9EE', #Uranus, light blue
    '#5B5DDF', #Neptune, turqoise/blue
    '#DDC4AF', #Pluto, peach
]

#Stores the radii to add a sense of scale for each body when plotting the graphs - this is the volumetric mean radius
#from the JPL data, all in km.
radii = [
    695700,
    2440,
    6051.84,
    6378.137,
    1737.53,
    3389.92,
    69911,
    58232,
    25362,
    24624,
    1188.3
]