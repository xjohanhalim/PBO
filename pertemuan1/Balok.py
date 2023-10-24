# Program menghitung volume dan luas permukaan balok

# Input panjang, lebar, dan tinggi balok dari pengguna
panjang = float(input("Masukkan panjang balok: "))
lebar = float(input("Masukkan lebar balok: "))
tinggi = float(input("Masukkan tinggi balok: "))

# Menghitung volume balok
volume = panjang * lebar * tinggi

# Menghitung luas permukaan balok
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

# Menampilkan hasil perhitungan
print("Volume balok adalah:", volume)
print("Luas permukaan balok adalah:", luas_permukaan)
