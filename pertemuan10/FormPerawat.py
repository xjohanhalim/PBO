import tkinter as tk
from tkinter import Frame, Label, Entry, Button, Radiobutton, ttk, VERTICAL, YES, BOTH, END, Tk, StringVar, messagebox
from Perawat import Perawat  # Ubah Mahasiswa menjadi Perawat

class FormPerawat:

    def __init__(self, parent, title):
        self.parent = parent
        self.parent.geometry("500x500")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        # Label
        Label(mainFrame, text='NIP:').grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)  # Ganti NIM menjadi NIP
        self.txtNIP = Entry(mainFrame) 
        self.txtNIP.grid(row=0, column=1, padx=5, pady=5)
        self.txtNIP.bind("<Return>", self.onCari)

        Label(mainFrame, text='Nama:').grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtNama = Entry(mainFrame)
        self.txtNama.grid(row=1, column=1, padx=5, pady=5)

        Label(mainFrame, text='Jenis Kelamin:').grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtJK = StringVar()
        self.L = Radiobutton(mainFrame, text='Laki-laki', value='L', variable=self.txtJK)
        self.L.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        self.L.select()
        self.P = Radiobutton(mainFrame, text='Perempuan', value='P', variable=self.txtJK)
        self.P.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        # define columns
        columns = ('id', 'nip', 'nama', 'jk')  # Ganti idmhs, nim menjadi id, nip

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('nip', text='NIP')  # Ganti nim menjadi nip
        self.tree.column('nip', width="60")
        self.tree.heading('nama', text='Nama')
        self.tree.column('nama', width="200")
        self.tree.heading('jk', text='JK')
        self.tree.column('jk', width="30")
        # set tree position
        self.tree.place(x=0, y=200)
        self.onReload()

    def onClear(self, event=None):
        self.txtNIP.delete(0, END)
        self.txtNIP.insert(END, "")
        self.txtNama.delete(0, END)
        self.txtNama.insert(END, "")
        self.btnSimpan.config(text="Simpan")
        self.L.select()
        self.onReload()
        self.ditemukan = False

    def onReload(self, event=None):
        # get data perawat
        perawat = Perawat()  # Ganti Mahasiswa menjadi Perawat
        result = perawat.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        nurses = []
        for row_data in result:
            nurses.append(row_data)

        for nurse in nurses:
            self.tree.insert('', END, values=nurse)

    def onCari(self, event=None):
        nip = self.txtNIP.get()  # Ganti nim menjadi nip
        perawat = Perawat()  # Ganti Mahasiswa menjadi Perawat
        res = perawat.getByNIP(nip)  # Ganti getByNIM menjadi getByNIP
        rec = perawat.affected
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan")
            self.ditemukan = False
            self.txtNama.focus()
        return res

    def TampilkanData(self, event=None):
        nip = self.txtNIP.get()  # Ganti nim menjadi nip
        perawat = Perawat()  # Ganti Mahasiswa menjadi Perawat
        res = perawat.getByNIP(nip)  # Ganti getByNIM menjadi getByNIP
        self.txtNama.delete(0, END)
        self.txtNama.insert(END, perawat.nama)
        jk = perawat.jk
        if jk == "P":
            self.P.select()
        else:
            self.L.select()

    def onSimpan(self, event=None):
        nip = self.txtNIP.get()
        nama = self.txtNama.get()
        jk = self.txtJK.get()

        perawat = Perawat()  # Ganti Mahasiswa menjadi Perawat
        perawat.nip = nip
        perawat.nama = nama
        perawat.jk = jk
        if self.ditemukan == True:
            res = perawat.updateByNIP(nip)  # Ganti updateByNIM menjadi updateByNIP
            ket = 'Diperbarui'
        else:
            res = perawat.simpan()
            ket = 'Disimpan'

        rec = perawat.affected
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Berhasil " + ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal " + ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        nip = self.txtNIP.get()
        perawat = Perawat()  # Ganti Mahasiswa menjadi Perawat
        perawat.nip = nip
        if self.ditemukan == True:
            res = perawat.deleteByNIP(nip)  # Ganti deleteByNIM menjadi deleteByNIP
            rec = perawat.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0

        if rec > 0:
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")

        self.onClear()

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormPerawat(root, "Aplikasi Data Perawat")  # Ganti FormMahasiswa menjadi FormPerawat
    root.mainloop()