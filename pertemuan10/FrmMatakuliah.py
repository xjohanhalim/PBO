import tkinter as tk
from tkinter import Frame, Label, Entry, Button, Radiobutton, ttk, VERTICAL, YES, BOTH, END, Tk, StringVar, messagebox
from Matakuliah import Matakuliah  # Assuming you have a Matakuliah class

class FormMatakuliah:

    def __init__(self, parent, title):
        self.parent = parent
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        # Label
        Label(mainFrame, text='Kode MK:').grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.txtKodeMK = Entry(mainFrame)
        self.txtKodeMK.grid(row=0, column=1, padx=5, pady=5)
        self.txtKodeMK.bind("<Return>", self.onCari)  # Add event for Enter key

        Label(mainFrame, text='Nama MK:').grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.txtNamaMK = Entry(mainFrame)
        self.txtNamaMK.grid(row=1, column=1, padx=5, pady=5)

        Label(mainFrame, text='SKS:').grid(row=2, column=0, sticky='w', padx=5, pady=5)
        self.txtSKS = Entry(mainFrame)
        self.txtSKS.grid(row=2, column=1, padx=5, pady=5)

        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        # Define columns
        columns = ('id', 'kode_mk', 'nama_mk', 'sks')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # Define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('kode_mk', text='Kode MK')
        self.tree.column('kode_mk', width="60")
        self.tree.heading('nama_mk', text='Nama MK')
        self.tree.column('nama_mk', width="200")
        self.tree.heading('sks', text='SKS')
        self.tree.column('sks', width="30")
        # Set tree position
        self.tree.place(x=0, y=200)
        self.onReload()

    def onClear(self, event=None):
        self.txtKodeMK.delete(0, END)
        self.txtKodeMK.insert(END, "")
        self.txtNamaMK.delete(0, END)
        self.txtNamaMK.insert(END, "")
        self.txtSKS.delete(0, END)
        self.txtSKS.insert(END, "")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False

    def onReload(self, event=None):
        # Get data matakuliah
        mk = Matakuliah()
        result = mk.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        courses = []
        for row_data in result:
            courses.append(row_data)

        for course in courses:
            self.tree.insert('', END, values=course)

    def onCari(self, event=None):
        kode_mk = self.txtKodeMK.get()
        mk = Matakuliah()
        res = mk.getByKodeMK(kode_mk)
        rec = mk.affected
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan")
            self.ditemukan = False
            self.txtNamaMK.focus()
        return res

    def TampilkanData(self, event=None):
        kode_mk = self.txtKodeMK.get()
        mk = Matakuliah()
        res = mk.getByKodeMK(kode_mk)
        self.txtNamaMK.delete(0, END)
        self.txtNamaMK.insert(END, mk.nama_mk)
        self.txtSKS.delete(0, END)
        self.txtSKS.insert(END, mk.sks)
        self.btnSimpan.config(text="Update")

    def onSimpan(self, event=None):
        kode_mk = self.txtKodeMK.get()
        nama_mk = self.txtNamaMK.get()
        sks = self.txtSKS.get()

        mk = Matakuliah()
        mk.kode_mk = kode_mk
        mk.nama_mk = nama_mk
        mk.sks = sks
        if self.ditemukan:
            res = mk.updateByKodeMK(kode_mk)
            ket = 'Diperbarui'
        else:
            res = mk.simpan()
            ket = 'Disimpan'

        rec = mk.affected
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Berhasil " + ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal " + ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        kode_mk = self.txtKodeMK.get()
        mk = Matakuliah()
        mk.kode_mk = kode_mk
        if self.ditemukan:
            res = mk.deleteByKodeMK(kode_mk)
            rec = mk.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0

        if rec > 0:
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")

        self.onClear()

    def onKeluar(self, event=None):
        # Command to close the application
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormMatakuliah(root, "Aplikasi Data Matakuliah")
    root.mainloop()
