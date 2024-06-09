
# filename : FrmPenyewa.py
import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W, SW, NW,StringVar,messagebox
from Penyewa import Penyewa
from FrmDetail_orderan import *
from FrmViewDetail_orderan import *
from bs4 import BeautifulSoup 
import time

# pip install tkcalendar
from tkcalendar import Calendar, DateEntry

class FormPenyewa:   
    def __init__(self, parent, title, update_main_window=None):
        self.parent = parent       
        self.parent.geometry("695x500")
        self.parent.title(title)
        self.update_main_window = update_main_window
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.__data = []
        self.ditemukan = None
        self.totalbayar = None
        self.lunas = None
        self.aturKomponen()
        self.viewDetail = None
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        
         # varchar 
        Label(mainFrame, text='NO_MEJA:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox NO_MEJA
        self.txtNO_MEJA = Entry(mainFrame) 
        self.txtNO_MEJA.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNO_MEJA.bind("<Return>",self.onCari) # menambahkan event Enter key
                
         # varchar 
        Label(mainFrame, text='NAMA:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Textbox NAMA
        self.txtNAMA = Entry(mainFrame) 
        self.txtNAMA.grid(row=1, column=1, padx=5, pady=5)
                
         # int 
        Label(mainFrame, text='JUMLAH_ORANG:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Textbox JUMLAH_ORANG
        self.txtJUMLAH_ORANG = Entry(mainFrame) 
        self.txtJUMLAH_ORANG.grid(row=2, column=1, padx=5, pady=5)
                
         # date 
        Label(mainFrame, text='TANGGAL:').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        # Date Input TANGGAL
        self.txtTANGGAL = DateEntry(mainFrame, width= 16, background= "salmon", foreground= "white",bd=2, date_pattern='y-mm-dd') 
        self.txtTANGGAL.grid(row=3, column=1, padx=5, pady=5)
                    
         # time 
        Label(mainFrame, text='JAM:').grid(row=4, column=0, sticky=W, padx=5, pady=5)

        self.txtJAM = Entry(mainFrame)
        self.txtJAM.grid(row=4, column=1, padx=5, pady=5)
        
        #  # int 
        # Label(mainFrame, text='TOTAL_BAYAR:').grid(row=5, column=0, sticky=W, padx=5, pady=5)
        # # Textbox TOTAL_BAYAR
        # self.txtTOTAL_BAYAR = Entry(mainFrame) 
        # self.txtTOTAL_BAYAR.grid(row=5, column=1, padx=5, pady=5)
                
        #  # tinyint 
        # Label(mainFrame, text='LUNAS:').grid(row=6, column=0, sticky=W, padx=5, pady=5)
        # # Check Box
        # self.txtLUNAS = StringVar()
        # chkLUNAS = tk.Checkbutton(mainFrame, text='Lunas', variable=self.txtLUNAS, onvalue='1', offvalue='0')
        # chkLUNAS.grid(row=6, column=1, padx=5, pady=5)
        # chkLUNAS.deselect()
            
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Reload', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        self.btnView = Button(mainFrame, text='View Detail', command=self.onView, width=10)
        self.btnView.grid(row=3, column=3, sticky=SW ,padx=5, pady=5)
        
        # define columns
        columns = ('id','no_meja','nama','jumlah_orang','tanggal','jam','total_bayar','lunas')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='id')
        self.tree.column('id', width="30")
        self.tree.heading('no_meja', text='no_meja')
        self.tree.column('no_meja', width="30")
        self.tree.heading('nama', text='nama')
        self.tree.column('nama', width="100")
        self.tree.heading('jumlah_orang', text='jumlah_orang')
        self.tree.column('jumlah_orang', width="100")
        self.tree.heading('tanggal', text='tanggal')
        self.tree.column('tanggal', width="100")
        self.tree.heading('jam', text='jam')
        self.tree.column('jam', width="100")
        self.tree.heading('total_bayar', text='total_bayar')
        self.tree.column('total_bayar', width="100")
        self.tree.heading('lunas', text='lunas')
        self.tree.column('lunas', width="100")
        # set tree position
        self.tree.place(x=0, y=250)
        self.onReload()
    
    def onView(self):
        if(self.ditemukan==True):
            self.new_window("View Detail", FrmViewDetail_orderan, self.__data)

    def on_treeview_scroll(self,*args):
        self.tree.yview(*args)

    def clean_html_tags(self,html_text):
        soup = BeautifulSoup(html_text, 'html.parser')
        cleaned_text = soup.get_text()
        return cleaned_text

    
    def onClear(self, event=None):
        self.__data = [] 
        self.ditemukan = None
        self.totalbayar = None
        self.lunas = None
        
        self.txtNO_MEJA.delete(0,END)
        self.txtNO_MEJA.insert(END,"")
                                
        self.txtNAMA.delete(0,END)
        self.txtNAMA.insert(END,"")
                                
        self.txtJUMLAH_ORANG.delete(0,END)
        self.txtJUMLAH_ORANG.insert(END,"")
                                
        # self.txtTOTAL_BAYAR.delete(0,END)
        # self.txtTOTAL_BAYAR.insert(END,"")
                                
        # self.txtLUNAS.set(False)
            
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
        self.__data = [] 
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
            
        self.txtNAMA.delete(0,END)
        self.txtNAMA.insert(END,obj.nama)
                                
        self.txtJUMLAH_ORANG.delete(0,END)
        self.txtJUMLAH_ORANG.insert(END,obj.jumlah_orang)
                                
        self.txtTANGGAL.delete(0,END)
        self.txtTANGGAL.insert(END,obj.tanggal)

        self.txtJAM.delete(0,END)
        self.txtJAM.insert(END,obj.jam)
                                
        # self.txtTOTAL_BAYAR.delete(0,END)
        # self.txtTOTAL_BAYAR.insert(END,obj.total_bayar)
                                
        # self.txtLUNAS.set(obj.lunas)
            
        self.btnSimpan.config(text="Update")
        
        no_meja = self.txtNO_MEJA.get()
        nama = self.txtNAMA.get()
        jumlah_orang = self.txtJUMLAH_ORANG.get()
        tanggal = self.txtTANGGAL.get()
        jam = self.txtJAM.get()
        
        
        self.totalbayar = obj.total_bayar
        self.lunas = obj.lunas
        self.__data.append(no_meja )
        self.__data.append(nama)
        self.__data.append(jumlah_orang)
        self.__data.append(tanggal)
        self.__data.append(jam)
        self.__data.append(self.totalbayar)
        self.__data.append(self.lunas)
        
    def onSimpan(self, event=None):
        no_meja = self.txtNO_MEJA.get()
        nama = self.txtNAMA.get()
        jumlah_orang = self.txtJUMLAH_ORANG.get()
        tanggal = self.txtTANGGAL.get()
        jam = self.txtJAM.get()
        
        # total_bayar = self.txtTOTAL_BAYAR.get()
        # lunas = self.txtLUNAS.get()    
           
        obj = Penyewa()
        
        obj.no_meja = no_meja
        obj.nama = nama
        obj.jumlah_orang = jumlah_orang
        obj.tanggal = tanggal
        obj.jam = jam
        
        # obj.total_bayar = total_bayar
        # obj.lunas = lunas
        
        self.totalbayar = obj.total_bayar
        self.lunas = obj.lunas
        self.__data.append(no_meja )
        self.__data.append(nama)
        self.__data.append(jumlah_orang)
        self.__data.append(tanggal)
        self.__data.append(jam)
        
        if(self.ditemukan==True):
            res = obj.updateByNO_MEJA(no_meja)
            ket = 'Diperbarui'
            
        else:
            obj.total_bayar = 0
            obj.lunas = 0
            res = obj.simpan()
            ket = 'Disimpan'
            
            
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
            # Periksa apakah jendela FrmDetail sudah ada
            self.existing_window_viewDetail = False
            for child in self.parent.winfo_children():
                if isinstance(child, FormDetail_orderan):
                    self.existing_window_viewDetail = True
                    child.lift()  # Bawa jendela FrmDetail ke depan
                    break
        
        if not self.existing_window_viewDetail:  # Jika jendela belum ada, buat yang baru
            time.sleep(2)
            self.new_window("Entry Detail", FormDetail_orderan, self.__data)
            self.onReload()

        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        
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
    aplikasi = FormPenyewa(root, "Aplikasi Data Penyewa")
    root.mainloop() 
    