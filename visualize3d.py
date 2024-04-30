import sys
import numpy as np
import matplotlib.pyplot as plt
import percolation3d
import percolation3dio

n = int(sys.argv[1])
p = float(sys.argv[2])
trials = int(sys.argv[3])

for i in range(trials):
    isOpen = percolation3dio.random(n, p)
    percolation3dio.draw(isOpen)
    plt.show()

    isFull = percolation3d.flow(isOpen)
    isFull = percolation3d.optimized_flow(isOpen)

    visualization_matrix = np.where(isFull, 2, isOpen)

    percolation3dio.draw(visualization_matrix)
    plt.show()