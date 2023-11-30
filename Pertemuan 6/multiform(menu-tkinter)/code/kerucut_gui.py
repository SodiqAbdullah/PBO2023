import tkinter as tk 
import math
from tkinter import Frame, Label, Entry, Button, END, W

class kerucut_gui:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300")
        self.root.title("menghitung luas dan volume kerucut")
        self.atur_komponen()

    def hitung_luas(self):
        jr2 = float(self.txtjari_jari.get())
        tg = float(self.txttinggi.get())

        garis_miring = math.sqrt(jr2**2 + tg**2)
        luas_permukaan = math.pi * jr2 * (jr2 + garis_miring)


        L = round(luas_permukaan,2)

        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END,L)

    def hitung_volume(self):
        jr2 = float(self.txtjari_jari.get())
        tg = float(self.txttinggi.get())

        V = round((1/3) * math.pi * jr2**2 * tg,2)

        self.txtvolume.delete(0,END)
        self.txtvolume.insert(END,V)

    def hitung(self):
        self.hitung_luas()
        self.hitung_volume()

    def atur_komponen(self):
            
        frame = Frame(self.root) 
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

        #Label tinggi
        tinggi = Label(frame, text="Tinggi:")
        tinggi.grid(row=1, column=0, sticky=W, padx=5, pady=5)

        # Textbox jari_jari
        self.txtjari_jari = Entry(frame)
        self.txtjari_jari.grid(row=0, column=1)

        #Textbox tinggi
        self.txttinggi = Entry(frame)
        self.txttinggi.grid(row=1, column=1)

        # Button
        hitung_button = Button(frame, text="Hitung", command=self.hitung)
        hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

        # Output Label Luas
        luas = Label(frame, text="Luas: ")
        luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

        # Output label volume
        volume = Label (frame, text="Volume: ")
        volume.grid(row=4, column=0, sticky=W, padx=5, pady=5)

        # Output Textbox Luas
        self.txtLuas = Entry(frame)
        self.txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

        # Output Textbox volume
        self.txtvolume = Entry (frame)
        self.txtvolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = kerucut_gui(root)
    root.mainloop()