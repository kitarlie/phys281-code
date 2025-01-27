"""

This contains functions that calculate several system parameters for conservation and accuracy tests.

"""

from Particle import Particle
import numpy as np

def total_KE(system):
    """

    Calculates the total kinetic energy of the system by summing the individual energies.

        Parameters: 
            system (list-like): An array containing each Particle object representing a solar system body.

        Returns:
            kineticEnergy (int/float): The total kinetic energy of all bodies in the system.

    """
    #Initialise the kinetic energy variable
    kineticEnergy = 0

    #Adds the individual energy of each body
    for body in system:
        kineticEnergy += body.calculate_kinetic_energy()

    #Returns the total kinetic energy
    return kineticEnergy

def total_PE(system):
        """
        
        Calculates the gravitational potential energy of the system

            Parameters:
                System (list-like): Contains all Particle instances defined for the system 

            Returns:
                potentialEnergy (float): The gravitational potential energy of the system
        
        """
        #Initialises the potential energy
        potentialEnergy = 0

        #Iterates over all bodies without repeating a combination
        for i, body in enumerate(system):
            for j in range(i+1, len(system)):
                potentialEnergy += ((system[i].G * system[i].mass * system[j].mass)/np.linalg.norm(system[i].position - system[j].position))
        
        #Returns the total potential energy
        return potentialEnergy

def total_AM(system):
    """

    Calculates the total angular momentum of the system by summing the individual angular momenta.

        Parameters: 
            system (list-like): An array containing each Particle object representing a solar system body.

        Returns:
            angularMomentum (int/float): The total angular momentum of all bodies in the system.

    """
    #Initialises the angular momentum variable
    angularMomentum = 0

    #Adds individual angular momenta
    for body in system:
        angularMomentum += body.calculate_angular_momentum()

    #Returns the angular momentum
    return angularMomentum

def total_LM(system):
    """

    Calculates the total linear momentum of the system by summing the individual linear momenta.

        Parameters: 
            system (list-like): An array containing each Particle object representing a solar system body.

        Returns:
            linearMomentum (int/float): The total linear momentum of all bodies in the system.

    """
    #Initialises the linear momentum variable
    linearMomentum = 0

    #Adds individual linear momenta
    for body in system:
        linearMomentum += body.calculate_linear_momentum()

    #Returns the linear momentum
    return linearMomentum

def distance_test(system, endDate):
    """

    Shows the distance between the 'ideal' data taken from JPL and the simulation data.

    Parameters:
        system (list-like): An array containing each Particle object representing a solar system body.

        endDate (str): The end datetime, yyyy-mm-dd hh:mm:ss:ms

    """
    #Organises the JPL data at the end date in the same way as the simulation parameters.
    import data
    ideal = []
    for body in (data.jpl_scrape(dateString = endDate)):
        ideal.append(Particle( 
                name = body['Name'], 
                mass = body['Mass'], 
                radius = body['Radius'],
                position = body['Position'],
                velocity = body['Velocity'],
                colour = body['Colour']
                )
    )

    #Adds a text variable that will be written to the summary file.
    text = '\n'

    #Compares every JPL ephemeride.
    for count, body in enumerate(ideal):
        distance = np.linalg.norm(body.position - system[count].position)

        #Adds the data to the text variable.
        text += (body.name + ': ' + str(distance) + ' metres out.\n')

    #Opens the text file in 'append' mode.
    f = open('ephemeride_data/!summary_file.txt', 'a')

    f.write(text)
    f.close()

def cons_of_energy():
    """

    Returns the average change in energy and the intial energy as a test for energy conservation.

        Returns:
            dE_ave(float): The average change in total energy across the simulation.

            E(float): The initial total energy.

    """
    f = open('ephemeride_data/energy.txt', 'r')

    #Contains all the energies
    dataList = f.read().rstrip('\n').split('\n')

    #Contains the changes in energy between each step
    dE = []

    #Subtracts the energy of i+1 from the energy of i
    for i in range(len(dataList)-1):
        dE.append(float(dataList[i+1]) - float(dataList[i]))

    #Closes the file
    f.close()

    #Calculates the average of the list
    return(np.mean(np.array(dE)), float(dataList[0]))

def cons_of_LM():
    """

    Returns the average change in linear momentum and the intial linear momentum as a test for conservation.

        Returns:
            dp_ave(float): The average change in total linear momentum across the simulation.

            p(float): The initial total linear momentum.

    """

    f = open('ephemeride_data/total_LM.txt', 'r')

    #Contains all the angular momenta
    dataList = f.read().rstrip('\n').split('\n')

    #Converts each point into a list
    for i in range(len(dataList)):
        dataList[i] = dataList[i].split(' ')

        #Converts each number from a string into a float
        for j in range(3):
            dataList[i][j] = float(dataList[i][j])

        #Converts the point to a numpy array
        dataList[i] = np.array(dataList[i])

    #Contains the changes in angular momentum between each step
    dp = []

    #Subtracts the LM of i+1 from the AM of i
    for i in range(len(dataList)-1):
        dp.append(dataList[i+1] - dataList[i])

    #Closes the file
    f.close()

    #Calculates the average of the list
    dp_ave = np.array([np.mean(np.array(dp)[0]), np.mean(np.array(dp)[1]), np.mean(np.array(dp)[2])])

    return(dp_ave, dataList[0])

def cons_of_AM():
    """

    Returns the average change in angular momentum and the intial angular momentum as a test for conservation.

        Returns:
            dL_ave(float): The average change in total angular momentum across the simulation.

            L(float): The initial total angular momentum.

    """

    f = open('ephemeride_data/total_AM.txt', 'r')

    #Contains all the angular momenta
    dataList = f.read().rstrip('\n').split('\n')

    #Converts each point into a list
    for i in range(len(dataList)):
        dataList[i] = dataList[i].split(' ')

        #Converts each number from a string into a float
        for j in range(3):
            dataList[i][j] = float(dataList[i][j])

        #Converts the point to a numpy array
        dataList[i] = np.array(dataList[i])

    #Contains the changes in angular momentum between each step
    dL = []

    #Subtracts the AM of i+1 from the AM of i
    for i in range(len(dataList)-1):
        dL.append(dataList[i+1] - dataList[i])

    #Closes the file
    f.close()

    #Calculates the average of the list
    dL_ave = np.array([np.mean(np.array(dL)[0]), np.mean(np.array(dL)[1]), np.mean(np.array(dL)[2])])

    return(dL_ave, dataList[0])

