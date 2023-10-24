# Program menghitung volume dan luas permukaan kerucut

import math

# Input jari-jari dan tinggi kerucut dari pengguna
jari_jari = float(input("Masukkan jari-jari kerucut: "))
tinggi = float(input("Masukkan tinggi kerucut: "))

# Menghitung volume kerucut
volume = (1/3) * math.pi * (jari_jari ** 2) * tinggi

# Menghitung luas permukaan kerucut
sisi_miring = math.sqrt((jari_jari ** 2) + (tinggi ** 2))
luas_permukaan = math.pi * jari_jari * (jari_jari + sisi_miring)

# Menampilkan hasil perhitungan
print("Volume kerucut adalah:", volume)
print("Luas permukaan kerucut adalah:", luas_permukaan)
