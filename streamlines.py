import numpy as np
import matplotlib.pyplot as plt

'''
    Interprets an expression for a velocity fields and plots the streamlines
'''


def streamlines(u, limits= np.array([[-10,-10],[10,10]]), dt= 0.1):

    xmin = limits[0][0]
    xmax = limits[1][0]
    ymin = limits[0][1]
    ymax = limits[1][1]

    # creating a grid of initial points
    x_values = np.linspace(xmin, xmax, 10)
    y_values = np.linspace(ymin, ymax, 10)
    grid = np.array([[x_values[i],y_values[j]] for i in range(len(x_values)) for j in range(len(y_values))])



    # for a specific streamline starting at x_init
    for i in range(len(grid)):

        x_init = grid[i]

        x_init = x_init.astype(np.float64)

        # forward streamline

        l_forward = np.array([x_init])

        x = x_init

        while xmin <= x[0] and xmax >= x[0] and ymin <= x[1] and ymax >= x[1]:
            l_forward = np.append(l_forward, np.array([x]), axis= 0)
            x = x + u(x)*dt

        # backward streamline

        l_backward = np.array([x_init])

        x = x_init

        while xmin <= x[0] and xmax >= x[0] and ymin <= x[1] and ymax >= x[1]:
            l_backward = np.append(l_backward, np.array([x]), axis= 0)
            x = x - u(x)*dt


        # combining forward and backward

        l = np.append(l_forward, l_backward, axis= 0)

        x = [x[0] for x in l]
        y = [x[1] for x in l]


        plt.plot(x, y, color= 'b')



    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)
    plt.show()


# defining the velocity field

a = 1
b = 1

def u(x):
    return np.array([(b*x[0]-a*x[1])/((x[0]**2+x[1]**2)**0.5),(a*x[0]+b*x[1])/((x[0]**2+x[1]**2)**0.5)])

streamlines(u)
