class Reamur:
    def __init__(self, suhu):
        self.suhu = suhu
        
    def get_Reamur(self):
        val = self.suhu
        return val
    
    def get_celcius(self):
        val = float(suhu) * 5/4
        return val
    
    def get_fahrenheit(self):
        val = (float(suhu) * 9/4) + 32
        return val
    
    def get_kelvin(self):
        val = (float(suhu) * 5/4) +273
        return val

suhu = input("masukkan suhu dalam Reamur: ")
awal = Reamur(float(suhu))
val = awal.get_Reamur()

C = awal.get_celcius()
F = awal.get_fahrenheit()
K = awal.get_kelvin()

print(str(val) + " Reamur, sama dengan : ")
print(str(C) + " celcius")
print(str(F) + " fahrenheit")
print(str(K) + " kelvin")
