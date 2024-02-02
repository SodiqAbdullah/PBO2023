alas = 8
tinggi = 6
tinggi_prisma = 10

# rumus menghitung luas
luas_alas = 0.5 * alas * tinggi
luas_sisi_tegak = 3 * alas * tinggi_prisma
luas_permukaan = 2 * luas_alas + luas_sisi_tegak

# rumus menghitung volume 
volume = 0.5 * alas * tinggi * tinggi_prisma

print('hasil dari mencari luas prisma segitiga dengan\nalas : ',alas,'\ntinggi_prisma : ',tinggi_prisma,'\ntinggi : ',tinggi,'\nadalah = ', luas_permukaan )

print('\nhasil dari mencari volume prisma segitiga dengan\nalas : ',alas,'\ntinggi_prisma : ',tinggi_prisma,'\ntinggi : ',tinggi,'\nadalah = ', volume )
