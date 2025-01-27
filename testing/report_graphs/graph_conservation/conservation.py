"""

Quick independent script to create the conservation graphs. Not intended for marking, just included for organisation.

"""

from matplotlib import pyplot as plt
import numpy as np

#The 'conservation factor' is the fraction of the initial value that is lost.

#Euler data
data_1 = [
    (6.533513324314882e+26/6.2110741699822796e+35), #Energy
    (np.linalg.norm(np.array([3.52709750e+29, 3.52490531e+29, 3.55843285e+29]))/np.linalg.norm(np.array([8.22617883e+41, 2.60669176e+41, 3.13117308e+43]))), #AM
    (np.linalg.norm(np.array([1.57514203e+15, -2.36989996e+15,  2.55750986e+14]))/np.linalg.norm(np.array([-4.31359973e+26, -1.27242245e+27,  4.19606590e+25]))) #LM
]

#Euler-Cromer data
data_2 = [
    (6.533513324314882e+26/6.2110741699822796e+35), #Energy
    (np.linalg.norm(np.array([3.52709750e+29, 3.52490531e+29, 3.55843285e+29]))/np.linalg.norm(np.array([8.22617883e+41, 2.60669176e+41, 3.13117308e+43]))), #AM
    (np.linalg.norm(np.array([1.57514203e+15, -2.36989996e+15,  2.55750986e+14]))/np.linalg.norm(np.array([-4.31359973e+26, -1.27242245e+27,  4.19606590e+25]))) #LM
]

#Euler-Richardson data
data_3 = [
    (6.53355740998358e+26/6.2110741699822796e+35), #Energy
    (np.linalg.norm(np.array([-1.56032026e+27,  1.28952087e+25,  1.68927235e+27])))/np.linalg.norm(np.array([8.22617883e+41, 2.60669176e+41, 3.13117308e+43])), #AM
    (np.linalg.norm(np.array([1.89928081e+17, 1.92786817e+17, 1.92069219e+17])))/np.linalg.norm(np.array([-4.31359973e+26, -1.27242245e+27,  4.19606590e+25])) #LM
]

fig = plt.figure(figsize = [10, 4], dpi = 150)

ax1, ax2, ax3 = fig.subplots(ncols = 3, sharey = 'col')

n = 0.2

ax1.bar(x = 0, height = data_1[0], color = 'r', width = n, label = 'Euler')
ax1.bar(x = 1, height = data_2[0], color = 'g', width = n, label = 'Euler-Cromer')
ax1.bar(x = 2, height = data_3[0], color = 'b', width = n, label = 'Euler-Richardson')

ax1.get_xaxis().set_ticks([])

ax1.set_xlabel('Energy')
ax1.set_ylabel('Conservation factor')

ax2.bar(x = 0, height = data_1[1], color = 'r', width = n, label = 'Euler')
ax2.bar(x = 1, height = data_2[1], color = 'g', width = n, label = 'Euler-Cromer')
ax2.bar(x = 2, height = data_3[1], color = 'b', width = n, label = 'Euler-Richardson')

ax2.get_xaxis().set_ticks([])

ax2.set_xlabel('Angular momentum')

ax3.bar(x = 0, height = data_1[2], color = 'r', width = n, label = 'Euler')
ax3.bar(x = 1, height = data_2[2], color = 'g', width = n, label = 'Euler-Cromer')
ax3.bar(x = 2, height = data_3[2], color = 'b', width = n, label = 'Euler-Richardson')

ax3.get_xaxis().set_ticks([])

ax3.set_xlabel('Linear momentum')

plt.legend()

#plt.show()

plt.savefig('conservation.svg')