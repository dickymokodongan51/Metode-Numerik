import numpy as np

# Definisikan fungsi
def f(x):
    return x + np.exp(x)

# Metode Bisection
def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    fa, fb = f(a), f(b)
    if fa * fb >= 0:
        raise ValueError("Fungsi tidak memiliki perubahan tanda dalam interval ini.")
    
    for _ in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        
        if np.abs(fc) < tol or (b - a) / 2 < tol:
            return c  # Akar ditemukan
        
        if fa * fc < 0:
            b = c
        else:
            a = c
            fa = fc
    return (a + b) / 2  # Kembalikan perkiraan akar

# Metode Regula Falsi
def regula_falsi_method(f, a, b, tol=1e-6, max_iter=100):
    fa, fb = f(a), f(b)
    if fa * fb >= 0:
        raise ValueError("Fungsi tidak memiliki perubahan tanda dalam interval ini.")
    
    for _ in range(max_iter):
        c = a - (fa * (b - a)) / (fb - fa)  # Rumus Regula Falsi
        fc = f(c)
        
        if np.abs(fc) < tol:
            return c  # Akar ditemukan
        
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return c  # Kembalikan perkiraan akar

# Tentukan interval [a, b]
a, b = -1, 0

# Cari akar dengan metode Bisection
root_bisection = bisection_method(f, a, b)
print(f"Akar menggunakan metode Bisection: {root_bisection}")

# Cari akar dengan metode Regula Falsi
root_regula_falsi = regula_falsi_method(f, a, b)
print(f"Akar menggunakan metode Regula Falsi: {root_regula_falsi}")
