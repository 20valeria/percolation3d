import sys
import numpy as np
import matplotlib.pyplot as plt


def random(n: int, p):
    """
    Генерирует трехмерную сетку с заданными размерами, где каждая ячейка случайным образом заполнена 0 или 1.

    Параметры:
    n (int): Размер сетки по каждому измерению.
    p (float): Вероятность того, что ячейка будет заполнена (1).

    Возвращает:
    numpy.ndarray: Трехмерный массив с размерами n x n x n, заполненный 0 или 1.
    """
    a = np.random.choice([1, 0], size=(n, n, n), p=[p, 1 - p])
    return a

#
def draw(matrix):
    """
    Визуализирует трехмерную сетку с использованием различных цветов для разных значений элементов массива.

    Параметры:
    matrix (numpy.ndarray): Трехмерный массив, который будет визуализирован.
    """
    # Перестановка слоев в матрице, чтобы синие (значение 2) были наверху
    n = len(matrix)
    axes = [n, n, n]

    # Определение цветов
    colors = np.empty(axes + [4], dtype=np.float32)
    colors[1] = [1, 1, 1, 0.5]  # Белый для 1
    colors[0] = [0, 0, 0, 0.5]  # Чёрный для 0
    colors[2] = [0, 0, 1, 0.5]  # Синий для 2 (предполагается наличие элементов со значением 2)


    # Визуализация
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.voxels(matrix == 1, facecolors=np.broadcast_to(colors[1], matrix.shape + (4,)), edgecolors='grey')  # Белый для 1
    ax.voxels(matrix == 0, facecolors=np.broadcast_to(colors[0], matrix.shape + (4,)),
              edgecolors='grey')  # Чёрный для 0
    ax.voxels(matrix == 2, facecolors=np.broadcast_to(colors[2], matrix.shape + (4,)), edgecolors='grey')  # Синий для 2



    plt.show()
#
def main():
    """
    Основная функция для генерации и визуализации трехмерной сетки.
    """
    n = int(sys.argv[1])  
    p = float(sys.argv[2])  
    test = random(n, p)  
    draw(test)  


if __name__ == "__main__":
    main()
