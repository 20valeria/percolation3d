import numpy as np
import percolation3dio
from collections import deque

def _flow(isOpen, isFull, start):
    """
    Вспомогательная функция для заполнения открытых ячеек в трехмерной сетке без использования рекурсии.

    Параметры:
    isOpen (numpy.ndarray): Трехмерный массив, указывающий, открыта ли каждая ячейка.
    isFull (numpy.ndarray): Трехмерный массив, указывающий, заполнена ли каждая ячейка.
    start (tuple): Кортеж, содержащий начальные индексы (i, j, k).

    Функция модифицирует массив `isFull`, отмечая ячейки как заполненные (True), если они достижимы.
    """
    stack = [start]
    visited = set([start])
    n = len(isFull)
    while stack:
        i, j, k = stack.pop()

        if (i < 0 or i >= n or j < 0 or j >= n or k < 0 or k >= n):
            continue
        if (not isOpen[i][j][k] or isFull[i][j][k]):
            continue

        isFull[i][j][k] = True

        for di, dj, dk in [ (0, 0, -1), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]:
            ni, nj, nk = i + di, j + dj, k + dk
            if (ni, nj, nk) not in visited:
                stack.append((ni, nj, nk))
                visited.add((ni, nj, nk))

def flow(isOpen):
    """
    Заполняет трехмерную сетку водой, начиная с верхнего слоя.

    Параметры:
    isOpen (numpy.ndarray): Трехмерный массив, указывающий, открыта ли каждая ячейка.

    Возвращает:
    numpy.ndarray: Массив, отображающий заполненные ячейки в трехмерной сетке.
    """
    n = len(isOpen)
    isFull = np.zeros((n, n, n), dtype=bool)
    for j in range(n):
        for k in range(n):
            _flow(isOpen, isFull, (0, j, k))
    return isFull

def optimized_flow(isOpen):
    n = isOpen.shape[0]
    isFull = np.zeros_like(isOpen, dtype=bool)
    queue = deque()

    # Инициализируем очередь всеми ячейками в верхнем слое, которые открыты
    for j in range(n):
        for k in range(n):
            if isOpen[0, j, k]:
                queue.append((0, j, k))
                isFull[0, j, k] = True

    # Направления распространения: вверх, вниз, влево, вправо, перед, зад
    directions = [ (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    while queue:
        i, j, k = queue.popleft()
        for di, dj, dk in directions:
            ni, nj, nk = i + di, j + dj, k + dk
            if 0 <= ni < n and 0 <= nj < n and 0 <= nk < n and not isFull[ni, nj, nk] and isOpen[ni, nj, nk]:
                isFull[ni, nj, nk] = True
                queue.append((ni, nj, nk))

    return isFull







def percolates(isOpen):
    """
    Проверяет, существует ли путь через открытые ячейки от верхнего слоя сетки к нижнему.

    Параметры:
    isOpen (numpy.ndarray): Трехмерный массив, указывающий, открыта ли каждая ячейка.

    Возвращает:
    bool: True, если существует путь от верха к низу сетки, иначе False.
    """
    isFull = flow(isOpen)
    n = len(isFull)
    for j in range(n):
        for k in range(n):
            if isFull[n - 1][j][k]:
                return True
    return False



if __name__ == "__main__":
    test = percolation3dio.random(10,0.6)
    a = percolates(test)
    print(a)