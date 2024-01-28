class Kelvin:
    def __init__(self, suhu):
        self.suhu = suhu
    
    def get_kelvin(self):
        val = self.suhu
        return val
    
    def get_celsius(self):
        val = (self.suhu - 32)
        return val
    
    def get_reamur(self):
        val = (self.suhu - 273) * 4/5
        return val

    def get_fahrenheit(self):
        val = (self.suhu + 32) * 9/5 - 273
        return val

suhu_kelvin = input("Masukan suhu dalam Kelvin: ")
F = Kelvin(float(suhu_kelvin))
val = F.get_kelvin()

C = F.get_celsius()
R = F.get_reamur()
F = F.get_fahrenheit()

print(str(val) + " Kelvin sama dengan:")
print(str(C) + " Celsius")
print(str(R) + " Reamur")
print(str(F) + " Fahrenheit")