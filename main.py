import numpy as np

def read_matrix(path):
    with open(path, 'r') as file:
        n = int(file.readline())
        matrix = np.zeros((n, n), dtype=int)
        for i in range(n):
            matrix[i] = list(map(int, file.readline().split()))
        return matrix

A = read_matrix("input.txt")
print(np.trace(A))
