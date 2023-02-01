import numpy as np
import matplotlib.pyplot as plt

'''
    Interprets an expression for a velocity fields and plots the streamlines
'''

# defining the velocity field

def u(x):
    return np.array([1,1])

# for a specific streamline starting at x_init

x_init = np.array([0,0])

x_init = x_init.astype(np.float64)

# defining limits

xmin = -10
xmax = 10
ymin = -10
ymax = 10


# forward streamline

l_forward = np.array([[]])

x = x_init
dt = 0.01

while xmin <= x[0] and xmax >= x[0] and ymin <= x[1] and ymax >= x[1]:
    np.append(l_forward, np.array([x]), axis= 1)
    x += u(x)*dt

print(l_forward)
# backward streamline

l_backward = np.array([[]])

x = x_init
dt = 0.01

while xmin <= x[0] and xmax >= x[0] and ymin <= x[1] and ymax >= x[1]:
    np.append(l_backward, np.array([x]), axis= 1)
    x -= u(x)*dt


# combining forward and backward

l = l_backward + l_forward

print(l)


plt.plot(l)
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)
plt.show()

