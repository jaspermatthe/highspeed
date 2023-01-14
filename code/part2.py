"""
Part 2

-No theoretical lines to plot
-Just theoretical points of critical pressure ratios, 3,5, and 6 are needed
-Mach number at shock location will be input to find these pressure ratios
"""

import flowtools
import numpy

"""
CONSTANTS
"""
gamma = 1.4



def diffuser_geom(hk2, slope, h0):
    x_min = 410 
    x_max = 760

    x_along_diffuser = []
    diffuser_height=[]
    x = x_min
    while x <= 760:
        x_along_diffuser.append(x)
        x_ref = x - x_min
        h = slope * x_ref + h0
        diffuser_height.append(h)

        x += 10


    return x_along_diffuser, diffuser_height


# Group A Geometry (4: 15mm, 5: 10mm)
# diffuser_height = diffuser_geom(14.6, 0.01692, 8.0)

# Group B Geometry (4: 18mm, 5: 10mm)
x_along_diffuser, diffuser_height = diffuser_geom(11.8, 0.02472, 2.2)
print(x_along_diffuser)
print(diffuser_height)
