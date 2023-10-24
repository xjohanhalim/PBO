# Program menghitung volume dan luas permukaan prisma segitiga

# Input panjang sisi segitiga dasar, tinggi segitiga, dan tinggi prisma dari pengguna
sisi_segitiga = float(input("Masukkan panjang sisi segitiga dasar: "))
tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))
tinggi_prisma = float(input("Masukkan tinggi prisma: "))

# Menghitung luas segitiga dasar
luas_segitiga = 0.5 * sisi_segitiga * tinggi_segitiga

# Menghitung volume prisma segitiga
volume = luas_segitiga * tinggi_prisma

# Menghitung luas permukaan prisma segitiga
luas_permukaan = (2 * luas_segitiga) + (sisi_segitiga * tinggi_prisma * 3)

# Menampilkan hasil perhitungan
print("Volume prisma segitiga adalah:", volume)
print("Luas permukaan prisma segitiga adalah:", luas_permukaan)