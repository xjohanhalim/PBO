print("Konversi Suhu Celcius")

# Entry
suhu = input("Masukan suhu dalam Celcius:")

# rumus
F = (9/5 * float(suhu)) + 32
R = (4/5 * float(suhu))
K = float(suhu) + 273

# output
print(suhu + "celcius sama dengan")
print(str(F) + " Fahrenheit")
print(str(R) + " Reamur")
print(str(K) + "Kelvin")