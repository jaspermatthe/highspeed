"""
Part 1

- Data collected around the first throat only
- Code below returns p/p_t and M from x = 44.8 [mm] until x = 194.8 [mm] for the two following cases:
    1. fully subsonic conditions (isentropic flow)
    2. supersonic after throat (isentropic flow)
"""

import flowtools
import numpy

gamma = 1.4

# Position, x, along test section from 44.8 to 194.8 [mm]
x = [44.8, 56.8, 59.8, 62.8, 74.8, 79.8, 84.8, 96.8, 99.8, 102.8, 114.8, 119.8, 124.8, 129.8, 134.8, 139.8, 144.8, 149.8, 154.8, 159.8, 164.8, 176.8, 179.8, 182.8, 194.8]

# Height, h, along test section from positions x = 44.8 to x = 194.8 [mm]
h = [19.204, 16.819, 16.532, 16.372, 16.958, 17.664, 18.553, 21.067, 21.698, 22.306, 24.488, 25.275, 25.992, 26.638, 27.219, 27.734, 28.188, 28.584, 28.924, 29.212, 29.45, 29.832, 29.89, 29.935, 30.0]

# A/A_t ratio along test section from positions x = 44.8 to x = 194.8 [mm]
A_ratio = [1.175, 1.029, 1.012, 1.002, 1.038, 1.081, 1.136, 1.29, 1.328, 1.365, 1.499, 1.547, 1.591, 1.631, 1.666, 1.698, 1.725, 1.75, 1.77, 1.788, 1.803, 1.826, 1.83, 1.832, 1.836]


"""Default Ouput Formats"""
# flowisentropic2: (MACH, T, P, RHO, A)
# flownormalshock2: (MACH, T, P, RHO, M, P0, P1)

# interpolate area ratio from position x
def interpolate_area(position) -> int:
    if position < x[0] or position > x[-1]:
        return "Sorry outside of domain"
    elif position >= x[0] and position <= x[-1]:
        # within domain
        area = numpy.interp(position, x, A_ratio)

    return area


"""
2. supersonic after throat

- Uses isentropic flow relations
- Specifies if before (subsonic) or after (supersonic) throat
since the area-mach relation outputs both a sub and supersonic 
mach number for a given area ratio
"""
def one_sup():
    # compute all mach numbers before and after throat using given area ratios
    mach = []
    counter = 0
    for area in A_ratio:
        # if before throat (sub)
        if counter < 4:
            output = (flowtools.flowisentropic2(gamma,area,'sub'))

        # if after throat (sup)
        if counter > 3:
            output = (flowtools.flowisentropic2(gamma,area,'sup'))

        mach.append(output[0])
        counter += 1


    # compute all pressure ratios before and after throat
    pressure_ratio = []
    for mach_number in mach:
        output = (flowtools.flowisentropic2(gamma,mach_number,'mach'))
        pressure_ratio.append(output[2])


    return mach, pressure_ratio



"""
1. fully subsonic conditions

Must use reference area ratios to legally use area-mach relation
"""

def one_sub(position_measured, pressure_ratio_measured):
    # pressure_ratio_measured should be p/p_t
    mach = []
    pressure_ratio = []

    # A. use pressure_ratio_measured (p/p_t) at position_measured (x_0) to determine A(x_0)/A* from isentropic relations
    output = (flowtools.flowisentropic2(gamma,pressure_ratio_measured,'pres'))
    Ax0_Astar = output[4]

    # B. read A_t/A(x_0) from given geometry
    At_Ax0 = 1 / interpolate_area(position_measured) # need reciprocal since area ratio list was A(x)/A_t

    # C. compute coefficient A_t/A* = A(x_0)/A* A_t/A(x_0) from above ratios
    At_Astar = Ax0_Astar * At_Ax0

    # D. convert local geometric area ratio to local sonic area ratio via above coefficient, A(x)/A* = A_t/A* A(x)/A_t
    local_sonic_area_ratio = []
    for area in A_ratio:
        Ax_Astar = At_Astar * area
        local_sonic_area_ratio.append(Ax_Astar)

    breakpoint()
    # E. use these local sonic area ratios to compute the subsonic mach numbers and pressure ratios
    # they should not be more than 1 i think
    for value in local_sonic_area_ratio:
        output = (flowtools.flowisentropic2(gamma,value,'sub'))

        mach.append(output[0])
        pressure_ratio.append(output[2])


    return mach, pressure_ratio

mach_sup, pressure_ratio_sup = one_sup()
mach_sub, pressure_ratio_sub = one_sub(45,0.997009)
print(mach_sub)

