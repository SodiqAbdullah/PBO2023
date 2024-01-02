print("konversi shuh Fahrenheit")

def get_celcius(suhu):
    C = (32 - float(suhu)) * 5/9
    return C

def get_reamur(suhu):
    R = (32 - float(suhu)) * 4/9
    return R

def get_kelvin(suhu):
    K = (32 - float(suhu)) * 5/9 + 273
    return K
    
suhu = input("masukkan suhu dalam Fahrenheit: ")

print(suhu + " fahrenheit sama dengaan")
print(str(get_celcius(suhu)) + " Celcius")
print(str(get_reamur(suhu)) + " Reamur")
print(str(get_kelvin(suhu)) + " Kelvin")
