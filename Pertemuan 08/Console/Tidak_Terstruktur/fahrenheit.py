print("konversi suhu fahrenheit")

# Entry
suhu = input("Masukkan suhu dalam Fahrenheit ")

# rumus
C = (32 - float(suhu)) * 5/9
R = (32 - float(suhu)) * 4/9
K = (32 - float(suhu)) * 5/9 + 273

# output
print(suhu + " fahrenheit sama dengaan")
print(str(C) + " Celcius")
print(str(R) + " Reamur")
print(str(K) + " Kelvin")
