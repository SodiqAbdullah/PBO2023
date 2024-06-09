# Dashboard.py

import tkinter as tk
from tkinter import Menu, messagebox
from FrmLogin import *
from FrmUsers import *
from FrmPenyewa import *
from FrmOrderan import *

class Dashboard:
    def __init__(self):
        # root window
        self.root = tk.Tk()
        self.root.title('Dashboard Order Restoran')
        # self.root.attributes('-fullscreen', True)
        self.root.geometry("900x400")
        self.__data = None
        self.__level = None
        # create a menubar
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)

        # create menus
        # self.menubar = Menu(self.menubar)
        self.guest_menu = Menu(self.menubar)
        self.admin_menu = Menu(self.menubar)
        self.customer_menu = Menu(self.menubar)

        # add menu items to File menu
        self.menubar.add_command(label='Login', command=lambda: self.new_window("LogIn", FormLogin))
        self.menubar.add_command(label='Registrasi', command=lambda: self.new_window("Registrasi", FormUsers))
        self.menubar.add_command(label='Exit', command=self.root.destroy)

        # add menu items to menu Admin
        self.admin_menu.add_command(label='Penyewa-Admin', command=lambda: self.new_window("Order Restoran", FormPenyewa))
        
        self.admin_menu.add_command(label='list-makan&minum', command=lambda: self.new_window("Order Restoran", FormOrderan))

        # add menu items to menu customerustomer
        self.customer_menu.add_command(label='Penyewa', command=lambda: self.new_window("Order Restoran", FormPenyewa))
        

    def new_window(self, number, _class):
        new = tk.Toplevel(self.root)
        new.transient()
        new.grab_set()
        _class(new, number, self.update_main_window)

    def update_main_window(self, data):
        # Method to receive data from child windows
        self.__data = data
        level = self.__data[0]
        loginvalid = self.__data[1]
        if(loginvalid==True):
            # index = self.menubar.index('Login')
            # hapus menu login
            self.menubar.delete(self.menubar.index('Login'))
            self.menubar.delete(self.menubar.index('Registrasi'))
            self.menubar.add_command(label='Logout', command=self.Logout)

            # tambahkan menu sesuai level
            if(level=='admin'): 
                self.menubar.add_cascade(label="Admin", menu=self.admin_menu)
                self.__level = 'Admin'
            elif(level=='customer'): 
                self.menubar.add_cascade(label="Customer", menu=self.customer_menu)
                self.__level = 'Customer'
            else:
                pass

    def Logout(self):
        index = self.menubar.index('Logout')
        # index = self.menubar.index('Registrasi')
        self.menubar.delete(index)
        self.menubar.add_command(label='Login', command=lambda: self.new_window("LogIn", FormLogin))
        self.menubar.add_command(label='Registrasi', command=lambda: self.new_window("Registrasi", FormUsers))
        self.remove_all_menus()

    def remove_all_menus(self):
        index = self.menubar.index(self.__level)
        if index is not None:
            self.menubar.delete(index)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    menu_app = Dashboard()
    menu_app.run()
