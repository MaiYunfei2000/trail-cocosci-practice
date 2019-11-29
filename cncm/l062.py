# listing 6.2 simple integrate and fire model in Python

import matplotlib.pyplot as plt

r = 1 # resistance, is a constant
c = 1 # capacitance, is a constant
tau = r*c # τ, is a constant
dt = 0.05 # change in time, is a constant
t = 0 # time, is an independent variable
v = 0 # volt, is a dependent variable
threshold = 5 # is a constant
i = [] # create list i, means current??????
tdata = [] # initialize tdata
vdata = [] # initialize vdata

# these two "for"s represent the variation of the current "I"

# This will be our current pulse
for z in range(0, 40):
    num = 10
    i.append(num)
    #print('i:', i) # debug use

# Now return input current to zero
for z in range(40, 75):
    num = 0
    i.append(num)
    #print('i:', i) # debug use

# This loop calculates our voltage
for j in range(0, 75):
    # what does this line mean?
    dvdt = (1/tau) * (r*i[j] - v)
        # calculate dv/dt, represents the rate of change of voltage as a function of time, ref the equation on page45
        # i[j] means the j-th element of the list "i"
        # the initial "v" is 0
    v = v + dvdt*dt
    if v > threshold:
        v = 0
    t = t + dt # change of time
    tdata.append(t)
    vdata.append(v)

# plot the data using "tdata" as the independent variable and vdata as the dependent variable
plt.plot(tdata, vdata)
# [matplotlib.pyplot.axis — Matplotlib 3.1.1 documentation](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.axis.html)
plt.axis([0, t, -1, 7])
    # set some axis properties
    # scale of axes:
        # xmin = 0, xmax = t(namely 3.75), ymin = -1, ymax = 7
# apply the label for the x axis
plt.xlabel('Time')
# apply the label for the y axis
plt.ylabel('Voltage (arbitrary units)')
plt.show()