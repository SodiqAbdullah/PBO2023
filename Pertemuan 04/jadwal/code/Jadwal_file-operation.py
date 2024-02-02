import tkinter as tk
from tkinter import ttk, filedialog
import os

class JadwalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Jadwal")

        self.jadwal = []
        self.load_jadwal_from_file()

        self.create_ui()

    def create_ui(self):
        # Treeview untuk menampilkan jadwal
        self.tree = ttk.Treeview(self.root, columns=('Hari', 'Waktu', 'Matakuliah'), show='headings')
        self.tree.heading('Hari', text='Hari')
        self.tree.heading('Waktu', text='Waktu')
        self.tree.heading('Matakuliah', text='Matakuliah')
        self.tree.pack(padx=10, pady=10)

        # Tombol-tombol
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        tambah_button = tk.Button(button_frame, text="Tambah Matakuliah", command=self.tambah_kegiatan)
        tambah_button.grid(row=0, column=0, padx=5)

        simpan_button = tk.Button(button_frame, text="Simpan Jadwal", command=self.simpan_jadwal)
        simpan_button.grid(row=0, column=1, padx=5)

        muat_button = tk.Button(button_frame, text="Muat Jadwal", command=self.muat_jadwal)
        muat_button.grid(row=0, column=2, padx=5)

    def tambah_kegiatan(self):
        # Membuat jendela pop-up untuk menambah Matakuliah baru
        popup = tk.Toplevel(self.root)
        popup.title("Tambah Matakuliah")

        hari_label = tk.Label(popup, text="Hari:")
        hari_label.grid(row=0, column=0, padx=5, pady=5)

        waktu_label = tk.Label(popup, text="Waktu:")
        waktu_label.grid(row=1, column=0, padx=5, pady=5)

        kegiatan_label = tk.Label(popup, text="Matakuliah:")
        kegiatan_label.grid(row=2, column=0, padx=5, pady=5)

        hari_entry = tk.Entry(popup)
        hari_entry.grid(row=0, column=1, padx=5, pady=5)

        waktu_entry = tk.Entry(popup)
        waktu_entry.grid(row=1, column=1, padx=5, pady=5)

        kegiatan_entry = tk.Entry(popup)
        kegiatan_entry.grid(row=2, column=1, padx=5, pady=5)

        tambah_button = tk.Button(popup, text="Tambah", command=lambda: self.tambah_kegiatan_popup(hari_entry.get(), waktu_entry.get(), kegiatan_entry.get(), popup))
        tambah_button.grid(row=3, column=0, columnspan=2, pady=10)

    def tambah_kegiatan_popup(self, hari, waktu, Matakuliah, popup):
        if hari and waktu and Matakuliah:
            self.jadwal.append((hari, waktu, Matakuliah))
            self.tampilkan_jadwal()
            popup.destroy()

    def tampilkan_jadwal(self):
        # Membersihkan treeview sebelum menampilkan kembali jadwal
        for i in self.tree.get_children():
            self.tree.delete(i)

        # Menampilkan jadwal ke dalam treeview
        for Matakuliah in self.jadwal:
            self.tree.insert("", "end", values=Matakuliah)

    def simpan_jadwal(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                for Matakuliah in self.jadwal:
                    file.write(','.join(Matakuliah) + '\n')

    def muat_jadwal(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.jadwal.clear()
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    Matakuliah = line.strip().split(',')
                    self.jadwal.append(tuple(Matakuliah))
            self.tampilkan_jadwal()

    def load_jadwal_from_file(self):
        file_path = "jadwal.txt"
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    Matakuliah = line.strip().split(',')
                    self.jadwal.append(tuple(Matakuliah))

if __name__ == "__main__":
    root = tk.Tk()
    app = JadwalApp(root)
    root.mainloop()
