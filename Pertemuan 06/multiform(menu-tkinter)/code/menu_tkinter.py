import tkinter as tk
from tkinter import messagebox, Menu
from balok_gui import balok_gui
from bola_gui import bola_gui
from kerucut_gui import kerucut_gui
from kubus_gui import kubus_gui
from limas_segiempat_gui import limas_segiempat_gui
from limas_segitiga_gui import limas_segitiga_gui
from prisma_segitiga_gui import prisma_segitiga_gui
from tabung_gui import tabung_gui

def show_about():
    messagebox.showinfo("About", "Ini adalah tugas pertemuan ke 6 untuk membuat menu yang dapat menampilkan aplikasi menghitung luas dan volume bangun ruang")

def exit_app():
    if messagebox.askokcancel("Exit", "Ingin keluar?"):
        root.destroy()

# untuk membuat jendela mengambang
def window_mengambang(_class):
    new = tk.Toplevel()
    new.transient()
    new.grab_set()
    _class(new)

root = tk.Tk()
root.title("Tkinter Menu")
root.geometry("400x300")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# tampilan menu
file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

app_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="App", menu=app_menu)

# isi menu App
app_menu.add_command(label="balok", command=lambda: window_mengambang(balok_gui))
app_menu.add_command(label="bola", command=lambda: window_mengambang(bola_gui))
app_menu.add_command(label="kerucut", command=lambda: window_mengambang(kerucut_gui))
app_menu.add_command(label="kubus", command=lambda: window_mengambang(kubus_gui))
app_menu.add_command(label="limas segiempat", command=lambda: window_mengambang(limas_segiempat_gui))
app_menu.add_command(label="limas segitiga", command=lambda: window_mengambang(limas_segitiga_gui))
app_menu.add_command(label="prisma segitiga", command=lambda: window_mengambang(prisma_segitiga_gui))
app_menu.add_command(label="tabung", command=lambda: window_mengambang(tabung_gui))


help_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=show_about)

root.mainloop()
