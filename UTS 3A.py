import numpy as np

def R(T):
    """
    Menghitung nilai resistansi R pada temperatur T.
    
    Parameter:
    T : float : Temperatur dalam Kelvin
    
    Return:
    float : Resistansi R dalam Ohm
    """
    return 5000 * np.exp(3500 * (1/T - 1/2900))

def forward_difference(func, T, h):
    """Menghitung turunan menggunakan metode selisih maju."""
    return (func(T + h) - func(T)) / h

def backward_difference(func, T, h):
    """Menghitung turunan menggunakan metode selisih mundur."""
    return (func(T) - func(T - h)) / h

def central_difference(func, T, h):
    """Menghitung turunan menggunakan metode selisih tengah."""
    return (func(T + h) - func(T - h)) / (2 * h)

# Parameter
T_values = np.arange(250, 351, 10)  # Temperatur dari 250K hingga 350K
h = 1e-5  # Langkah kecil untuk perhitungan selisih

# Menghitung dR/dT untuk setiap metode
results = { 'T': [], 'Forward': [], 'Backward': [], 'Central': [] }

for T in T_values:
    results['T'].append(T)
    results['Forward'].append(forward_difference(R, T, h))
    results['Backward'].append(backward_difference(R, T, h))
    results['Central'].append(central_difference(R, T, h))

# Menampilkan hasil
for i in range(len(T_values)):
    print(f"T = {results['T'][i]} K: Forward = {results['Forward'][i]:.2f}, "
          f"Backward = {results['Backward'][i]:.2f}, Central = {results['Central'][i]:.2f}")
