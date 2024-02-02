class Kelvin:
    def __init__(self, suhu):
        self.suhu = suhu
        
    def get_Kelvin(self):
        val = self.suhu
        return val
    
    def get_celcius(self):
        val = float(suhu) - 273
        return val
    
    def get_fahrenheit(self):
        val = 9/5 * (float(suhu) - 273) + 32
        return val
    
    def get_reamur(self):
        val = 4/5 * (float(suhu) - 273)
        return val

suhu = input("masukkan suhu dalam Kelvin: ")
awal = Kelvin(float(suhu))
val = awal.get_Kelvin()

C = awal.get_celcius()
F = awal.get_fahrenheit()
R = awal.get_reamur()

print(str(val) + " Kelvin, sama dengan : ")
print(str(C) + " celcius")
print(str(F) + " fahrenheit")
print(str(R) + " reamur")
