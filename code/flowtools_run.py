import flowtools

gamma = 1.4

out = flowtools.flowisentropic2(gamma,0.0585,'pres')
print(out)

out2 = flowtools.flownormalshock2(gamma,2.5,'mach')
print(out2)

