from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
import numpy as np

def model1(x, b, m):
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

def model2(x, b, m):
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

def model3(x, c, b, a):
    """

    A simple linear model y = mx + b for the data.

    Parameters:
        x (list-like): The independent variable

    Returns:
        y (list-like): The dependent variable

    """


    return(c + b*x + a*x**2)

#The conservation factor dE_ave/E_0 for every deltaT tested:
energyData = np.array(
    [
        6.53355740998358e+26,
        1.6333903506697132e+27,
        3.266784027603369e+27,
        4.900181029007533e+27,
        6.533581352747167e+27,
        9.800391965823715e+27,
        1.3067215852613648e+28,
        1.633501600416978e+28,
    ]
)/6.2110741699822796e+35

amData = np.array(
    [
        np.linalg.norm(np.array([-1.56032026e+27,  1.28952087e+25,  1.68927235e+27])),
        np.linalg.norm(np.array([-1.39268254e+27, -1.54742505e+27, -1.47005380e+27])),
        np.linalg.norm(np.array([-4.28120930e+27,  -9.28455029e+26, -2.69509863e+27])),
        np.linalg.norm(np.array([-6.79577501e+27, -6.78287980e+27, -5.19676912e+27])),
        np.linalg.norm(np.array([-1.05353855e+28, -1.39913015e+28, -9.02664612e+27])),
        np.linalg.norm(np.array([-2.39206122e+28, -2.56743606e+28, -2.39464026e+28])),
        np.linalg.norm(np.array([-4.25283984e+28, -4.74414730e+28, -4.26702457e+28])),
        np.linalg.norm(np.array([-7.29610911e+28, -6.98533458e+28, -6.80867022e+28])),

    ]
)/np.linalg.norm(np.array([8.22617883e+41, 2.60669176e+41, 3.13117308e+43]))

lmData = np.array(
    [   
        np.linalg.norm(np.array([1.89928081e+17,  1.92786817e+17, 1.92069219e+17])),
        np.linalg.norm(np.array([1.19721250e+18, 1.19606243e+18, 1.19762665e+18])),
        np.linalg.norm(np.array([4.79479597e+18, 4.78983854e+18, 4.79425344e+18])),
        np.linalg.norm(np.array([1.07851220e+19, 1.07882202e+19, 1.07852573e+19])),
        np.linalg.norm(np.array([1.91819101e+19, 1.91772839e+19, 1.91801013e+19])),
        np.linalg.norm(np.array([4.31692517e+19, 4.31667670e+19, 4.31575392e+19])),
        np.linalg.norm(np.array([7.67705052e+19, 7.67544183e+19, 7.67409145e+19])),
        np.linalg.norm(np.array([1.19988683e+20, 1.19962172e+20, 1.19931744e+20])),      
    ]
)/np.linalg.norm(np.array([-4.31359973e+26, -1.27242245e+27, 4.19606590e+25]))

#Time interval data
deltaT = np.array([
    10,
    25,
    50,
    75,
    100,
    150,
    200,
    250,
])

#Performs curve fitting
alpha1, alpha2 = curve_fit(model1, deltaT, energyData)
beta1, beta2 = curve_fit(model2, deltaT, amData)
gamma1, gamma2 = curve_fit(model3, deltaT, lmData)

#Initialises figure and axis
fig = plt.figure(figsize = [8, 6])
ax = plt.subplot()

#Plots line of best fit
ax.plot(deltaT, model1(deltaT, alpha1[0], alpha1[1]), color = 'k', lw = 1)
ax.plot(deltaT, model2(deltaT, beta1[0], beta1[1]), color = 'k', lw = 1)
ax.plot(deltaT, model3(deltaT, gamma1[0], gamma1[1], gamma1[2]), color = 'k', lw = 1)

#Plots points
print(energyData)
print(amData)
ax.scatter(deltaT, energyData, c = 'r', marker = 'o', label = 'Energy')
ax.scatter(deltaT, amData, c = 'g', marker = 'o', label = 'Angular momentum')
ax.scatter(deltaT, lmData, c = 'b', marker = 'o', label = 'Linear momentum')

ax.set_xlabel('Time interval, s')
ax.set_ylabel('Conservation factor')

plt.legend()

plt.show()