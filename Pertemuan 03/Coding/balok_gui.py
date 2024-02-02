import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas():
    panjang = float(txtpanjang.get())
    lebar = float(txtlebar.get())
    tinggi = float(txttinggi.get())


    L = 2 * (panjang*lebar + panjang*tinggi + lebar*tinggi)

    txtLuas.delete(0, END)
    txtLuas.insert(END,L)

def hitung_volume():
    panjang = float(txtpanjang.get())
    lebar = float(txtlebar.get())
    tinggi = float(txttinggi.get())

    V = panjang * lebar * tinggi

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
app.title("Kalkulator Luas dan volume balok")

# Windows
frame = Frame(app) 
frame.pack(padx=20, pady=20)

nametag = tk.Frame(frame, bg="lightblue", height=30)
nametag.grid(row=6, column=0, columnspan=2, sticky="ew", pady=10)

nama = Label(nametag, text="Sodiq Abdullah", bg='lightblue') 
nama.grid(row=6, column=0, sticky=W, padx=5, pady=5)

kelas = Label(nametag, text="TIF22E", bg='lightblue' ) 
kelas.grid(row=6, column=1, sticky='e', padx=5, pady=5)

# Label Panjang
panjang = Label(frame, text="Panjang:") 
panjang.grid(row=0, column=0, sticky=W, padx=5, pady=5)

#Label Lebar
lebar = Label(frame, text="Lebar:")
lebar.grid(row=1, column=0, sticky=W, padx=5, pady=5)

#Label Tinggi
tinggi = Label(frame, text="Tinggi:")
tinggi.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Textbox Panjang
txtpanjang = Entry(frame)
txtpanjang.grid(row=0, column=1)

#Textbox Lebar
txtlebar = Entry(frame)
txtlebar.grid(row=1, column=1)

# Textbox Tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=2, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas: ")
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output label volume
volume = Label (frame, text="volume: ")
volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Textbox volume
txtvolume = Entry (frame)
txtvolume.grid(row=5, column=1, sticky=W, padx=5, pady=5)

app.mainloop()