import numpy as np
import matplotlib.pyplot as plt

def R(T):
    """Menghitung nilai resistansi R pada temperatur T."""
    return 5000 * np.exp(3500 * (1/T - 1/2900))

def forward_difference(T, h=1e-5):
    """Menghitung dR/dT menggunakan metode selisih maju."""
    return (R(T + h) - R(T)) / h

def backward_difference(T, h=1e-5):
    """Menghitung dR/dT menggunakan metode selisih mundur."""
    return (R(T) - R(T - h)) / h

def central_difference(T, h=1e-5):
    """Menghitung dR/dT menggunakan metode selisih tengah."""
    return (R(T + h) - R(T - h)) / (2 * h)

def exact_derivative(T):
    """Menghitung turunan eksak dR/dT."""
    R_T = R(T)
    return R_T * (-3500 / T**2)

# Rentang temperatur
T_values = np.arange(250, 351, 10)

# Menghitung turunan eksak dan metode numerik
exact_results = [exact_derivative(T) for T in T_values]
forward_results = [forward_difference(T) for T in T_values]
backward_results = [backward_difference(T) for T in T_values]
central_results = [central_difference(T) for T in T_values]

# Menghitung error relatif
def calculate_relative_error(numerical, exact):
    """Menghitung error relatif antara hasil numerik dan eksak."""
    numerical_array = np.array(numerical)
    exact_array = np.array(exact)
    
    # Menghindari pembagian dengan nol
    return np.abs((numerical_array - exact_array) / np.where(exact_array == 0, 1e-10, exact_array)) * 100

forward_errors = calculate_relative_error(forward_results, exact_results)
backward_errors = calculate_relative_error(backward_results, exact_results)
central_errors = calculate_relative_error(central_results, exact_results)

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(T_values, forward_errors, marker='o', label='Error Selisih Maju (%)')
plt.plot(T_values, backward_errors, marker='s', label='Error Selisih Mundur (%)')
plt.plot(T_values, central_errors, marker='^', label='Error Selisih Tengah (%)')

plt.title('Error Relatif untuk Metode Numerik dR/dT')
plt.xlabel('Temperatur (K)')
plt.ylabel('Error Relatif (%)')
plt.legend()
plt.grid()
plt.xticks(T_values)
plt.ylim(0, max(forward_errors.max(), backward_errors.max(), central_errors.max()) + 5)
plt.show()
