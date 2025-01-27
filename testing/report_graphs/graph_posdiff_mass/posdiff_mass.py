"""

Quick independent script to create the graph of difference in position to the JPL data and mass.

"""

from matplotlib import pyplot as plt
import numpy as np

#Euler data for the final distance of each body at deltaT = 10
final_positions_1 = [
    24287.657967372885,
    6374.618490894202,
    3386.1355730718324,
    3753.9696336965585,
    1432.0960732995738,
    132.70001338561175,
    34.683776928983164,
    8.574046831272462,
    3.6917683544879663,
    2.708786904447415,
]

#Euler-Cromer data
final_positions_2 = [
    24287.657967372885,
    6374.618490894202,
    3386.1355730718324,
    3753.9696336965585,
    1432.0960732995738,
    132.70001338561175,
    34.683776928983164,
    8.574046831272462,
    3.6917683544879663,
    2.708786904447415 
]

#Euler-Richardson data
final_positions_3 = [
    5277.795180741108,
    411.0156669982625,
    775.6766433750192,
    6280.027971814288,
    316.89403809577897,
    29.40422921376594,
    7.686151104142101,
    1.9037231413049025,
    0.8230351226397113,
    0.5966769185602899
]

#Masses
masses = [
    3.301033816280359e+23,
    4.867305814842006e+24,
    5.972168494074286e+24,
    7.34578878683907e+22,
    6.416908799424659e+23,
    1.89851763525763e+27,
    5.683173920860615e+26,
    8.68096924021995e+25,
    1.024306234448616e+26,
    1.3039569692701858e+22,
]

fig = plt.figure(figsize=[8, 6], dpi = 100)

ax = plt.subplot()

ax.set_xscale('log')

ax.set_ylabel('Distance from JPL data, m')
ax.set_xlabel('Body mass, kg')

ax.plot(masses, final_positions_1, color = 'r', marker = '.', linestyle = 'None', label = 'Euler')
ax.plot(masses, final_positions_2, color = 'g', marker = '.', linestyle = 'None', label = 'Euler-Cromer')
ax.plot(masses, final_positions_3, color = 'b', marker = '.', linestyle = 'None', label = 'Euler-Richardson')

plt.legend()

plt.savefig('posdiff_mass.svg')