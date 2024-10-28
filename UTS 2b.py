import numpy as np

def determinant(matrix):
    """
    Menghitung determinan dari matriks persegi menggunakan ekspansi kofaktor.
    
    Parameter:
    matrix : np.array : Matriks persegi yang ingin dihitung determinannya
    
    Return:
    float : Determinan matriks
    """
    # Basis kasus untuk matriks 1x1
    if matrix.shape == (1, 1):
        return matrix[0, 0]
    
    # Basis kasus untuk matriks 2x2
    if matrix.shape == (2, 2):
        return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]
    
    # Rekursi untuk matriks lebih besar
    det = 0
    for col in range(matrix.shape[1]):
        # Minor adalah matriks yang diperoleh dengan menghapus baris pertama dan kolom saat ini
        minor = np.delete(np.delete(matrix, 0, axis=0), col, axis=1)
        
        # Kofaktor adalah elemen dikalikan (-1)^(baris + kolom)
        cofactor = ((-1) ** col) * matrix[0, col] * determinant(minor)
        
        # Menambahkan kofaktor ke dalam determinan
        det += cofactor
        
    return det

# Contoh penggunaan dengan matriks 3x3
A = np.array([[4, -1, -1],
              [-1, 3, -1],
              [-1, -1, 5]], dtype=float)

# Menghitung determinan matriks A
det_A = determinant(A)
print("Determinan matriks A:", det_A)
