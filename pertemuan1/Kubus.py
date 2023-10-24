# Program menghitung volume dan luas permukaan kubus

# Input sisi kubus dari pengguna
sisi = float(input("Masukkan panjang sisi kubus: "))

# Menghitung volume kubus
volume = sisi ** 3

# Menghitung luas permukaan kubus
luas_permukaan = 6 * (sisi ** 2)

# Menampilkan hasil perhitungan
print("Volume kubus adalah:", volume)
print("Luas permukaan kubus adalah:", luas_permukaan)
