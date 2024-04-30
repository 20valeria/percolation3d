import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

def update_flow_3d(isOpen, isFull, n):
    """
    Обновляет состояние заполненности трехмерной сетки на основе соседних ячеек.

    Параметры:
    isOpen (numpy.ndarray): Трехмерный массив, показывающий открытость ячеек.
    isFull (numpy.ndarray): Трехмерный массив, показывающий заполненность ячеек.
    n (int): Размер сетки по каждому измерению.

    Возвращает:
    bool: True, если было выполнено какое-либо обновление; иначе False.
    """

    updated = False
    # Индексы соседних ячеек
    neighbor_offsets = np.array([(1, 0, 0), (0, 1, 0), (0, -1, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1)])

    # Итерация по всем ячейкам
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
    """
    Инициализирует визуализацию трехмерной сетки перед началом анимации.

    Возвращает:
    tuple: Кортеж, содержащий объект фигуры.
    """
    ax.cla()
    # Начальная визуализация
    ax.voxels(isOpen, facecolors='white', edgecolor='none', alpha=0.1)
    return fig,


def update(frame):
    """
    Обновляет состояние визуализации для каждого кадра анимации.

    Параметры:
    frame: Номер текущего кадра анимации.

    Возвращает:
    tuple: Кортеж, содержащий объект фигуры.
    """
    if update_flow_3d(isOpen, isFull, n):
        ax.cla()
        filled_color = [0, 0, 1, 0.5]  # Прозрачно-голубой для значений 2
        open_color = [1, 1, 1, 0.5]  # Белый для значений 1

        colors = np.empty(isOpen.shape + (4,), dtype=np.float32)
        colors[isOpen & ~isFull] = open_color
        colors[isFull] = filled_color

        ax.voxels(isOpen, facecolors=colors, edgecolor= 'none')

    return fig,


n = 10
p = 0.5  

isOpen = np.random.rand(n, n, n) < p
isFull = np.zeros((n, n, n), dtype=bool)
isFull[0, :, :] = isOpen[0, :, :]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ani = FuncAnimation(fig, update, frames=400, init_func=init, blit=False, interval=100, repeat=False)
plt.show()
