import numpy as np


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

def calculate_relative_error(numerical, exact):
    """Menghitung error relatif antara hasil numerik dan eksak."""
    numerical_array = np.array(numerical)
    exact_array = np.array(exact)
    
    # Menghindari pembagian dengan nol
    return np.abs((numerical_array - exact_array) / np.where(exact_array == 0, 1e-10, exact_array)) * 100

def richardson_extrapolation(f_h, f_h_half):
    """Menghitung nilai extrapolasi Richardson."""
    return (2 * f_h_half - f_h)

# Rentang temperatur
T_values = np.arange(250, 351, 10)

# Menghitung turunan eksak dan metode numerik
exact_results = [exact_derivative(T) for T in T_values]
forward_results = [forward_difference(T) for T in T_values]
backward_results = [backward_difference(T) for T in T_values]
central_results = [central_difference(T) for T in T_values]

# Metode Extrapolasi Richardson
richardson_results = []
for T in T_values:
    f_h = central_difference(T, h=1e-5)
    f_h_half = central_difference(T, h=5e-6)
    richardson_results.append(richardson_extrapolation(f_h, f_h_half))

# Menghitung error relatif untuk Richardson
richardson_errors = calculate_relative_error(richardson_results, exact_results)


# Menampilkan hasil
for T, exact, richardson in zip(T_values, exact_results, richardson_results):
    print(f"T: {T} K, Exact: {exact:.2f}, Richardson: {richardson:.2f}, Error: {richardson_errors[T_values.tolist().index(T)]:.2f}%")
