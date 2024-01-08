import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Dokter import Dokter

class FormDokter:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("600x500")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Label
        Label(mainFrame, text='NIP:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txtNIP = Entry(mainFrame) 
        self.txtNIP.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNIP.bind("<Return>",self.onCari) # menambahkan event Enter key

        Label(mainFrame, text='Nama Dokter:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5) 

        Label(mainFrame, text='Jenis Kelamin:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtJK = StringVar()
        self.L = Radiobutton(mainFrame, text='Laki-laki', value='L', variable=self.txtJK)
        self.L.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        self.L.select() # set pilihan yg pertama
        self.P = Radiobutton(mainFrame, text='Perempuan', value='P', variable=self.txtJK)
        self.P.grid(row=3, column=1, padx=5, pady=5, sticky=W)
        
        Label(mainFrame, text='Spesialis:').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.txtspesialis = Entry(mainFrame) 
        self.txtspesialis.grid(row=4, column=1, padx=5, pady=5) 
        
        Label(mainFrame, text='Tempat Bertugas:').grid(row=5, column=0, sticky=W, padx=5, pady=5)
        self.txttempat_bertugas = Entry(mainFrame) 
        self.txttempat_bertugas.grid(row=5, column=1, padx=5, pady=5) 

        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        # define columns
        columns = ('id', 'nip', 'nama','jk', 'spesialis', 'tempat_bertugas')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('nip', text='NIP')
        self.tree.column('nip', width="60")
        self.tree.heading('nama', text='Nama Dokter')
        self.tree.column('nama', width="120")
        self.tree.heading('jk', text='JK')
        self.tree.column('jk', width="30")
        self.tree.heading('spesialis', text='Spesialis')
        self.tree.column('spesialis', width="80")
        self.tree.heading('tempat_bertugas', text='Tempat Bertugas')
        self.tree.column('tempat_bertugas', width="200")
        # set tree position
        self.tree.place(x=0, y=250)
        self.onReload()
        
    def onClear(self, event=None):
        self.txtNIP.delete(0,END)
        self.txtNIP.insert(END,"")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")
        self.txtspesialis.delete(0,END)
        self.txtspesialis.insert(END,"")
        self.txttempat_bertugas.delete(0,END)
        self.txttempat_bertugas.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.L.select()
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data Dokter
        mhs = Dokter()
        result = mhs.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        students=[]
        for row_data in result:
            students.append(row_data)

        for student in students:
            self.tree.insert('',END, values=student)
    
    def onCari(self, event=None):
        nip = self.txtNIP.get()
        mhs = Dokter()
        res = mhs.getByNIP(nip)
        rec = mhs.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txtNama.focus()
        return res
        
    def TampilkanData(self, event=None):
        nip = self.txtNIP.get()
        mhs = Dokter()
        res = mhs.getByNIP(nip)
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,mhs.nama)
        jk = mhs.jk
        if(jk=="P"):
            self.P.select()
        else:
            self.L.select()
        self.txtspesialis.delete(0,END)
        self.txtspesialis.insert(END,mhs.spesialis)
        self.txttempat_bertugas.delete(0,END)
        self.txttempat_bertugas.insert(END,mhs.tempat_bertugas)   
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        nip = self.txtNIP.get()
        nama = self.txtNama.get()
        jk = self.txtJK.get()
        spesialis = self.txtspesialis.get()
        tempat_bertugas = self.txttempat_bertugas.get()
        
        mhs = Dokter()
        mhs.nip = nip
        mhs.nama = nama
        mhs.jk = jk
        mhs.spesialis = spesialis
        mhs.tempat_bertugas = tempat_bertugas

        if(self.ditemukan==True):
            res = mhs.updateByNIP(nip)
            ket = 'Diperbarui'
        else:
            res = mhs.simpan()
            ket = 'Disimpan'
            
        rec = mhs.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        nip = self.txtNIP.get()
        mhs = Dokter()
        mhs.nip = nip
        if(self.ditemukan==True):
            res = mhs.deleteByNIP(nip)
            rec = mhs.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormDokter(root, "Aplikasi Data Dokter")
    root.mainloop() 