import numpy as np
import matplotlib.pyplot as plt

'''
    Interprets an expression for a velocity fields and plots the streamlines
'''


def streamlines(u, limits= np.array([[-10,-10],[10,10]]), dt= 0.01):

    xmin = limits[0][0]
    xmax = limits[1][0]
    ymin = limits[0][1]
    ymax = limits[1][1]

    # creating a grid of initial points
    print('Creating Grid')
    x_values = np.linspace(xmin, xmax, 5)
    y_values = np.linspace(ymin, ymax, 5)
    grid = np.array([[x_values[i],y_values[j]] for i in range(len(x_values)) for j in range(len(y_values))])


    # for a specific streamline starting at x_init
    for i in range(len(grid)):

        x_init = grid[i]

        x_init = x_init.astype(np.float64)

        # forward streamline
        print('Calculating Forward Streamline')
        l_forward = np.array([x_init])

        x = x_init
        iterations = 0

        while xmin <= x[0] and xmax >= x[0] and ymin <= x[1] and ymax >= x[1] and iterations < 10000:
            l_forward = np.append(l_forward, np.array([x]), axis= 0)
            x = x + u(x)*dt
            iterations += 1

        # backward streamline
        print('Calculating Backward Streamline')
        l_backward = np.array([x_init])

        x = x_init
        iterations = 0

        while xmin <= x[0] and xmax >= x[0] and ymin <= x[1] and ymax >= x[1] and iterations < 10000:
            l_backward = np.append(l_backward, np.array([x]), axis= 0)
            x = x - u(x)*dt
            iterations += 1


        # combining forward and backward

        l = np.append(l_forward, l_backward, axis= 0)

        x = [x[0] for x in l]
        y = [x[1] for x in l]

        print('Plotting Streamline')
        plt.plot(x, y, color= 'b')



    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)
    plt.show()


# defining the velocity field

a = 1
b = 1

def u(x):
    return np.array([(b*x[0]-a*x[1])*(np.linalg.norm(x)),(a*x[0]+b*x[1])*(np.linalg.norm(x))])

streamlines(u)
