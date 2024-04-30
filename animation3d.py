import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def update_flow_3d(isOpen, isFull, n):
    updated = False
    neighbor_offsets = np.array([(0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)])  # Порядок важен для направления

    for i, j, k in np.ndindex(isFull.shape):
        if isFull[i, j, k]:
            neighbors = [np.array([i, j, k]) + offset for offset in neighbor_offsets]
            for ni, nj, nk in neighbors:
                if 0 <= ni < n and 0 <= nj < n and 0 <= nk < n:
                    if isOpen[ni, nj, nk] and not isFull[ni, nj, nk]:
                        isFull[ni, nj, nk] = True
                        updated = True
    return updated

def init():
    ax.voxels(isOpen, facecolors='white', edgecolor='none', alpha=0.1)
    return fig,

def update(frame):
    if update_flow_3d(isOpen, isFull, n):
        ax.cla()
        filled_color = [0, 0, 1, 0.5]  # Синий для заполненных
        open_color = [1, 1, 1, 0.5]  # Белый для открытых
        colors = np.empty(isOpen.shape + (4,), dtype=np.float32)
        colors[isOpen & ~isFull] = open_color
        colors[isFull] = filled_color
        ax.voxels(isOpen, facecolors=colors, edgecolor='none')
    return fig,

n = 15
p = 0.5

isOpen = np.random.rand(n, n, n) < p
isFull = np.zeros((n, n, n), dtype=bool)
isFull[:, :, n-1] = isOpen[:, :, n-1]  # Заполнение начинается с верхней грани по оси z

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ani = FuncAnimation(fig, update, frames=200, init_func=init, blit=False, interval=200, repeat=False)
plt.show()
