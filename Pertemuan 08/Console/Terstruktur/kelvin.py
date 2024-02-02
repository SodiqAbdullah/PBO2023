print("konversi shuh Kelvin")

def get_celcius(suhu):
    C = float(suhu) - 273
    return C

def get_fahrenheit(suhu):
    F = 9/5 * (float(suhu) - 273) + 32
    return F

def get_reamur(suhu):
    K = 4/5 * (float(suhu) - 273)
    return K
    
suhu = input("masukkan suhu dalam Kelvin: ")

print(suhu + " Kelvin sama dengaan")
print(str(get_celcius(suhu)) + " Celcius")
print(str(get_fahrenheit(suhu)) + " fahrenheit")
print(str(get_reamur(suhu)) + " reamur")
