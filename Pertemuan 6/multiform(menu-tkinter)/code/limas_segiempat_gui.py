import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W

class limas_segiempat_gui:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300")
        self.root.title("menghitung luas dan volume limas segiempat")
        self.komponen()  
              
    def hitung_luas(self):
        ps = float(self.txtpanjang_sisi.get())
        tg = float(self.txttinggi.get())

        luas_alas = ps**2
        luas_selubung = 4 * (0.5 * ps * tg)  # Ada 4 sisi segitiga tegak pada limas segiempat

        # Mencari luas permukaan
        luas_permukaan = luas_alas + luas_selubung

        L = round(luas_permukaan,2)

        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END,L)

    def hitung_volume(self):
        ps = float(self.txtpanjang_sisi.get())
        tg = float(self.txttinggi.get())

        V = round((1/3) * ps**2 * tg,2)

        self.txtvolume.delete(0,END)
        self.txtvolume.insert(END,V)

    def hitung(self):
        self.hitung_luas()
        self.hitung_volume()

    def komponen(self):
        frame = Frame(self.root) 
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
        self.txtpanjang_sisi = Entry(frame)
        self.txtpanjang_sisi.grid(row=0, column=1)

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
    aplikasi = limas_segiempat_gui(root)
    root.mainloop()