print("Konversi Suhu Kelvin")

# Entry
suhu_kelvin = input("Masukan suhu dalam Kelvin: ")

# rumus
C = (float(suhu_kelvin) - 32) 
R = (float(suhu_kelvin) - 273) * 4/5
F = (float(suhu_kelvin) - 273) * 9/5 + 32

# output
print(suhu_kelvin + " Kelvin sama dengan: ")
print(str(C) + " Celsius")
print(str(R) + " Reamur")
print(str(F) + " Fahrenheit")
