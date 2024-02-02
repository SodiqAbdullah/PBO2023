panjang_sisi = 6
tinggi = 12

luas_alas = panjang_sisi**2
luas_selubung = 4 * (0.5 * panjang_sisi * tinggi)  # Ada 4 sisi segitiga tegak pada limas segiempat

# Mencari luas permukaan
luas_permukaan = luas_alas + luas_selubung

# Mencari untuk menghitung volume limas segiempat
volume = (1/3) * panjang_sisi**2 * tinggi

print('hasil dari mencari luas limas segiempat dengan\npanjang sisi : ',panjang_sisi,'\ntinggi : ',tinggi,'\nadalah = ', luas_permukaan )

print('\nhasil dari mencari volume limas segiempat dengan\npanjang sisi : ',panjang_sisi,'\ntinggi : ',tinggi,'\nadalah = ', volume )