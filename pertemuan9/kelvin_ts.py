print("Konversi Suhu Kelvin")

def get_celsius(suhu_kelvin):
    return (float(suhu_kelvin) - 273) 

def get_reamur(suhu_kelvin):
    return (float(suhu_kelvin) - 273) * 4/5

def get_fahrenheit(suhu_kelvin):
    return (float(suhu_kelvin) - 32) * 9/5 + 273

# Entry
suhu_kelvin = input("Masukan suhu dalam Kelvin: ")

# rumus 
C = get_celsius(suhu_kelvin)
R = get_reamur(suhu_kelvin)
F = get_fahrenheit(suhu_kelvin)

# output
print(suhu_kelvin + " Fahrenheit sama dengan:")
print(str(C) + " Celsius")
print(str(R) + " Reamur")
print(str(F) + " Fahrenheit")
