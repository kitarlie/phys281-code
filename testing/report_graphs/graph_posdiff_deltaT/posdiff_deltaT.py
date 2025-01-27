from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
import numpy as np

def model(x, b, m):
    """

    A simple linear model y = mx + b for the data.

    Parameters:
        x (list-like): The independent variable

        b (float): The y-intercept

        m (float): The gradient

    Returns:
        y (list-like): The dependent variable

    """


    return(b + m * x)

#Error data for the Earth
earthData = np.array([
    775.6766433750192,
    829.5040907313482,
    949.5913567382695,
    1096.7863765719371,
    1261.872199519638,
    1624.1867375275165,
    2010.8584650420212,
    ])

#Time interval data
deltaT = np.array([
    10,
    25,
    50,
    75,
    100,
    150,
    200,
])

#Performs curve fitting
copt, ccov = curve_fit(model, deltaT, earthData)

#Initialises figure and axis
fig = plt.figure(figsize = [8, 6])
ax = plt.subplot()

#Plots line of best fit
ax.plot(deltaT, model(deltaT, copt[0], copt[1]), color = 'k', label = 'Best fit')

#Plots points
ax.scatter(deltaT, earthData, c = 'b', marker = '.', label = 'Data')

ax.set_xlabel('Time interval, s')

ax.set_ylabel('Error in Earth position, m')

plt.legend()

plt.savefig('posdiff_deltaT.svg')