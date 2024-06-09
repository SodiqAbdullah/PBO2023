# filename : FrmOrderan.py
import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Orderan import Orderan
class FormOrderan:   
    def __init__(self, parent, title, update_main_window=None):
        self.parent = parent       
        self.parent.geometry("400x500")
        self.parent.title(title)
        self.update_main_window = update_main_window
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        
        
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        
         # varchar 
        Label(mainFrame, text='KODE_ORDER:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox KODE_ORDER
        self.txtKODE_ORDER = Entry(mainFrame) 
        self.txtKODE_ORDER.grid(row=0, column=1, padx=5, pady=5) 
        self.txtKODE_ORDER.bind("<Return>",self.onCari) # menambahkan event Enter key
                
         # varchar 
        Label(mainFrame, text='NAMA_ORDERAN:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Textbox NAMA_ORDERAN
        self.txtNAMA_ORDERAN = Entry(mainFrame) 
        self.txtNAMA_ORDERAN.grid(row=1, column=1, padx=5, pady=5)
                
         # int 
        Label(mainFrame, text='HARGA:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Textbox HARGA
        self.txtHARGA = Entry(mainFrame) 
        self.txtHARGA.grid(row=2, column=1, padx=5, pady=5)
                
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        
        # define columns
        columns = ('id','kode_order','nama_orderan','harga')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings', height=15)
        # define headings
        self.tree.heading('id', text='id')
        self.tree.column('id', width="30")
        self.tree.heading('kode_order', text='kode_order')
        self.tree.column('kode_order', width="50")
        self.tree.heading('nama_orderan', text='nama_orderan')
        self.tree.column('nama_orderan', width="150")
        self.tree.heading('harga', text='harga')
        self.tree.column('harga', width="150")
        # set tree position
        self.tree.place(x=0, y=150)
        self.onReload()
    
    def onClear(self, event=None):
        self.txtKODE_ORDER.delete(0,END)
        self.txtKODE_ORDER.insert(END,"")
                                
        self.txtNAMA_ORDERAN.delete(0,END)
        self.txtNAMA_ORDERAN.insert(END,"")
                                
        self.txtHARGA.delete(0,END)
        self.txtHARGA.insert(END,"")
                                
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data orderan
        obj = Orderan()
        result = obj.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)
        for row in mylist:
            self.tree.insert('',END, values=row)
            
    def onCari(self, event=None):
        kode_order = self.txtKODE_ORDER.get()
        obj = Orderan()
        res = obj.getByKODE_ORDER(kode_order)
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
        kode_order = self.txtKODE_ORDER.get()
        obj = Orderan()
        res = obj.getByKODE_ORDER(kode_order)
            
        self.txtNAMA_ORDERAN.delete(0,END)
        self.txtNAMA_ORDERAN.insert(END,obj.nama_orderan)
                                
        self.txtHARGA.delete(0,END)
        self.txtHARGA.insert(END,obj.harga)
                                
        self.btnSimpan.config(text="Update")
    def onSimpan(self, event=None):
        kode_order = self.txtKODE_ORDER.get()
        nama_orderan = self.txtNAMA_ORDERAN.get()
        harga = self.txtHARGA.get()       
        obj = Orderan()
        obj.kode_order = kode_order
        obj.nama_orderan = nama_orderan
        obj.harga = harga
        if(self.ditemukan==True):
            res = obj.updateByKODE_ORDER(kode_order)
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
        kode_order = self.txtKODE_ORDER.get()
        obj = Orderan()
        obj.kode_order = kode_order
        if(self.ditemukan==True):
            res = obj.deleteByKODE_ORDER(kode_order)
            rec = obj.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
 
    def new_window(self, number, _class, extra_data):
        new = tk.Toplevel(self.parent)
        new.transient()
        new.grab_set()
        _class(new, number, self.update_main_window, extra_data)

    def update_main_window(self, data):
        # Method to receive data from child windows
        self.__data = data
        level = self.__data[0]
        loginvalid = self.__data[1]
        if(loginvalid==True):
            index = self.file_menu.index('Login')
            # hapus menu login
            self.file_menu.delete(index)
            self.file_menu.add_command(label='Logout', command=self.Logout)

            # tambahkan menu sesuai level
            if(level=='admin'): 
                self.menubar.add_cascade(label="Admin", menu=self.admin_menu)
                self.__level = 'Admin'
            else:
                pass
 
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
        
if __name__ == '__main__':
    def update_main_window(result):
        print(result)
    
    root = tk.Tk()
    aplikasi = FormOrderan(root, "Aplikasi Data Orderan")
    root.mainloop() 
    