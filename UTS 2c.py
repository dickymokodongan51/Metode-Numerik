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

    # Tahap Eliminasi Maju
    for i in range(n):
        # 1. Pivoting - memastikan elemen diagonal (pivot) tidak nol
        if A[i][i] == 0:
            for k in range(i + 1, n):
                if A[k][i] != 0:
                    # Tukar baris jika ditemukan elemen non-nol
                    A[[i, k]] = A[[k, i]]
                    b[i], b[k] = b[k], b[i]
                    break
            else:
                # Jika pivot tetap nol, matriks dianggap singular
                raise ValueError("Matriks singular atau tidak memiliki solusi unik.")
        
        # 2. Normalisasi Baris Pivot
        pivot = A[i][i]
        A[i] = A[i] / pivot
        b[i] = b[i] / pivot

        # 3. Eliminasi Elemen di Bawah Pivot
        for j in range(i + 1, n):
            factor = A[j][i]
            A[j] = A[j] - factor * A[i]
            b[j] = b[j] - factor * b[i]

    # Tahap Substitusi Mundur
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = b[i] - np.dot(A[i, i + 1:], x[i + 1:])
    
    return x

# Definisi matriks A dan vektor b
A = np.array([[4, -1, -1],
              [-1, 3, -1],
              [-1, -1, 5]], dtype=float)
b = np.array([5, 3, 4], dtype=float)

# Menyelesaikan sistem menggunakan eliminasi Gauss
try:
    solusi_gauss = gauss_elimination(A.copy(), b.copy())
    print("Solusi sistem persamaan menggunakan eliminasi Gauss:", solusi_gauss)
except ValueError as e:
    print("Error:", e)
