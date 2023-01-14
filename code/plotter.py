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

x_along_diffuser = [410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760] 
diffuser_height = [2.2, 2.4472, 2.6944, 2.9416, 3.1888, 3.436, 3.6832000000000003, 3.9304, 4.1776, 4.4248, 4.672000000000001, 4.9192, 5.166399999999999, 5.413600000000001, 5.6608, 5.9079999999999995, 6.1552, 6.4024, 6.6496, 6.8968, 7.144, 7.3911999999999995, 7.6384, 7.8856, 8.1328, 8.379999999999999, 8.6272, 8.8744, 9.1216, 9.3688, 9.616, 9.863199999999999, 10.110399999999998, 10.357600000000001, 10.604800000000001, 10.852]

# THEORETICAL
# import computed mach numbers and pressure ratios for sub and supersonic cases
# subsonic case needs a measured pressure ratio (p/p_t) at a known position
    # one_sub(position, pressure_ratio)
M_sup, p_ratio_sup = np.array(one_sup())
M_sub, p_ratio_sub = np.array(one_sub(45,0.89))


# EXPERIMENTAL (TO BE FILLED IN)
M_exp = -M_sup
p_ratio_exp = -p_ratio_sup

save_to_folder = 'C://Users/matth/Documents/School/University/Delft/Courses/Year 2/Q2/Aero II/High Speed Practical/plots/'

markers = ['-.', '-o', '-v', '-x', '-s', '-D']

"""
Part 2 Supersonic Plots
"""
# M_nom = 2.1, x_throat = 65.0 mm, h_throat = 16.34 mm

# f, (ax0,ax1,ax2) = plt.subplots(3)

# ax0.plot(x, A_ratio, '-s', color='black')
# ax0.set_ylabel('$\mathregular{A/A_{t}}$ [-]')

# ax1.plot(x, M_sub, '-x', color='green', label='theoretical')
# # ax1.plot(x, M_exp, '-v', color='red', label='experimental')
# ax1.set_ylabel('M [-]')
# ax1.legend(loc='best')

# ax2.plot(x, p_ratio_sub, '-x', color='green', label='theoretical')
# # ax2.plot(x, p_ratio_exp, '-v', color='red', label='experimental')
# ax2.set_ylabel('$\mathregular{p/p_{t}}$ [-]')
# ax2.legend(loc='best')

# ax0.grid()
# ax1.grid()
# ax2.grid()
# f.supxlabel('x [mm]')
# plt.savefig(save_to_folder + 'x vs M (fully subsonic case)')
# plt.show()



"""
Part 1 Supersonic Plots
"""
# M_nom = 2.1, x_throat = 65.0 mm, h_throat = 16.34 mm

# f, (ax0,ax1,ax2) = plt.subplots(3)

# ax0.plot(x, A_ratio, '-s', color='black')
# ax0.set_ylabel('$\mathregular{A/A_{t}}$ [-]')

# ax1.plot(x, M_sup, '-x', color='green', label='theoretical')
# ax1.plot(x, M_exp, '-v', color='red', label='experimental')
# ax1.set_ylabel('M [-]')
# ax1.legend(loc='best')

# ax2.plot(x, p_ratio_sup, '-x', color='green', label='theoretical')
# ax2.plot(x, p_ratio_exp, '-v', color='red', label='experimental')
# ax2.set_ylabel('$\mathregular{p/p_{t}}$ [-]')
# ax2.legend(loc='best')

# ax0.grid()
# ax1.grid()
# ax2.grid()
# f.supxlabel('x [mm]')
# plt.savefig(save_to_folder + 'x vs M (subsonic-supersonic case)')
# plt.show()

# $\mathregular{u_{p}(t)}$


plt.grid()
plt.plot(x_along_diffuser, diffuser_height, '-')
plt.xlabel('x_along_diffuser [mm]')
plt.ylabel('diffuser_height [mm]')
# plt.legend(loc='best')
plt.savefig(save_to_folder + 'diffuser geometry')
plt.show()