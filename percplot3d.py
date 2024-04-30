import numpy as np
import matplotlib.pyplot as plt
import sys
import estimate3d


def estimate_evaluate(n, x, trials):
    """
    Пример функции оценки для демонстрации, возвращает значение функции sin(pi * x).

    Параметры:
    n (int): Не используется в данной функции, предназначен для согласования сигнатуры с другими функциями.
    x (float): Входное значение для оценки функции.
    trials (int): Не используется в данной функции, предназначен для согласования сигнатуры с другими функциями.

    Возвращает:
    float: Результат вычисления функции sin(pi * x) для заданного x.
    """
    return np.sin(np.pi * x)


def curve(n, x0, y0, x1, y1, trials=100, gap=0.01, err=0.0025):
    """
    Рекурсивно рисует кривую, адаптируясь к изменениям в функции оценки.

    Параметры:
    n (int): Параметр, передаваемый в функцию оценки.
    x0, y0 (float): Начальная точка кривой.
    x1, y1 (float): Конечная точка кривой.
    trials (int, опционально): Количество испытаний для функции оценки.
    gap (float, опционально): Минимальное расстояние между точками для остановки рекурсии.
    err (float, опционально): Максимально допустимая ошибка между оценкой и средней точкой.
    """
    xm = (x0 + x1) / 2.0
    ym = (y0 + y1) / 2.0
    fxm = estimate3d.evaluate(n, xm, trials)

    if (x1 - x0 < gap) or (abs(ym - fxm) < err):
        plt.plot([x0, x1], [y0, y1], 'k-', lw=1)
        return

    curve(n, x0, y0, xm, fxm, trials, gap, err)
    plt.plot(xm, fxm, 'ko', markersize=2)
    curve(n, xm, fxm, x1, y1, trials, gap, err)



if __name__ == "__main__":
    """
    Выполняет визуализацию адаптивной кривой, используя рекурсивную функцию curve.
    """
    n = int(sys.argv[1])  # Получает значение n из аргументов командной строки
    plt.figure(figsize=(8, 6))
    plt.gca().set_aspect('equal', adjustable='box')
    curve(n, 0.0, 0.0, 1.0, 1.0)
    plt.xlim(0.0, 1.0)
    plt.ylim(0.0, 1.0)
    plt.show()
