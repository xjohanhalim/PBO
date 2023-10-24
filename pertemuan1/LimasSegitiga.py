# Program menghitung volume dan luas permukaan limas segitiga

# Input panjang sisi segitiga dasar, tinggi segitiga, dan tinggi limas dari pengguna
sisi_segitiga = float(input("Masukkan panjang sisi segitiga dasar: "))
tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))
tinggi_limas = float(input("Masukkan tinggi limas: "))

# Menghitung luas segitiga dasar
luas_segitiga = 0.5 * sisi_segitiga * tinggi_segitiga

# Menghitung volume limas segitiga
volume = (1/3) * luas_segitiga * tinggi_limas

# Menghitung luas permukaan limas segitiga
luas_permukaan = luas_segitiga + (sisi_segitiga * tinggi_limas * 3)

# Menampilkan hasil perhitungan
print("Volume limas segitiga adalah:", volume)
print("Luas permukaan limas segitiga adalah:", luas_permukaan)
