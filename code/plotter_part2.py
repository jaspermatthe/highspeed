import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

from part1 import *
from part2 import *

############
### DATA ###
############

# CONSTANTS
x = [44.8, 56.8, 59.8, 62.8, 74.8, 79.8, 84.8, 96.8, 99.8, 102.8, 114.8, 119.8, 124.8, 129.8, 134.8, 139.8, 144.8, 149.8, 154.8, 159.8, 164.8, 176.8, 179.8, 182.8, 194.8, 226.8, 254.8, 286.8, 314.8, 344.8, 376.8, 404.8, 434.8, 466.8, 494.8, 524.8, 556.8, 584.8, 614.8, 642.8, 674.8, 704.8, 734.8, 764.8, 796.8, 824.8, 854.8]
p_ratio = np.array([0.781381, 0.681254, 0.627379, 0.572096, 0.440294, 0.384134, 0.336203, 0.27019, 0.244047, 0.21753, 0.174522, 0.156648, 0.143651, 0.134892, 0.129972, 0.129501, 0.129057, 0.128039, 0.127851, 0.128469, 0.129768, 0.130833, 0.130729, 0.131342, 0.131452, 0.13329, 0.138981, 0.163118, 0.171505, 0.16189, 0.193759, 0.159079, 0.178082, 0.170626, 0.180855, 0.171606, 0.180789, 0.179816, 0.2132, 0.272552, 0.29942, 0.318293, 0.331491, 0.338732, 0.361007, 0.389107, 0.410095])

# LOCATION OF SHOCK WAVES
x_shock_3 = 630
x_shock_5 = 530
pe6_pt_shock_3, pe5_pt_shock_3, pe3_pt_shock_3 =  pressure_ratio_shock_location(x_shock_3)
pe6_pt_shock_5, pe5_pt_shock_5, pe3_pt_shock_5 =  pressure_ratio_shock_location(x_shock_5)


# EXPERIMENTAL PRESSURE RATIOS DATA
p_ratio_3 = []
p_ratio_4 = []
p_ratio_5 = []


save_to_folder = 'C://Users/matth/Documents/School/University/Delft/Courses/Year 2/Q2/Aero II/High Speed Practical/plots/'

markers = ['-.', '-o', '-v', '-x', '-s', '-D']



plt.grid()
# pressure ratios
plt.plot(x, p_ratio, '-o', color = "magenta", label='3A/B (Supersonic 630.0 mm)')
plt.plot(x, p_ratio, '-s', color = "cyan", label='4A/B (Supersonic 630.0 mm)')
plt.plot(x, p_ratio, '-x', color = "blue", label='5A/B (Subsonic)')

# shock locations
plt.axvline(x_shock_3, color = 'black', linestyle = '--')
plt.text(x_shock_3 - 30 , 0.5, '3 shockwave', rotation=90)

plt.axvline(x_shock_5, color = 'black', linestyle = '--')
plt.text(x_shock_5 - 30, 0.5, '5 shockwave', rotation=90)

# pressure ratio coordinates
# shockwave at 3
plt.plot(x_shock_3, pe3_pt_shock_3, marker="v", markersize=10, color = 'black', label = '$\mathregular{p/p_{t}}_{3}$')
plt.plot(x_shock_3, pe5_pt_shock_3, marker="^", markersize=10, color = 'black', label = '$\mathregular{p/p_{t}}_{5}$')
plt.plot(x_shock_3, pe6_pt_shock_3, marker="<", markersize=10, color = 'black', label = '$\mathregular{p/p_{t}}_{6}$')
# shockwave at 5
plt.plot(x_shock_5, pe3_pt_shock_5, marker="X", markersize=10, color = 'black', label = '$\mathregular{p/p_{t}}_{3}$')
plt.plot(x_shock_5, pe5_pt_shock_5, marker="D", markersize=10, color = 'black', label = '$\mathregular{p/p_{t}}_{5}$')
plt.plot(x_shock_5, pe6_pt_shock_5, marker="p", markersize=10, color = 'black', label = '$\mathregular{p/p_{t}}_{6}$')



plt.xlabel('Position along tunnel, x [mm]')
plt.ylabel('Pressure ratio $\mathregular{p/p_{t}}$ [-] [mm]')
plt.legend(loc='best')
plt.savefig(save_to_folder + 'pressure ratio versus position along tunnel')
plt.show()