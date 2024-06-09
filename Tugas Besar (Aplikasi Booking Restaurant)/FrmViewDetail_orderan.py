# filename : FrmViewDetail_orderan.py
 
from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,E, W, font, ttk,messagebox
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from Penyewa import Penyewa
from Detail_orderan import Detail_orderan
from Orderan import Orderan
from datetime import datetime

class FrmViewDetail_orderan:   
    def __init__(self, parent, title, update_main_window=None, extra_data=None):
        self.parent = parent       
        self.parent.geometry("630x500")
        self.parent.title(title)
        self.update_main_window = update_main_window
        self.extra_data=extra_data
        self.no_meja = self.extra_data[0]
        self.nama = self.extra_data[1]
        self.jumlah_orang = self.extra_data[2]
        self.tanggal = self.extra_data[3]
        self.jam = self.extra_data[4]
        self.totalbayar = self.extra_data[5]
        self.lunas = self.extra_data[6]
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.resized_img = None 
        self.aturKomponen()
        self.onReload(self.no_meja)
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        self.txtDisplay=Label(mainFrame)
        self.txtDisplay.place(x=290, y=0)
        self.txtDisplay.configure(text=self.custom_format(self.totalbayar),font=('Arial', 20, 'bold'))
                
         # varchar 
        Label(mainFrame, text='NO_MEJA:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox NO_MEJA
        self.txtNO_MEJA = Label(mainFrame, text=self.no_meja) 
        self.txtNO_MEJA.grid(row=0, column=1, sticky=W, padx=5, pady=5)
                
         # varchar 
        Label(mainFrame, text='NAMA:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Textbox NAMA
        self.txtNAMA = Label(mainFrame, text=self.nama) 
        self.txtNAMA.grid(row=1, column=1, sticky=W, padx=5, pady=5)
                
         # int 
        Label(mainFrame, text='JUMLAH_ORANG:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Textbox JUMLAH_ORANG
        self.txtJUMLAH_ORANG = Label(mainFrame, text=self.jumlah_orang)  
        self.txtJUMLAH_ORANG.grid(row=2, column=1, sticky=W, padx=5, pady=5)
                
         # date 
        Label(mainFrame, text='TANGGAL:').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        # Date Input TANGGAL
        self.txtTANGGAL = Label(mainFrame, text=self.tanggal)
        self.txtTANGGAL.grid(row=3, column=1, sticky=W, padx=5, pady=5)
                    
         # time 
        Label(mainFrame, text='JAM:').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.txtJAM = Label(mainFrame, text=self.jam) 
        self.txtJAM.grid(row=4, column=1, sticky=W, padx=5, pady=5)
        
        Label(mainFrame, text='TOTAL BAYAR:').grid(row=5, column=0, sticky=W, padx=5, pady=5)
        # Date Input TOTAL BAYAR
        self.txtTOTALBAYAR = Label(mainFrame, text=self.custom_format(self.totalbayar))
        self.txtTOTALBAYAR.grid(row=5, column=1, sticky=W, padx=5, pady=5)

        Label(mainFrame, text='LUNAS:').grid(row=6, column=0, sticky=W, padx=5, pady=5)
        # Date Input LUNAS
        self.txtLUNAS = Label(mainFrame, text=self.getStatusLunas(self.lunas))
        self.txtLUNAS.grid(row=6, column=1, sticky=W, padx=5, pady=5)

        Label(mainFrame, text='Total Bayar:').place(x=280, y=350)
        Label(mainFrame, text=self.custom_format(self.totalbayar)).place(x=380, y=400)
        if(self.lunas==0):
            self.btnLunas = Button(mainFrame, text='Set Lunas', bg='green', fg='white', font=('Arial', 10, 'bold'),width=10, command=self.onSetLunas)
            self.btnLunas.place(x=0, y=440)
        
        
        # define columns
        columns = ('id','kode_order','nama_orderan','harga','qty','subtotal')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings', height=7)
        # define headings
        self.tree.heading('id', text='id')
        self.tree.column('id', width="30")
        self.tree.heading('kode_order', text='kode_order')
        self.tree.column('kode_order', width="100")
        self.tree.heading('nama_orderan', text='nama_orderan')
        self.tree.column('nama_orderan', width="100")
        self.tree.heading('harga', text='harga')
        self.tree.column('harga', width="100")
        self.tree.heading('qty', text='qty')
        self.tree.column('qty', width="100")
        self.tree.heading('subtotal', text='subtotal')
        self.tree.column('subtotal', width="100")
        # set tree position
        self.tree.place(x=0, y=250)
        # self.onReload()
        
    def getStatusLunas(self, statuslunas):
        if(statuslunas==1):
            val = "Telah Lunas"
        else:
            val = "Belum Lunas"
        return val
    
    def onSetLunas(self):
        pj = Penyewa()
        val = pj.setLunas(self.no_meja)
        if(val==1):
            messagebox.showinfo("showinfo", "Data Berhasil di set LUNAS")
            self.lunas = 1
            self.txtLUNAS.configure(text=self.getStatusLunas(self.lunas))
            self.btnLunas.destroy()

        else:
            messagebox.showwarning("showwarning", "Data Gagal di set LUNAS")
        
    def custom_format(self,number):
        formatted_number = "{:,.2f}".format(number)
        formatted_number = formatted_number.replace(',', 'temp').replace('.', ',').replace('temp', '.')
        return formatted_number
    
    def flip_date(self,input_date):
        # Parse the input string as a date
        date_object = datetime.strptime(input_date, '%Y-%m-%d')
        # Format the date in the desired way
        flipped_date = date_object.strftime('%d-%m-%Y')
        return flipped_date
    
    def onReload(self, no_meja):
        # get data detail_orderan
        obj = Detail_orderan()
        result = obj.getAllData(no_meja)
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)
        for row in mylist:
            self.tree.insert('',END, values=row)
            
    def onSimpan(self, event=None):
        kode = self.txtKODE.get()
        no_meja = self.txtNO_MEJA.get()
        kode_order = self.txtKODE_ORDER.get()
        qty = self.txtQTY.get()
        harga = self.txtHARGA.get()
        subtotal = self.txtSUBTOTAL.get() 
            
        obj = Detail_orderan()
                
        obj.kode = kode
        obj.no_meja = no_meja
        obj.kode_order = kode_order
        obj.qty = qty
        obj.harga = harga
        obj.subtotal = subtotal
        
        if(self.ditemukan==True):
            res = obj.updateByKODE(kode)
            ket = 'Diperbarui'
            
        else:
            res = obj.simpan()
            ket = 'Disimpan'
            
            
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
            self.onReload(no_meja)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
        
if __name__ == '__main__':
    def update_main_window(result):
        print(result)
    
    root = Tk()
    aplikasi = FrmViewDetail_orderan(root, "Aplikasi Data Detail_orderan")
    root.mainloop() 