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

def exact_derivative(T):
    """
    Menghitung turunan eksak dR/dT.
    
    Parameter:
    T : float : Temperatur dalam Kelvin
    
    Return:
    float : Turunan dR/dT
    """
    # Hitung nilai R pada temperatur T
    R_T = R(T)
    
    # Hitung turunan
    dR_dT = R_T * (-3500 / T**2)
    
    return dR_dT

# Menghitung nilai eksak dR/dT untuk temperatur dari 250K hingga 350K
T_values = np.arange(250, 351, 10)  # Temperatur dari 250K hingga 350K
exact_results = [exact_derivative(T) for T in T_values]

# Menampilkan hasil
print("Temperatur (K) | dR/dT (Ohm/K)")
print("-----------------------------")
for i in range(len(T_values)):
    print(f"{T_values[i]:<16} | {exact_results[i]:.4f}")
