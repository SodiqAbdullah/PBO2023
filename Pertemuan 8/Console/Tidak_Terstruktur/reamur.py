print("konversi suhu Reamur")

# Entry
suhu = input("Masukkan suhu dalam Reamur ")

# rumus
C = float(suhu) * 5/4
F = (float(suhu) * 9/4) + 32
K = (float(suhu) * 5/4) + 273

# output
print(suhu + " Reamur sama dengaan")
print(str(C) + " Celcius")
print(str(F) + " fahrenheit")
print(str(K) + " Kelvin")
