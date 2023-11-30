import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W

class prisma_segitiga_gui:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300")
        self.root.title("menghitung luas dan volume prisma segitiga")
        self.komponen()
        
    def hitung_luas(self):
        alas = float(self.txtalas.get())
        t = float(self.txttinggi.get())
        tp = float(self.txttinggi_prisma.get())

        luas_alas = 0.5 * alas * t
        luas_sisi_tegak = 3 * alas * tp
        luas_permukaan = 2 * luas_alas + luas_sisi_tegak

        L = round(luas_permukaan,2)

        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END,L)

    def hitung_volume(self):
        alas = float(self.txtalas.get())
        t = float(self.txttinggi.get())
        tp = float(self.txttinggi_prisma.get())

        V = round(0.5 * alas * t * tp,2)

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

        # Label alas
        alas = Label(frame, text="Alas:") 
        alas.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        #Label tinggi
        tinggi = Label(frame, text="Tinggi:")
        tinggi.grid(row=1, column=0, sticky=W, padx=5, pady=5)

        #Label tinggi_prisma
        tinggi_prisma = Label(frame, text="Tinggi Prisma:")
        tinggi_prisma.grid(row=2, column=0, sticky=W, padx=5, pady=5)

        # Textbox alas
        self.txtalas = Entry(frame)
        self.txtalas.grid(row=0, column=1)

        #Textbox tinggi
        self.txttinggi = Entry(frame)
        self.txttinggi.grid(row=1, column=1)

        # Textbox tinggi_prisma
        self.txttinggi_prisma = Entry(frame)
        self.txttinggi_prisma.grid(row=2, column=1)

        # Button
        hitung_button = Button(frame, text="Hitung", command=self.hitung)
        hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

        # Output Label Luas
        luas = Label(frame, text="Luas: ")
        luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

        # Output label volume
        volume = Label (frame, text="Volume: ")
        volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

        # Output Textbox Luas
        self.txtLuas = Entry(frame)
        self.txtLuas.grid(row=4, column=1, sticky=W, padx=5, pady=5)

        # Output Textbox volume
        self.txtvolume = Entry (frame)
        self.txtvolume.grid(row=5, column=1, sticky=W, padx=5, pady=5)
        
if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = prisma_segitiga_gui(root)
    root.mainloop()