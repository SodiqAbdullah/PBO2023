# filename : FrmDetail_orderan.py
 
from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,E, W, font, ttk,messagebox
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from Penyewa import Penyewa
from Detail_orderan import Detail_orderan
from Orderan import Orderan
import random
import string

class FormDetail_orderan:   
    def __init__(self, parent, title, update_main_window=None, extra_data=None):
        self.parent = parent       
        self.parent.geometry("1110x500")
        self.parent.title(title)
        self.update_main_window = update_main_window
        self.extra_data=extra_data
        self.no_meja = self.extra_data[0]
        self.nama = self.extra_data[1]
        self.jumlah_orang = self.extra_data[2]
        self.tanggal = self.extra_data[3]
        self.jam = self.extra_data[4]
        self.totalbayar = 0
        self.lunas = 0
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.resized_img = None 
        self.aturKomponen()
        self.onReload2()
        
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
        
                
         # varchar 
        Label(mainFrame, text='KODE_ORDER:').grid(row=5, column=0, sticky=W, padx=5, pady=5)
        # Textbox KODE_ORDER
        self.txtKODE_ORDER = Entry(mainFrame) 
        self.txtKODE_ORDER.grid(row=6, column=0, padx=5, pady=5)
        self.txtKODE_ORDER.bind("<Return>",self.onCari) # menambahkan event Enter key
        
                
        Label(mainFrame, text='NAMA_ORDERAN:').grid(row=5, column=1, sticky=W, padx=5, pady=5)
        # Textbox NAMA_ORDERAN
        self.txtNAMA_ORDERAN = Entry(mainFrame) 
        self.txtNAMA_ORDERAN.grid(row=6, column=1, padx=5, pady=5)
                
         # int 
        Label(mainFrame, text='QTY:').grid(row=5, column=2, sticky=W, padx=5, pady=5)
        # Textbox QTY
        self.txtQTY = Entry(mainFrame) 
        self.txtQTY.grid(row=6, column=2, padx=5, pady=5)
        self.txtQTY.delete(0,END)
        self.txtQTY.insert(END,"1")
                
         # int 
        Label(mainFrame, text='HARGA:').grid(row=5, column=3, sticky=W, padx=5, pady=5)
        # Textbox HARGA
        self.txtHARGA = Entry(mainFrame) 
        self.txtHARGA.grid(row=6, column=3, padx=5, pady=5)
                
        self.btnSimpan = Button(mainFrame, text='+', bg='orange', fg='black', font=('Arial', 10, 'bold'),width=5, command=self.onSimpan)
        self.btnSimpan.grid(row=4, column=5, padx=5, pady=5)

        self.btnLunas = Button(mainFrame, text='Set Lunas', bg='green', fg='white', font=('Arial', 10, 'bold'),width=10, command=self.onSetLunas)
        self.btnLunas.place(x=0, y=440)

        self.LabelTotalBayar = Label(mainFrame, text='Total Bayar:').place(x=280, y=440)
        self.txtTotalBayar = Label(mainFrame)
        self.txtTotalBayar.place(x=380, y=440)
        
        
        self.txtMenu = Label(mainFrame, text='Menu')
        self.txtMenu.place(x=700, y=50)
        
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
        
        columns2 = ('id','kode_order','nama_orderan','harga')
        self.tree2 = ttk.Treeview(mainFrame, columns=columns2, show='headings', height=15)
        # define headings
        self.tree2.heading('id', text='id')
        self.tree2.column('id', width="30")
        self.tree2.heading('kode_order', text='kode_order')
        self.tree2.column('kode_order', width="50")
        self.tree2.heading('nama_orderan', text='nama_orderan')
        self.tree2.column('nama_orderan', width="150")
        self.tree2.heading('harga', text='harga')
        self.tree2.column('harga', width="150")
        # set tree2 position
        self.tree2.place(x=700, y=100)
        
    def custom_format(self,number):
        formatted_number = "{:,.2f}".format(number)
        formatted_number = formatted_number.replace(',', 'temp').replace('.', ',').replace('temp', '.')
        return formatted_number

    def generate_random_string(self,length):
        characters = string.ascii_letters + string.digits + string.punctuation
        # Remove unwanted characters
        characters = ''.join(char for char in characters if char not in 'iIoO0')
        return ''.join(random.choice(characters) for _ in range(length))
    
    def onCari(self, event=None):
        kode = self.txtKODE_ORDER.get()
        obj = Orderan()
        res = obj.getByKODE_ORDER(kode)
        rec = obj.affected
        if(rec>0):
            self.TampilkanData()
            self.ditemukan = False
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = None
        return res
    
    def TampilkanData(self):
        kode_order = self.txtKODE_ORDER.get()
        obj = Orderan()
        res = obj.getByKODE_ORDER(kode_order)
            
        self.txtNAMA_ORDERAN.delete(0,END)
        self.txtNAMA_ORDERAN.insert(END,obj.nama_orderan)
                                
        self.txtHARGA.delete(0,END)
        self.txtHARGA.insert(END,obj.harga)
        
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
            
    def onReload2(self, event=None):
        # get data orderan
        obj = Orderan()
        result = obj.getAllData()
        for item in self.tree2.get_children():
            self.tree2.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)
        for row in mylist:
            self.tree2.insert('',END, values=row)
            
    def onSetLunas(self):
        pj = Penyewa()
        val = pj.setLunas(self.no_meja)
        if(val==1):
            messagebox.showinfo("showinfo", "Data Berhasil di set LUNAS")
            self.btnSimpan.destroy()
            self.btnLunas.destroy()

        else:
            messagebox.showwarning("showwarning", "Data Gagal di set LUNAS")
        
    def onClear(self, event=None):
        self.txtKODE_ORDER.delete(0,END)
        self.txtKODE_ORDER.insert(END,"")
                                
        # self.txtNO_MEJA.delete(0,END)
        # self.txtNO_MEJA.insert(END,"")
                                
        self.txtNAMA_ORDERAN.delete(0,END)
        self.txtNAMA_ORDERAN.insert(END,"")
                                
        self.txtQTY.delete(0,END)
        self.txtQTY.insert(END,"1")
                                
        self.txtHARGA.delete(0,END)
        self.txtHARGA.insert(END,"")
                                
        # self.txtSUBTOTAL.delete(0,END)
        # self.txtSUBTOTAL.insert(END,"")
                                
        self.btnSimpan.config(text="+")
        self.onReload(self.no_meja)
        self.onReload2()
        self.ditemukan = False
        
    def onSimpan(self, event=None):
        kode = self.generate_random_string(5)
        no_meja = self.no_meja
        kode_order = self.txtKODE_ORDER.get()
        qty = self.txtQTY.get()
        harga = self.txtHARGA.get()
        subtotal = int(qty) * float(harga)   
            
        obj = Detail_orderan()
        pj = Penyewa()
        tb = pj.getTotalbayar(no_meja)
        
        obj.kode = kode
        obj.no_meja = no_meja
        obj.kode_order = kode_order
        obj.qty = qty
        obj.harga = harga
        obj.subtotal = subtotal
        
        res = obj.simpan()
        ket = 'Disimpan'
        
        rec = obj.affected
        if(rec>0):
            total = int(tb) + int(subtotal)
            self.totalbayar = total
            pj.updateTotalbayar(total, no_meja)
            self.onReload(no_meja)
            self.onReload2()
            self.txtDisplay.configure(text=self.custom_format(self.totalbayar),font=('Arial', 20, 'bold'))
            self.txtTotalBayar.configure(text=self.custom_format(self.totalbayar))
            self.onClear()
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        
        return rec
 
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
        
if __name__ == '__main__':
    def update_main_window(result):
        print(result)
    
    root = Tk()
    aplikasi = FormDetail_orderan(root, "Aplikasi Data Detail_orderan")
    root.mainloop() 