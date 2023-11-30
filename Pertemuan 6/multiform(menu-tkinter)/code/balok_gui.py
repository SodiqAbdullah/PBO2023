import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W

class balok_gui:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300")
        self.root.title("menghitung luas dan volume balok")
        self.atur_komponen()

    def hitung_luas(self):
        panjang = float(self.txtpanjang.get())
        lebar = float(self.txtlebar.get())
        tinggi = float(self.txttinggi.get())


        L = 2 * (panjang*lebar + panjang*tinggi + lebar*tinggi)

        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END,L)

    def hitung_volume(self):
        panjang = float(self.txtpanjang.get())
        lebar = float(self.txtlebar.get())
        tinggi = float(self.txttinggi.get())

        V = panjang * lebar * tinggi

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
        self.txtpanjang = Entry(frame)
        self.txtpanjang.grid(row=0, column=1)

        #Textbox Lebar
        self.txtlebar = Entry(frame)
        self.txtlebar.grid(row=1, column=1)

        # Textbox Tinggi
        self.txttinggi = Entry(frame)
        self.txttinggi.grid(row=2, column=1)

        # Button
        hitung_button = Button(frame, text="Hitung", command=self.hitung)
        hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

        # Output Label Luas
        luas = Label(frame, text="Luas: ")
        luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

        # Output label volume
        volume = Label (frame, text="volume: ")
        volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

        # Output Textbox Luas
        self.txtLuas = Entry(frame)
        self.txtLuas.grid(row=4, column=1, sticky=W, padx=5, pady=5)

        # Output Textbox volume
        self.txtvolume = Entry (frame)
        self.txtvolume.grid(row=5, column=1, sticky=W, padx=5, pady=5)

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = balok_gui(root)
    root.mainloop()
