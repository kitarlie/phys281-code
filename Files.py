"""

Contains all the functions that perform file handling actions.

"""

import os
import Tests

def setup_files(deltaT, startDate, endDate, algorithm, system):
    """

    Clears all current files in ephemeride_data and creates new ones for the new run.

        Parameters:
            deltaT (int/float): The time interval across which the particle moves.

            startDate (str): A text representation of the start date in a format compatible with astropy.

            endDate (str): A text representation of the end date in a format compatible with astropy.

            algorithm (int): A numerical representation of which approximation algorithm is used.

            system(list-like): Contains all Particle instances defined for the system.

    """

    #Finds ephemeride_data within the current working directory.
    directory = os.getcwd() + '/ephemeride_data'

    #Creates a list of all files in ephemeride_data
    files = os.listdir(directory)
    for file in files:
        
        #Creates a file path for each file
        file_path = os.path.join(directory, file)

        #Deletes the file if it exists
        if os.path.isfile(file_path):
            os.remove(file_path)


    #Sets the file name
    fileName = 'ephemeride_data/!summary_file.txt'

    #Creates and opens the file
    f = open(fileName, 'x')

    #Writes the data into the file
    f.write('deltaT: ' + str(deltaT) + '\nstartDate: ' + startDate + '\nendDate: ' + endDate + '\nalgorithm: ' + str(algorithm) + '\n')
    
    #Closes the file
    f.close()

    #Initialises individual ephemeride files
    for body in system:
        #Creates a string containing each position element.
        position = str(body.position[0]) + ' ' + str(body.position[1]) + ' ' + str(body.position[2])

        #Creates the file name in the form ephemeride_data/name.txt
        fileName = 'ephemeride_data/' + body.name + '.txt'

        f = open(fileName, 'x')
        f.write(position + '\n')
        f.close()

    #Initialises conservation quantity files

    #Energy file
    fileName = 'ephemeride_data/energy.txt'
    f = open(fileName, 'x')
    f.write(str(Tests.total_KE(system) + Tests.total_PE(system)) + '\n')
    f.close()

    #Linear momentum file

    LM = str(Tests.total_LM(system)[0]) + ' ' + str(Tests.total_LM(system)[1]) + ' ' + str(Tests.total_LM(system)[2])

    fileName = 'ephemeride_data/total_LM.txt'
    f = open(fileName, 'x')
    f.write(LM + '\n')
    f.close()

    #Angular momentum file

    AM = str(Tests.total_AM(system)[0]) + ' ' + str(Tests.total_AM(system)[1]) + ' ' + str(Tests.total_AM(system)[2])

    fileName = 'ephemeride_data/total_AM.txt'
    f = open(fileName, 'x')
    f.write(AM + '\n')
    f.close()

def ephemeride_file(body):
    """

    Creates a text file for each body storing the position of each body during each time interval.

    All files are stored in the folder ephemeride_data

        Parameters:
            body (object): The solar system body whose data is currently being stored.

    """
    #Creates a string containing each position element.
    position = str(body.position[0]) + ' ' + str(body.position[1]) + ' ' + str(body.position[2])

    fileName = 'ephemeride_data/' + body.name + '.txt'

    #Writes to the file
    f = open(fileName, 'a')
    f.write(position + '\n')
    f.close()

def energy_file(system):
    """

    Updates the energy file.

        Parameters:
            system(list-like): Contains all Particle instances defined for the system.

    """
    #Writes to the file
    fileName = 'ephemeride_data/Energy.txt'
    f = open(fileName, 'a')
    f.write(str(Tests.total_KE(system) + Tests.total_PE(system)) + '\n')
    f.close()

def LM_file(system):
    """

    Updates the linear momentum file.

        Parameters:
            system(list-like): Contains all Particle instances defined for the system.

    """
    #Creates a string containing each linear momentum element.
    LM = str(Tests.total_LM(system)[0]) + ' ' + str(Tests.total_LM(system)[1]) + ' ' + str(Tests.total_LM(system)[2])

    #Writes to the file
    fileName = 'ephemeride_data/Total_LM.txt'
    f = open(fileName, 'a')
    f.write(LM + '\n')
    f.close()

def AM_file(system):
    """

    Updates the angular momentum file.

        Parameters:
            system(list-like): Contains all Particle instances defined for the system.

    """
    #Creates a string containing each angular momentum element.
    AM = str(Tests.total_AM(system)[0]) + ' ' + str(Tests.total_AM(system)[1]) + ' ' + str(Tests.total_AM(system)[2])

    #Writes to the file.
    fileName = 'ephemeride_data/Total_AM.txt'
    f = open(fileName, 'a')
    f.write(AM + '\n')
    f.close()

def scrape_position_data(system):
    """

    Turns the position data from ephemeride_data into usable data for pyplot.

        Parameters:
            system(list-like): Contains all Particle instances defined for the system.

        Returns:
            dataList(list-like): Contains all position vectors at every time for all bodies in the system.

    """
    #Sets up the data list to store all the positions.
    dataList = []


    for body in system:
        #Sets up a data file for each individual body.
        bodyList = []

        #Opens and reads the file.
        fileName = 'ephemeride_data/' + body.name + '.txt'
        f = open(fileName, 'r')
            
        #Splits the file by line and removes trailing newline characters.
        bodyList = f.read().rstrip('\n').split('\n')


        for i, entry in enumerate(bodyList):
            #Splits each line by whitespace to get separate numbers.
            bodyList[i] = entry.split(' ')

            for j, entry_ in enumerate(bodyList[i]):
                #Converts each entry from a string to a float.
                bodyList[i][j] = float(entry_)

        dataList.append(bodyList)

        f.close()

    return dataList

def update_summary(dE, E, dL, L, dp, p):
    """

    Updates the summary file with the conservation data.

        Parameters:
            dE (float): The average change in total energy.

            E (float): The initial total energy.

            dL (float): The average change in total angular momentum.

            L (float): The initial total angular momentum.
            
            dp (float): The average change in total linear momentum.

            p (float): The initial total linear momentum.
    """
    #Sets the file name.
    fileName = 'ephemeride_data/!summary_file.txt'

    #Opens the file in 'append' mode.
    f = open(fileName, 'a')

    #Formats the summary text for the conservation data.
    summary = ('Average change in energy:' + str(dE) + '\n' +
        'Initial energy:' + str(E) + '\n' +

        'Average change in angular momentum:' + str(dL) + '\n' +
        'Initial angular momentum:' + str(L) + '\n' +

        'Average change in linear momentum:' + str(dp) + '\n' +
        'Initial linear momentum:' + str(p) + '\n'
    )

    #Writes the data into the file.
    f.write(summary)

    #Closes the file.
    f.close()