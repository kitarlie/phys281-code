"""

Handles the graphing aspect of the code.

"""

from matplotlib import pyplot as plt
import numpy as np

def data_setup(bodyList):
    """

    Reformats the data list so it is organised by x, y, z rather than by each time.

        Parameters:
            bodyList (list-like): The list of position data for the current body

        Returns:
            xs (list-like): The past x-coordinates of the body

            ys (listlike): The past y-coordinates of the body

            zs (listlike): The past z-coordinates of the body

    """
    #Initialises lists for the x, y and z coordinates.
    xs = []
    ys = []
    zs = []

    #Chooses each point in the body data.
    for point in bodyList:

        #Adds each coordinate to the corresponding list
        xs.append(point[0])
        ys.append(point[1])
        zs.append(point[2])


    return (xs, ys, zs)


def plot(system, dataList):
    """

    Plots each body onto the graph.

        Parameters:
            system(list-like): Contains all Particle instances defined for the system.

            dataList(list-like): Contains all position vectors at every time for all bodies in the system.

    """

    #Introduces a new figure.
    fig = plt.figure()

    #Creates a 3-D axis to plot on.
    ax = plt.subplot(projection = '3d')

    #Plots for every body
    for i, body in enumerate(system):
        #Sets up data lists
        xs, ys, zs = data_setup(dataList[i])

        #Plots the 'trail' where the planet has been, as a line
        ax.plot(xs, ys, zs, color = body.colour, marker = None, linestyle = 'solid', )

        #Plots the planet itself in its final position as a larger point.
        ax.plot(xs[-1], ys[-1], zs[-1], color = body.colour, marker = '.')

    #Displays the figure
    plt.show()
