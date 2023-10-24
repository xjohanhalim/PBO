# Program menghitung volume dan luas permukaan limas segiempat

# Input panjang, lebar, tinggi alas, dan tinggi limas dari pengguna
panjang_alas = float(input("Masukkan panjang alas limas: "))
lebar_alas = float(input("Masukkan lebar alas limas: "))
tinggi_alas = float(input("Masukkan tinggi alas limas: "))
tinggi_limas = float(input("Masukkan tinggi limas: "))

# Menghitung volume limas
volume = (1/3) * (panjang_alas * lebar_alas * tinggi_limas)

# Menghitung luas permukaan limas
luas_permukaan = (panjang_alas * lebar_alas) + (panjang_alas * (tinggi_limas + tinggi_alas)) + (lebar_alas * (tinggi_limas + tinggi_alas))

# Menampilkan hasil perhitungan
print("Volume limas adalah:", volume)
print("Luas permukaan limas adalah:", luas_permukaan)