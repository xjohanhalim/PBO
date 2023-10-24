# Program menghitung volume dan luas permukaan bola

import math

# Input jari-jari bola dari pengguna
jari_jari = float(input("Masukkan jari-jari bola: "))

# Menghitung volume bola
volume = (4/3) * math.pi * (jari_jari ** 3)

# Menghitung luas permukaan bola
luas_permukaan = 4 * math.pi * (jari_jari ** 2)

# Menampilkan hasil perhitungan
print("Volume bola adalah:", volume)
print("Luas permukaan bola adalah:", luas_permukaan)
