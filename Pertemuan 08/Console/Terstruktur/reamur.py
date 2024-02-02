print("konversi shuh Reamur")

def get_celcius(suhu):
    C = float(suhu) * 5/4
    return C

def get_fahrenheit(suhu):
    F = (float(suhu) * 9/4) + 32
    return F

def get_kelvin(suhu):
    K = (float(suhu) * 5/4) +273
    return K
    
suhu = input("masukkan suhu dalam Reamur: ")

print(suhu + " Reamur sama dengaan")
print(str(get_celcius(suhu)) + " Celcius")
print(str(get_fahrenheit(suhu)) + " fahrenheit")
print(str(get_kelvin(suhu)) + " Kelvin")
