import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W
from fungsi_rumus import LuasBola, VolumeBola

def hitung_luas():
    jrjr = float(txtjari_jari.get())
    
    L = LuasBola(jrjr)

    txtLuas.delete(0, END)
    txtLuas.insert(END,L)

def hitung_volume():
    jrjr = float(txtjari_jari.get())

    V = VolumeBola(jrjr)

    txtvolume.delete(0,END)
    txtvolume.insert(END,V)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object app = tk.Tk()
app = tk.Tk()
app.geometry("400x300")

# Tambahkan judul
app.title("Kalkulator Luas dan volume Bola")

# Windows
frame = Frame(app) 
frame.pack(padx=20, pady=20)

nametag = tk.Frame(frame, bg="lightblue", height=30)
nametag.grid(row=6, column=0, columnspan=2, sticky="ew", pady=10)

nama = Label(nametag, text="Sodiq Abdullah", bg='lightblue') 
nama.grid(row=6, column=0, sticky=W, padx=5, pady=5)

kelas = Label(nametag, text="TIF22E", bg='lightblue' ) 
kelas.grid(row=6, column=1, sticky='e', padx=5, pady=5)

# Label jari_jari
jari_jari = Label(frame, text="Jari-jari:") 
jari_jari.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Textbox jari_jari
txtjari_jari = Entry(frame)
txtjari_jari.grid(row=0, column=1)

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