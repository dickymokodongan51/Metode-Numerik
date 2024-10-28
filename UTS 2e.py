import numpy as np

def determinant(matrix):
    """Menghitung determinan dari matriks persegi menggunakan ekspansi kofaktor."""
    # Basis kasus untuk matriks 2x2
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for c in range(len(matrix)):
        # Minor matrix setelah menghapus baris pertama dan kolom ke-c
        minor = np.delete(np.delete(matrix, 0, axis=0), c, axis=1)
        det += ((-1) ** c) * matrix[0][c] * determinant(minor)
    return det

def cofactor(matrix, i, j):
    """Menghitung kofaktor dari elemen pada baris ke-i dan kolom ke-j."""
    minor = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
    return ((-1) ** (i + j)) * determinant(minor)

def adjoint(matrix):
    """Menghitung adjoin dari matriks."""
    n = len(matrix)
    adj = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            adj[j][i] = cofactor(matrix, i, j)  # Transpose di sini
    return adj

def inverse(matrix):
    """
    Menghitung invers dari matriks persegi menggunakan metode adjoin.
    
    Parameter:
    matrix : np.array : Matriks persegi
    
    Return:
    np.array : Matriks inverse
    """
    det = determinant(matrix)
    if det == 0:
        raise ValueError("Matriks singular tidak memiliki inverse")
    
    adj = adjoint(matrix)
    return adj / det

# Koefisien matriks A dari soal
A = np.array([[4, -1, -1],
              [-1, 3, -1],
              [-1, -1, 5]], dtype=float)

# Menghitung inverse dari matriks A
try:
    inverse_A = inverse(A)
    print("Inverse matriks A:\n", inverse_A)
except ValueError as e:
    print("Error:", e)
