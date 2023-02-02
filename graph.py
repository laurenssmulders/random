import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.sin(x)

xmin = -10
xmax = 10
n = 1000

x = np.linspace(xmin,xmax,n)

y = f(x)

plt.plot(x,y, color= 'b')
plt.xlim(xmin,xmax)
plt.show()

