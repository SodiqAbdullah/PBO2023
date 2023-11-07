import math

# rumus menghitung luas dan volume balok
def LuasBalok(panjang, lebar, tinggi):
    return (2 * (panjang*lebar + panjang*tinggi + lebar*tinggi))

def VolumeBalok(panjang, lebar, tinggi):
    return (panjang * lebar * tinggi)


# rumus menghitung luas dan volume bola
def LuasBola(jari2):
    return (round(4 * math.pi * jari2**2,2))

def VolumeBola(jari2):
    return (round((4/3) * math.pi * jari2**3,2))


# rumus menghitung luas dan volume kerucut
def KerucutLuas(jr2, tg):
    garis_miring = math.sqrt(jr2**2 + tg**2)
    luas_permukaan = math.pi * jr2 * (jr2 + garis_miring)

    return (round(luas_permukaan,2))

def KerucutVolume(jr2, tg):
    return(round((1/3) * math.pi * jr2**2 * tg,2))


# rumus menghitung luas dan volume kubus
def KubusLuas(sisi):
    return (6*sisi**2)

def KubusVolume(sisi):
    return(sisi**3)


# rumus menghitung luas dan volume limas segiempat
def LimasEmpatLuas(ps, tg):
    luas_alas = ps**2
    # Ada 4 sisi segitiga tegak pada limas segiempat
    luas_selubung = 4 * (0.5 * ps * tg)  
    # Mencari luas permukaan
    luas_permukaan = luas_alas + luas_selubung
    return(round(luas_permukaan,2))    
    
def LimasEmpatVolume(ps, tg):
    return(round((1/3) * ps**2 * tg,2))


# rumus menghitung luas dan volume limas segitiga
def LimasTigaLuas(ts, tl, alas):
    luas_alas = 0.5 * alas * ts
    luas_selubung = 3 * (0.5 * alas * tl)
    luas_permukaan = luas_alas + luas_selubung
    return(round(luas_permukaan,2))    
    
def LimasTigaVolume(ts, tl, alas):
    return(round((1/3) * 0.5 * alas * ts * tl,2))


# rumus menghitung luas dan volume prisma segitiga
def PrismaTigaLuas(alas, t, tp):
    luas_alas = 0.5 * alas * t
    luas_sisi_tegak = 3 * alas * tp
    luas_permukaan = 2 * luas_alas + luas_sisi_tegak
    return (round(luas_permukaan,2))

def PrismaTigaVolume(alas, t, tp):
    return (round(0.5 * alas * t * tp,2))


# rumus menghitung luas dan volume tabung
def TabungLuas(jr2, tg):
    return (round(2 * math.pi * jr2 * (jr2 + tg),2))
    
def TabungVolume(jr2, tg):
    return (round(math.pi * jr2**2 * tg,2))