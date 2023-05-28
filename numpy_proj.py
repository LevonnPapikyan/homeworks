#open comment if you run in jupyter-notebook
#%matplotlib notebook

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def create_universe(N=50, p=0.5):
    return np.random.choice([0, 1], size=(N, N), p=[1-p, p])

def animate(frame, universe, img):
    new_universe = np.zeros((N+2, N+2))
    new_universe[1:-1, 1:-1] = universe
    for i in range(1, N+1):
        for j in range(1, N+1):
            n = (new_universe[i+1][j] + new_universe[i-1][j]
                 + new_universe[i][j+1] + new_universe[i][j-1]
                 + new_universe[i+1][j+1] + new_universe[i-1][j-1]
                 + new_universe[i+1][j-1] + new_universe[i-1][j+1])
            if new_universe[i][j] == 0 and n == 3:
                universe[i-1][j-1] = 1
            elif new_universe[i][j] == 1 and (n < 2 or n > 3):
                universe[i-1][j-1] = 0
            else:
                universe[i-1][j-1] = new_universe[i][j]
    img.set_data(universe)
    return img

N = 50
universe = create_universe(N=N, p=0.5)
fig = plt.figure(figsize=(7, 7))
ax = plt.axes()
img = ax.imshow(universe, interpolation='nearest')
ani = FuncAnimation(fig, animate, fargs=(universe, img,),
                    frames=None, interval=500, save_count=50)

plt.show() 