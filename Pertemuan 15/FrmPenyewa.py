
# filename : FrmPenyewa.py
import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Penyewa import Penyewa
# pip install tkcalendar
from tkcalendar import Calendar, DateEntry
class FormPenyewa:   
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("750x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        
        
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        
         # int 
        Label(mainFrame, text='NO_MEJA:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox NO_MEJA
        self.txtNO_MEJA = Entry(mainFrame) 
        self.txtNO_MEJA.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNO_MEJA.bind("<Return>",self.onCari) # menambahkan event Enter key
                
         # varchar 
        Label(mainFrame, text='PENYEWA:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Textbox PENYEWA
        self.txtPENYEWA = Entry(mainFrame) 
        self.txtPENYEWA.grid(row=1, column=1, padx=5, pady=5)
                
         # date 
        Label(mainFrame, text='TANGGAL:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Date Input TANGGAL
        self.txtTANGGAL = DateEntry(mainFrame, width= 16, background= "magenta3", foreground= "white",bd=2, date_pattern='y-mm-dd') 
        self.txtTANGGAL.grid(row=2, column=1, padx=5, pady=5)
                    
         # time 
        Label(mainFrame, text='JAM:').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.txtJAM = Entry(mainFrame)
        self.txtJAM.grid(row=3, column=1, padx=5, pady=5) 
        # Combo Box
        # self.txtJAM = StringVar()
        # CboJAM = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtJAM) 
        # CboJAM.grid(row=3, column=1, padx=5, pady=5)
        # # Adding combobox drop down list
        # CboJAM['values'] = ('time')
        # CboJAM.current()
        
         # int 
        Label(mainFrame, text='JUMLAH_KURSI:').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        # Textbox JUMLAH_KURSI
        self.txtJUMLAH_KURSI = Entry(mainFrame) 
        self.txtJUMLAH_KURSI.grid(row=4, column=1, padx=5, pady=5)
                
         # varchar 
        Label(mainFrame, text='MAKANAN:').grid(row=5, column=0, sticky=W, padx=5, pady=5)
        # Textbox MAKANAN
        self.txtMAKANAN = Entry(mainFrame) 
        self.txtMAKANAN.grid(row=5, column=1, padx=5, pady=5)
                
         # varchar 
        Label(mainFrame, text='MINUMAN:').grid(row=6, column=0, sticky=W, padx=5, pady=5)
        # Textbox MINUMAN
        self.txtMINUMAN = Entry(mainFrame) 
        self.txtMINUMAN.grid(row=6, column=1, padx=5, pady=5)
                
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        
        # define columns
        columns = ('no','no_meja','penyewa','tanggal','jam','jumlah_kursi','makanan','minuman')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('no', text='no')
        self.tree.column('no', width="26")
        self.tree.heading('no_meja', text='no_meja')
        self.tree.column('no_meja', width="59")
        self.tree.heading('penyewa', text='penyewa')
        self.tree.column('penyewa', width="100")
        self.tree.heading('tanggal', text='tanggal')
        self.tree.column('tanggal', width="100")
        self.tree.heading('jam', text='jam')
        self.tree.column('jam', width="100")
        self.tree.heading('jumlah_kursi', text='jumlah_kursi')
        self.tree.column('jumlah_kursi', width="100")
        self.tree.heading('makanan', text='makanan')
        self.tree.column('makanan', width="100")
        self.tree.heading('minuman', text='minuman')
        self.tree.column('minuman', width="100")
        # set tree position
        self.tree.place(x=0, y=250)
        self.onReload()
    
    def onClear(self, event=None):
        self.txtNO_MEJA.delete(0,END)
        self.txtNO_MEJA.insert(END,"")
                                
        self.txtPENYEWA.delete(0,END)
        self.txtPENYEWA.insert(END,"")
                                
        self.txtJUMLAH_KURSI.delete(0,END)
        self.txtJUMLAH_KURSI.insert(END,"")
                                
        self.txtMAKANAN.delete(0,END)
        self.txtMAKANAN.insert(END,"")
                                
        self.txtMINUMAN.delete(0,END)
        self.txtMINUMAN.insert(END,"")
                                
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data penyewa
        obj = Penyewa()
        result = obj.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)
        for row in mylist:
            self.tree.insert('',END, values=row)
            
    def onCari(self, event=None):
        no_meja = self.txtNO_MEJA.get()
        obj = Penyewa()
        res = obj.getByNO_MEJA(no_meja)
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            # self.txtNama.focus()
        return res
            
    def TampilkanData(self, event=None):
        no_meja = self.txtNO_MEJA.get()
        obj = Penyewa()
        res = obj.getByNO_MEJA(no_meja)
            
        self.txtPENYEWA.delete(0,END)
        self.txtPENYEWA.insert(END,obj.penyewa)
                                
        self.txtTANGGAL.delete(0,END)
        self.txtTANGGAL.insert(END,obj.tanggal)
                                
        self.txtJUMLAH_KURSI.delete(0,END)
        self.txtJUMLAH_KURSI.insert(END,obj.jumlah_kursi)
                                
        self.txtMAKANAN.delete(0,END)
        self.txtMAKANAN.insert(END,obj.makanan)
                                
        self.txtMINUMAN.delete(0,END)
        self.txtMINUMAN.insert(END,obj.minuman)
                                
        self.btnSimpan.config(text="Update")
    def onSimpan(self, event=None):
        no_meja = self.txtNO_MEJA.get()
        penyewa = self.txtPENYEWA.get()
        tanggal = self.txtTANGGAL.get()
        jam = self.txtJAM.get()
        jumlah_kursi = self.txtJUMLAH_KURSI.get()
        makanan = self.txtMAKANAN.get()
        minuman = self.txtMINUMAN.get()       
        obj = Penyewa()
        obj.no_meja = no_meja
        obj.penyewa = penyewa
        obj.tanggal = tanggal
        obj.jam = jam
        obj.jumlah_kursi = jumlah_kursi
        obj.makanan = makanan
        obj.minuman = minuman
        if(self.ditemukan==True):
            res = obj.updateByNO_MEJA(no_meja)
            ket = 'Diperbarui'
            
        else:
            res = obj.simpan()
            ket = 'Disimpan'
            
            
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec
 
    def onDelete(self, event=None):
        no_meja = self.txtNO_MEJA.get()
        obj = Penyewa()
        obj.no_meja = no_meja
        if(self.ditemukan==True):
            res = obj.deleteByNO_MEJA(no_meja)
            rec = obj.affected
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
    aplikasi = FormPenyewa(root, "Aplikasi Data Penyewa")
    root.mainloop() 