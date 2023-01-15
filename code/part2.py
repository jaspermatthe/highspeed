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


"""
Diffuser Geometry
"""
def diffuser_geom(hk2, slope, h0):
    x_min = 410 
    x_max = 760
    step = 2

    x_along_diffuser = []
    diffuser_height = []
    area_ratio = []
    x = x_min
    while x <= x_max:
        x_along_diffuser.append(x)
        x_ref = x - x_min
        h_diffuse = slope * x_ref + h0
        h = h_diffuse + hk2
        diffuser_height.append(h)
        A_ratio = h / hk2
        area_ratio.append(A_ratio)

        x += 2


    return x_along_diffuser, diffuser_height, area_ratio


# Group A Geometry (4: 15mm, 5: 10mm)
# diffuser_height = diffuser_geom(14.6, 0.01692, 8.0)

# Group B Geometry (4: 18mm, 5: 10mm)
x_along_diffuser, diffuser_height, area_ratio = diffuser_geom(11.8, 0.02472, 2.2)
# print(x_along_diffuser)
# print(diffuser_height)
# print(area_ratio)



"""
Takes in location of a shock 
Computes the area ratio from the height distribution
Computes mach numnber from area ratio
Computes pressure ratio from mach number
"""
def pressure_ratio_shock_location(shock_location):
    pressure_ratio = 1
    area_ratio_local = numpy.interp(shock_location, x_along_diffuser, area_ratio)
    
    # (p/p_t)6
    # ideally expanded case
    # using isentropic relations (supersonic)
    output = flowtools.flowisentropic2(gamma, area_ratio_local, 'sup')
    Me6 = output[0]
    pe6_pt = output[2]

    # (p/p_t)5
    # using normal shock relations to 'jump' back to (p/p_t)6 right after shock
    output = flowtools.flownormalshock2(gamma, Me6, 'mach') # Me6 is actually downstream but we take it as upstream 
    pe5_pe6 = output[2] # output is downstream/upstream but since we reversed mach input this does not need reciprocal
    pe5_pt = pe5_pe6 * pe6_pt

    # (p/p_t)3
    # using isentropic flow relations (subsonic)
    output = flowtools.flowisentropic2(gamma, area_ratio_local, 'sub')
    Me3 = output[0]
    pe3_pt = output[2]


    return pe6_pt, pe5_pt, pe3_pt

pe6_pt, pe5_pt, pe3_pt =  pressure_ratio_shock_location(630)
print(f"pe6_pt {pe6_pt}, pe5/pt {pe5_pt}, pe3/pt {pe3_pt}")
