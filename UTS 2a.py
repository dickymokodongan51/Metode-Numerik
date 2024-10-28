import numpy as np

def gauss_elimination(A, b):
    """
    Menyelesaikan sistem persamaan linear Ax = b menggunakan metode eliminasi Gauss.
    
    Parameter:
    A : np.array : Matriks koefisien
    b : np.array : Vektor hasil
    
    Return:
    np.array : Vektor solusi
    """
    n = len(b)

    # Proses eliminasi maju
    for i in range(n):
        # Memeriksa pivot untuk menghindari pembagian dengan nol
        if A[i][i] == 0:
            # Cari baris non-nol di bawah baris i
            for k in range(i + 1, n):
                if A[k][i] != 0:
                    # Tukar baris
                    A[[i, k]] = A[[k, i]]
                    b[i], b[k] = b[k], b[i]
                    break
            else:
                raise ValueError("Matriks singular atau sistem tidak memiliki solusi unik.")
        
        # Normalisasi baris pivot
        pivot = A[i][i]
        A[i] = A[i] / pivot
        b[i] = b[i] / pivot

        # Eliminasi elemen di bawah pivot
        for j in range(i + 1, n):
            factor = A[j][i]
            A[j] = A[j] - factor * A[i]
            b[j] = b[j] - factor * b[i]

    # Back substitution untuk menemukan solusi
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = b[i] - np.dot(A[i, i + 1:], x[i + 1:])
    
    return x

# Matriks A dan vektor b dari soal
A = np.array([[4, -1, -1],
              [-1, 3, -1],
              [-1, -1, 5]], dtype=float)
b = np.array([5, 3, 4], dtype=float)

# Menyelesaikan sistem menggunakan metode eliminasi Gauss
try:
    solusi_gauss = gauss_elimination(A.copy(), b.copy())
    print("Solusi sistem persamaan menggunakan eliminasi Gauss:", solusi_gauss)
except ValueError as e:
    print("Error:", e)
