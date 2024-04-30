import sys
import percolation3d
import percolation3dio

def evaluate(n, р, trials):
    """
    Вычисляет вероятность протекания в трехмерной сетке.
    
    Параметры:
    n (int): Размер сетки (n x n x n).
    p (float): Вероятность того, что ячейка сетки будет открыта.
    trials (int): Количество испытаний для оценки вероятности проcfxbdfybz.
    
    Возвращает:
    float: Оцененная вероятность протекания через сетку.
    """
    count = 0
    for i in range(trials):
        isOpen = percolation3dio.random(n, р)
        if (percolation3d.percolates( isOpen )):
            count += 1
    return (1.0 * count / trials)*100


def main( ):
    n = int(sys.argv[1])
    р = float(sys.argv[2])
    trials = int(sys.argv[3])
    q = evaluate(n, р, trials)
    print(q)


if __name__ == "__main__":
    main( )