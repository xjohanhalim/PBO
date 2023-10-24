# Program menghitung volume dan luas permukaan silinder

import math

# Input jari-jari dan tinggi silinder dari pengguna
jari_jari = float(input("Masukkan jari-jari silinder: "))
tinggi = float(input("Masukkan tinggi silinder: "))

# Menghitung volume silinder
volume = math.pi * (jari_jari ** 2) * tinggi

# Menghitung luas permukaan silinder
luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)

# Menampilkan hasil perhitungan
print("Volume silinder adalah:", volume)
print("Luas permukaan silinder adalah:", luas_permukaan)
