import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas():
    alas = float(txtalas.get())
    ts = float(txttinggi_segitiga.get())
    tl = float(txttinggi_limas.get())

    luas_alas = 0.5 * alas * ts
    luas_selubung = 3 * (0.5 * alas * tl)
    luas_permukaan = luas_alas + luas_selubung

    L = round(luas_permukaan,2)

    txtLuas.delete(0, END)
    txtLuas.insert(END,L)

def hitung_volume():
    alas = float(txtalas.get())
    ts = float(txttinggi_segitiga.get())
    tl = float(txttinggi_limas.get())

    V = round((1/3) * 0.5 * alas * ts * tl,2)

    txtvolume.delete(0,END)
    txtvolume.insert(END,V)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object app = tk.Tk()
app = tk.Tk()
# app.configure(bg="black")
app.geometry("400x300")

# Tambahkan judul
app.title("Kalkulator Luas dan volume Limas Segitiga")

# Windows
frame = Frame(app) 
frame.pack(padx=20, pady=20)

nametag = tk.Frame(frame, bg="lightblue", height=30)
nametag.grid(row=6, column=0, columnspan=2, sticky="ew", pady=10)

nama = Label(nametag, text="Sodiq Abdullah", bg='lightblue') 
nama.grid(row=6, column=0, sticky=W, padx=5, pady=5)

kelas = Label(nametag, text="TIF22E", bg='lightblue' ) 
kelas.grid(row=6, column=1, sticky='e', padx=5, pady=5)

# Label alas
alas = Label(frame, text="Alas:") 
alas.grid(row=0, column=0, sticky=W, padx=5, pady=5)

#Label tinggi_segitiga
tinggi_segitiga = Label(frame, text="Tinggi Segitiga:")
tinggi_segitiga.grid(row=1, column=0, sticky=W, padx=5, pady=5)

#Label tinggi_limas
tinggi_limas = Label(frame, text="Tinggi Limas:")
tinggi_limas.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Textbox alas
txtalas = Entry(frame)
txtalas.grid(row=0, column=1)

#Textbox tinggi_segitiga
txttinggi_segitiga = Entry(frame)
txttinggi_segitiga.grid(row=1, column=1)

# Textbox tinggi_limas
txttinggi_limas = Entry(frame)
txttinggi_limas.grid(row=2, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas: ")
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output label volume
volume = Label (frame, text="Volume: ")
volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Textbox volume
txtvolume = Entry (frame)
txtvolume.grid(row=5, column=1, sticky=W, padx=5, pady=5)

app.mainloop()