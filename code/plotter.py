import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

from part1 import *

"""
Part 1 Data
"""
# CONSTANTS
x = [44.8, 56.8, 59.8, 62.8, 74.8, 79.8, 84.8, 96.8, 99.8, 102.8, 114.8, 119.8, 124.8, 129.8, 134.8, 139.8, 144.8, 149.8, 154.8, 159.8, 164.8, 176.8, 179.8, 182.8, 194.8]
y = [19.204, 16.819, 16.532, 16.372, 16.958, 17.664, 18.553, 21.067, 21.698, 22.306, 24.488, 25.275, 25.992, 26.638, 27.219, 27.734, 28.188, 28.584, 28.924, 29.212, 29.45, 29.832, 29.89, 29.935, 30.0]
A_ratio = [1.175, 1.029, 1.012, 1.002, 1.038, 1.081, 1.136, 1.29, 1.328, 1.365, 1.499, 1.547, 1.591, 1.631, 1.666, 1.698, 1.725, 1.75, 1.77, 1.788, 1.803, 1.826, 1.83, 1.832, 1.836]

# THEORETICAL
# M = np.array([0.6114721591994688, 0.8240924123910661, 0.8842711568403594, 0.9516961340885424, 1.2244269375297963, 1.3330989336073804, 1.4368158908660429, 1.647454595606023, 1.6897282789409802, 1.7284633803755622, 1.8532673616015025, 1.89331622031482, 1.928291438228662, 1.9587954018140197, 1.9845661099439407, 2.0074328406051296, 2.026242969092337, 2.0432866257045332, 2.0566749932653243, 2.0685444242640676, 2.0783094575541243, 2.0930671152404665, 2.0956077009956875, 2.0968751575522995, 2.099404430690951])
# p_ratio = np.array([0.7769301794549013, 0.640337791078573, 0.60136572477909, 0.5583912544129024, 0.3993745365979945, 0.34492887454285887, 0.29827918143282256, 0.21922762569214674, 0.20575395888348919, 0.19406207265491093, 0.16038705399322264, 0.15078793418137823, 0.14285067958591638, 0.13625384368347193, 0.13090863961239077, 0.12633503638686486, 0.12268879899274424, 0.1194731756620722, 0.11700476514669463, 0.1148579897494271, 0.11312068893329402, 0.11054380008497391, 0.11010601652704768, 0.10988824929226905, 0.10945494527261293])

# import camputed mach numbers and pressure ratios for sub and supersonic cases
# subsonic case needs a measured pressure ratio (p/p_t) at a known position
    # one_sub(position, pressure_ratio)
M_sup, p_ratio_sup = np.array(one_sup())
M_sub, p_ratio_sub = np.array(one_sub(45,0.89))


# EXPERIMENTAL
M_exp = -M_sup
p_ratio_exp = -p_ratio_sup

save_to_folder = 'C://Users/matth/Documents/School/University/Delft/Courses/Year 2/Q2/Aero II/High Speed Practical/plots/'

markers = ['-.', '-o', '-v', '-x', '-s', '-D']

"""
Part 2 Supersonic Plots
"""
# M_nom = 2.1, x_throat = 65.0 mm, h_throat = 16.34 mm

f, (ax0,ax1,ax2) = plt.subplots(3)

ax0.plot(x, A_ratio, '-s', color='black')
ax0.set_ylabel('$\mathregular{A/A_{t}}$ [-]')

ax1.plot(x, M_sub, '-x', color='green', label='theoretical')
# ax1.plot(x, M_exp, '-v', color='red', label='experimental')
ax1.set_ylabel('M [-]')
ax1.legend(loc='best')

ax2.plot(x, p_ratio_sub, '-x', color='green', label='theoretical')
# ax2.plot(x, p_ratio_exp, '-v', color='red', label='experimental')
ax2.set_ylabel('$\mathregular{p/p_{t}}$ [-]')
ax2.legend(loc='best')

ax0.grid()
ax1.grid()
ax2.grid()
f.supxlabel('x [mm]')
plt.savefig(save_to_folder + 'x vs M (fully subsonic case)')
plt.show()



"""
Part 1 Supersonic Plots
"""
# M_nom = 2.1, x_throat = 65.0 mm, h_throat = 16.34 mm

f, (ax0,ax1,ax2) = plt.subplots(3)

ax0.plot(x, A_ratio, '-s', color='black')
ax0.set_ylabel('$\mathregular{A/A_{t}}$ [-]')

ax1.plot(x, M_sup, '-x', color='green', label='theoretical')
ax1.plot(x, M_exp, '-v', color='red', label='experimental')
ax1.set_ylabel('M [-]')
ax1.legend(loc='best')

ax2.plot(x, p_ratio_sup, '-x', color='green', label='theoretical')
ax2.plot(x, p_ratio_exp, '-v', color='red', label='experimental')
ax2.set_ylabel('$\mathregular{p/p_{t}}$ [-]')
ax2.legend(loc='best')

ax0.grid()
ax1.grid()
ax2.grid()
f.supxlabel('x [mm]')
plt.savefig(save_to_folder + 'x vs M (subsonic-supersonic case)')
plt.show()

# $\mathregular{u_{p}(t)}$