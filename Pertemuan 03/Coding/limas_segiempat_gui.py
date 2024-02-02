import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas():
    ps = float(txtpanjang_sisi.get())
    tg = float(txttinggi.get())

    luas_alas = ps**2
    luas_selubung = 4 * (0.5 * ps * tg)  # Ada 4 sisi segitiga tegak pada limas segiempat

    # Mencari luas permukaan
    luas_permukaan = luas_alas + luas_selubung

    L = round(luas_permukaan,2)

    txtLuas.delete(0, END)
    txtLuas.insert(END,L)

def hitung_volume():
    ps = float(txtpanjang_sisi.get())
    tg = float(txttinggi.get())

    V = round((1/3) * ps**2 * tg,2)

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
app.title("Kalkulator Luas dan volume Limas Segiempat")

# Windows
frame = Frame(app) 
frame.pack(padx=20, pady=20)

nametag = tk.Frame(frame, bg="lightblue", height=30)
nametag.grid(row=6, column=0, columnspan=2, sticky="ew", pady=10)

nama = Label(nametag, text="Sodiq Abdullah", bg='lightblue') 
nama.grid(row=6, column=0, sticky=W, padx=5, pady=5)

kelas = Label(nametag, text="TIF22E", bg='lightblue' ) 
kelas.grid(row=6, column=1, sticky='e', padx=5, pady=5)

# Label panjang_sisi
panjang_sisi = Label(frame, text="Panjang Sisi:") 
panjang_sisi.grid(row=0, column=0, sticky=W, padx=5, pady=5)

#Label tinggi
tinggi = Label(frame, text="Tinggi:")
tinggi.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Textbox panjang_sisi
txtpanjang_sisi = Entry(frame)
txtpanjang_sisi.grid(row=0, column=1)

#Textbox tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=1, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas: ")
luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output label volume
volume = Label (frame, text="Volume: ")
volume.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Textbox volume
txtvolume = Entry (frame)
txtvolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)

app.mainloop()