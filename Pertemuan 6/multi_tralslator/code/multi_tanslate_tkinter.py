from tkinter import Frame, Label, Entry, Button, Tk, W, END
from tkinter import ttk
from googletrans import Translator

class FrmTranslator:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("800x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill="both", expand="yes")

        # Pasang Label
        Label(mainFrame, text='Masukkan teks:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Hasil Terjemahan:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Dari Bahasa:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Ke Bahasa:').grid(row=1, column=2,
            sticky=W, padx=5, pady=5)

        nametag = Frame(mainFrame, bg="lightblue", height=30)
        nametag.grid(row=6, column=0, columnspan=2, sticky="ew", pady=10)

        nama = Label(nametag, text="Sodiq Abdullah", bg='lightblue')
        nama.grid(row=6, column=0, sticky=W, padx=5, pady=5)

        kelas = Label(nametag, text="TIF22E", bg='lightblue')
        kelas.grid(row=6, column=1, sticky='e', padx=5, pady=5)


        # Pasang Textbox
        self.txtSumber = Entry(mainFrame, width=50) 
        self.txtSumber.grid(row=0, column=1, padx=5, pady=5)

        self.txtHasil = Entry(mainFrame, width=50) 
        self.txtHasil.grid(row=2, column=1, padx=5, pady=5)

        # Pasang Combobox (Dropdown) untuk Bahasa Masukan
        self.from_lang_combobox = ttk.Combobox(mainFrame, values=["id", "en", 'jw'])
        self.from_lang_combobox.grid(row=1, column=1, padx=5, pady=5)
        self.from_lang_combobox.set("id")

        # Pasang Combobox (Dropdown) untuk Bahasa Keluaran
        self.to_lang_combobox = ttk.Combobox(mainFrame, values=["en", "id", 'jw', 'zh-cn', 'ar'])
        self.to_lang_combobox.grid(row=1, column=3, padx=5, pady=5)
        self.to_lang_combobox.set("en")

        # Pasang Button
        self.btnTranslate = Button(mainFrame, text='Translate!', command=self.onTranslate)
        self.btnTranslate.grid(row=1, column=4, padx=5, pady=5) 

    def onTranslate(self):
        # Membuat instance object
        penterjemah = Translator()

        # Menterjemahkan
        hasil = penterjemah.translate(
            self.txtSumber.get(),
            src=self.from_lang_combobox.get(),
            dest=self.to_lang_combobox.get()
        ) 
       
        # Menampilkan hasil terjemahan
        self.txtHasil.delete(0, END)
        self.txtHasil.insert(END, hasil.text)

    def onKeluar(self, event=None):
        # Memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmTranslator(root, "Program Translator")
    root.mainloop()
