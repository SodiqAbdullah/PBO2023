print("konversi suhu Kelvin")

# Entry
suhu = input("Masukkan suhu dalam Kelvin ")

# rumus
C = float(suhu) - 273
F = 9/5 * (float(suhu) - 273) + 32
R = 4/5 * (float(suhu) - 273)

# output
print(suhu + " Kelvin sama dengaan")
print(str(C) + " Celcius")
print(str(F) + " Farenheit")
print(str(R) + " Reamur")
