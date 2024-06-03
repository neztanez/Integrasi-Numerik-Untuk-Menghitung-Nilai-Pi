import numpy as np
import time

# Fungsi f(x) yang akan diintegrasikan
def f(x):
    return 4 / (1 + x**2)

# Metode integrasi Reimann
def reimann_integration(a, b, N):
    h = (b - a) / N  # Lebar setiap subinterval
    integral = sum(f(a + i * h) for i in range(N))  # Jumlah nilai f di setiap titik
    integral *= h  # Mengalikan dengan lebar subinterval
    return integral

# Metode integrasi trapezoid
def trapezoid_integration(a, b, N):
    h = (b - a) / N  # Lebar setiap subinterval
    integral = 0.5 * (f(a) + f(b))  # Nilai awal dengan setengah dari f(a) dan f(b)
    for i in range(1, N):
        integral += f(a + i * h)  # Menambahkan nilai f di titik-titik lainnya
    integral *= h  # Mengalikan dengan lebar subinterval
    return integral

# Metode integrasi Simpson 1/3
def simpson_integration(a, b, N):
    if N % 2 == 1:  # Memastikan N adalah genap
        N += 1
    h = (b - a) / N  # Lebar setiap subinterval
    integral = f(a) + f(b)  # Nilai awal dengan f(a) dan f(b)
    for i in range(1, N, 2):
        integral += 4 * f(a + i * h)  # Menambahkan nilai f di titik ganjil
    for i in range(2, N-1, 2):
        integral += 2 * f(a + i * h)  # Menambahkan nilai f di titik genap
    integral *= h / 3  # Mengalikan dengan lebar subinterval dan membagi dengan 3
    return integral

# Menghitung galat RMS antara nilai pi yang diaproksimasi dan nilai referensi pi
def calculate_rms_error(approx_pi, true_pi):
    return np.sqrt(np.mean((approx_pi - true_pi) ** 2))

def main():
    true_pi = 3.14159265358979323846  # Nilai referensi pi
    N_values = [10, 100, 1000, 10000]  # Variasi nilai N

    nim = input("Masukkan NIM Anda: ")  # Meminta input NIM dari pengguna
    last_two_digits = int(nim[-2:])  # Mendapatkan dua digit terakhir dari NIM
    method = last_two_digits % 3  # Menentukan metode berdasarkan dua digit terakhir

    # Menentukan metode integrasi berdasarkan nilai dua digit terakhir NIM
    if method == 0:
        methods = [(reimann_integration, "Reimann Integration"), 
                   (simpson_integration, "Simpson 1/3 Integration")]
    elif method == 1:
        methods = [(trapezoid_integration, "Trapezoid Integration")]
    elif method == 2:
        methods = [(simpson_integration, "Simpson 1/3 Integration")]

    # Melakukan pengujian untuk setiap metode yang dipilih
    for integration_method, method_name in methods:
        print(f'Metode yang digunakan: {method_name}\n')

        results = []

        # Menghitung integral untuk setiap nilai N
        for N in N_values:
            start_time = time.time()  # Mengukur waktu mulai
            approx_pi = integration_method(0, 1, N)  # Menghitung nilai pi yang diaproksimasi
            end_time = time.time()  # Mengukur waktu selesai
            rms_error = calculate_rms_error(approx_pi, true_pi)  # Menghitung galat RMS
            exec_time = end_time - start_time  # Menghitung waktu eksekusi
            results.append((N, approx_pi, rms_error, exec_time))  # Menyimpan hasil

        # Menampilkan hasil untuk setiap nilai N
        for result in results:
            print(f'N = {result[0]}, Approximated Pi = {result[1]}, RMS Error = {result[2]}, Execution Time = {result[3]} seconds')
        print("\n")  # Baris baru untuk pemisah hasil setiap metode

if __name__ == "__main__":
    main()  # Menjalankan fungsi utama
