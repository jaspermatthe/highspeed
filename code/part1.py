import flowtools


gamma = 1.5

# Position, x, along test section from 44.8 to 194.8 [mm]
x = [44.8, 56.8, 59.8, 62.8, 74.8, 79.8, 84.8, 96.8, 99.8, 102.8, 114.8, 119.8, 124.8, 129.8, 134.8, 139.8, 144.8, 149.8, 154.8, 159.8, 164.8, 176.8, 179.8, 182.8, 194.8]

# Height, h, along test section from positions x = 44.8 to x = 194.8 [mm]
h = [19.204, 16.819, 16.532, 16.372, 16.958, 17.664, 18.553, 21.067, 21.698, 22.306, 24.488, 25.275, 25.992, 26.638, 27.219, 27.734, 28.188, 28.584, 28.924, 29.212, 29.45, 29.832, 29.89, 29.935, 30.0]

# A/A_t ratio along test section from positions x = 44.8 to x = 194.8 [mm]
A_ratio = [1.175, 1.029, 1.012, 1.002, 1.038, 1.081, 1.136, 1.29, 1.328, 1.365, 1.499, 1.547, 1.591, 1.631, 1.666, 1.698, 1.725, 1.75, 1.77, 1.788, 1.803, 1.826, 1.83, 1.832, 1.836]


"""Default Ouput Formats"""
# flowisentropic2: (MACH, T, P, RHO, A)
# flownormalshock2: (MACH, T, P, RHO, M, P0, P1)

"""Supersonic Flow Case"""
# compute all mach numbers before and after throat
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
# print(pressure_ratio)



"""Subsonic Flow Case"""


