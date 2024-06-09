	# filename : FrmUsers.py
import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Users import Users
import bcrypt


class FormUsers:   
    def __init__(self, parent, title, update_main_window):
        self.parent = parent
        self.update_main_window = update_main_window
        self.parent.geometry("250x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        
        
        self.ditemukan = None
        self.aturKomponen()
        # self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        
         # varchar 
        Label(mainFrame, text='EMAIL:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox EMAIL
        self.txtEMAIL = Entry(mainFrame) 
        self.txtEMAIL.grid(row=0, column=1, padx=5, pady=5) 
        # self.txtEMAIL.bind("<Return>",self.onCari) # menambahkan event Enter key
                
         # varchar 
        Label(mainFrame, text='NAMA:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Textbox NAMA
        self.txtNAMA = Entry(mainFrame) 
        self.txtNAMA.grid(row=1, column=1, padx=5, pady=5)
                
         # varchar 
        Label(mainFrame, text='PASSWORD:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Textbox PASSWORD
        self.txtPASSWORD = Entry(mainFrame) 
        self.txtPASSWORD.grid(row=2, column=1, padx=5, pady=5)
                
         # enum 
        Label(mainFrame, text='LEVEL:').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        # # Combo Box
        self.txtLEVEL = Entry(mainFrame)
        self.txtLEVEL.insert(END,"Customer")
        self.txtLEVEL.grid(row=3, column=1, sticky=W, padx=5, pady=5)
        self.txtLEVEL.config(state='disabled')
        # CboLEVEL = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtLEVEL) 
        # CboLEVEL.grid(row=3, column=1, padx=5, pady=5)
        # # Adding combobox drop down list
        # CboLEVEL['values'] = ('admin','customer')
        # CboLEVEL.current()
        # Label(mainFrame, text='Customer').grid(row=3, column=1, sticky=W, padx=5, pady=5)
        
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=30)
        self.btnSimpan.grid(row=4, column=0, columnspan=2, padx=5, pady=10)
        # self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        # self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        # self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        # self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        
        # # define columns
        # columns = ('id','email','nama','password','level')
        # self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # # define headings
        # self.tree.heading('id', text='id')
        # self.tree.column('id', width="30")
        # self.tree.heading('email', text='email')
        # self.tree.column('email', width="30")
        # self.tree.heading('nama', text='nama')
        # self.tree.column('nama', width="100")
        # self.tree.heading('password', text='password')
        # self.tree.column('password', width="100")
        # self.tree.heading('level', text='level')
        # self.tree.column('level', width="100")
        # # set tree position
        # self.tree.place(x=0, y=250)
        # self.onReload()
    
    # def onClear(self, event=None):
    #     self.txtEMAIL.delete(0,END)
    #     self.txtEMAIL.insert(END,"")
                                
    #     self.txtNAMA.delete(0,END)
    #     self.txtNAMA.insert(END,"")
                                
    #     self.txtPASSWORD.delete(0,END)
    #     self.txtPASSWORD.insert(END,"")
                                
    #     self.txtLEVEL.set("")
            
    #     self.btnSimpan.config(text="Simpan")
    #     self.onReload()
    #     self.ditemukan = False
        
    # def onReload(self, event=None):
    #     # get data users
    #     obj = Users()
    #     result = obj.getAllData()
    #     for item in self.tree.get_children():
    #         self.tree.delete(item)
    #     mylist=[]
    #     for row_data in result:
    #         mylist.append(row_data)
    #     for row in mylist:
    #         self.tree.insert('',END, values=row)
            
    # def onCari(self, event=None):
    #     email = self.txtEMAIL.get()
    #     obj = Users()
    #     res = obj.getByEMAIL(email)
    #     rec = obj.affected
    #     if(rec>0):
    #         messagebox.showinfo("showinfo", "Data Ditemukan")
    #         self.TampilkanData()
    #         self.ditemukan = True
    #     else:
    #         messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
    #         self.ditemukan = False
    #         # self.txtNama.focus()
    #     return res
            
    # def TampilkanData(self, event=None):
    #     email = self.txtEMAIL.get()
    #     obj = Users()
    #     res = obj.getByEMAIL(email)
            
    #     self.txtNAMA.delete(0,END)
    #     self.txtNAMA.insert(END,obj.nama)
                                
    #     self.txtPASSWORD.delete(0,END)
    #     self.txtPASSWORD.insert(END,obj.password)
                                
    #     self.txtLEVEL.set(obj.level)
            
    #     self.btnSimpan.config(text="Update")
        
    def onSimpan(self, event=None):
        email = self.txtEMAIL.get()
        nama = self.txtNAMA.get()
        password = self.txtPASSWORD.get()
        level = self.txtLEVEL.get()

        # Enkripsi password menggunakan bcrypt
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        obj = Users()
        obj.email = email
        obj.nama = nama
        obj.password = hashed_password.decode('utf-8')  # Decode hasil enkripsi untuk disimpan di database
        obj.level = level

        if self.ditemukan:
            res = obj.updateByEMAIL(email)
            ket = 'Diperbarui'
        else:
            res = obj.simpan()
            ket = 'Disimpan'

        rec = obj.affected
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Berhasil " + ket)
            # self.update_main_window(val)
            self.parent.destroy()
        else:
            messagebox.showwarning("showwarning", "Data Gagal " + ket)
        # self.onClear()
        return rec

    # def onDelete(self, event=None):
    #     email = self.txtEMAIL.get()
    #     obj = Users()
    #     obj.email = email
    #     if(self.ditemukan==True):
    #         res = obj.deleteByEMAIL(email)
    #         rec = obj.affected
    #     else:
    #         messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
    #         rec = 0
        
    #     if(rec>0):
    #         messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
    #     self.onClear()
 
 
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
        
if __name__ == '__main__':
    def update_main_window(result):
        print(result)

    root = tk.Tk()
    aplikasi = FormUsers(root, "Registrasi")
    root.mainloop() 