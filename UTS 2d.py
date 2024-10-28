import numpy as np

def gauss_jordan(A, b):
    n = len(b)
    for i in range(n):
        if A[i][i] == 0:
            for k in range(i + 1, n):
                if A[k][i] != 0:
                    A[[i, k]] = A[[k, i]]
                    b[i], b[k] = b[k], b[i]
                    break
            else:
                raise ValueError("Matriks singular atau sistem tidak memiliki solusi unik.")
        pivot = A[i][i]
        A[i] = A[i] / pivot
        b[i] = b[i] / pivot
        for j in range(n):
            if j != i:
                factor = A[j][i]
                A[j] = A[j] - factor * A[i]
                b[j] = b[j] - factor * b[i]
    return b

def gauss_elimination(A, b):
    n = len(b)
    for i in range(n):
        if A[i][i] == 0:
            for k in range(i + 1, n):
                if A[k][i] != 0:
                    A[[i, k]] = A[[k, i]]
                    b[i], b[k] = b[k], b[i]
                    break
            else:
                raise ValueError("Matriks singular atau sistem tidak memiliki solusi unik.")
        pivot = A[i][i]
        A[i] = A[i] / pivot
        b[i] = b[i] / pivot
        for j in range(i + 1, n):
            factor = A[j][i]
            A[j] = A[j] - factor * A[i]
            b[j] = b[j] - factor * b[i]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = b[i] - np.dot(A[i, i + 1:], x[i + 1:])
    return x

# Definisi matriks A dan vektor b
A = np.array([[4, -1, -1],
              [-1, 3, -1],
              [-1, -1, 5]], dtype=float)
b = np.array([5, 3, 4], dtype=float)

# Solusi menggunakan metode Gauss-Jordan
try:
    solusi_gauss_jordan = gauss_jordan(A.copy(), b.copy())
    print("Solusi sistem persamaan menggunakan Gauss-Jordan:", solusi_gauss_jordan)
except ValueError as e:
    print("Error:", e)

# Solusi menggunakan eliminasi Gauss
try:
    solusi_gauss = gauss_elimination(A.copy(), b.copy())
    print("Solusi sistem persamaan menggunakan eliminasi Gauss:", solusi_gauss)
except ValueError as e:
    print("Error:", e)

# Menampilkan solusi pada plot
labels = ['I1', 'I2', 'I3']
x = np.arange(len(labels))
width = 0.3

