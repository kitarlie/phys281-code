"""

This is the main code for the simulation.

After calling Menu and data, it creates the required Particle instances and updates them as long as the initial conditions
require. It also stores the initial conditions, ephemeride and conservation data in text files which can be saved for later.

"""

import data
import Graphics
from Particle import Particle
from Files import *
from Menu import MainWindow as menu
import numpy as np
import Tests

    

def update(system, deltaT, algorithm):
    """

    Updates the position, velocity and acceleration of each body.

        Parameters:
            system (list-like): Contains all Particle instances defined for the system.

            deltaT (int/float): The time interval across which the particle moves.

            algorithm (int): A numerical representation of which approximation algorithm is used.

    """
        
    for body in system:
        #Updates all accelerations before velocity and position.
        body.update_gravitational_acceleration(system)

    for body in system:
        #Updates position and velocity.
        body.algorithm_choice(deltaT, system, algorithm)

        #Updates ephemeride files.
        ephemeride_file(body)

    
    #Saves the current energy, linear momentum and angular momentum.
    energy_file(system)
    LM_file(system)
    AM_file(system)


#Initialises the menu
Menu = menu()

#Takes the time interval, formats the start date and end date.
deltaT = int(Menu.outputs[0])


#Converts the start and end dates into astropy-compatible formats.
startDate = data.date_convert(
    day = Menu.outputs[1], 
    month = Menu.outputs[2],
    year = Menu.outputs[3]
)

endDate = data.date_convert(
    day = Menu.outputs[4], 
    month = Menu.outputs[5],
    year = Menu.outputs[6]
)

#The choice of algorithm
algorithm = int(Menu.outputs[7])


#Finds the number of intervals needed based on the start date, end date and frame interval deltaT (must be int)
intervalNumber = round(data.time_difference(startDate, endDate)/deltaT)

#Collects all the objects to be passed into the Acceleration function
system = []


#Iterates over all bodies with given data, creates a Particle instance for each one and adds it to the System list
#Also creates the text file for each body
for body in (data.jpl_scrape(dateString = startDate) + Menu.customBodies):
    particle = Particle( 
            name = body['Name'], 
            mass = body['Mass'], 
            radius = body['Radius'],
            position = body['Position'],
            velocity = body['Velocity'],
            colour = body['Colour']
            )
    system.append(particle)
    ephemeride_file(particle)

#Sets up the file system with the setup file, position files for each body and the conservation quantities.
setup_files(deltaT, startDate, endDate, algorithm, system)

#Runs the simulation until the end date is reached
print('Running simulation')
for i in range(intervalNumber):
    update(system, deltaT, algorithm)
print('Simulation finished')

#Applies the distance test
Tests.distance_test(system, endDate)

#Applies the three conservation tests
dE, E = Tests.cons_of_energy()

dL, L = Tests.cons_of_AM()

dp, p = Tests.cons_of_LM()

#Adds to summary file
update_summary(dE, E, dL, L, dp, p)

#Plots graph
Graphics.plot(system, scrape_position_data(system))
