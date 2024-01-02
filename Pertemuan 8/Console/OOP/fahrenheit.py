class Fahrenheit:
    def __init__(self, suhu):
        self.suhu = suhu
        
    def get_Fahrenheit(self):
        val = self.suhu
        return val
    
    def get_celcius(self):
        val = (32 - float(suhu)) * 5/9
        return val
    
    def get_reamur(self):
        val = (32 - float(suhu)) * 4/9
        return val
    
    def get_kelvin(self):
        val = (32 - float(suhu)) * 5/9 + 273
        return val

suhu = input("masukkan suhu dalam Fahrenheit: ")
awal = Fahrenheit(float(suhu))
val = awal.get_Fahrenheit()

C = awal.get_celcius()
R = awal.get_reamur()
K = awal.get_kelvin()

print(str(val) + " Fahrenheit, sama dengan : ")
print(str(C) + " celcius")
print(str(R) + " reamur")
print(str(K) + " kelvin")
