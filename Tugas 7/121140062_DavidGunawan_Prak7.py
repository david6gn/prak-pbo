import tkinter as tk

class KotakTicTacToe:
    def __init__(self):
        self.pemain_saat_ini = "X"
        self.papan = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.jendela = tk.Tk()
        self.jendela.title("Tic Tac Toe")

        self.daftar_tombol = []
        for i in range(3):
            tombol_baris = []
            for j in range(3):
                tombol = tk.Button(self.jendela, text="", font=("Helvetica", 20), width=5, height=2, command=lambda baris=i, kolom=j: self.tombol_klik(baris, kolom))
                tombol.grid(row=i, column=j)
                tombol_baris.append(tombol)
            self.daftar_tombol.append(tombol_baris)

        self.label = tk.Label(self.jendela, text=f"Pemain Saat Ini: {self.pemain_saat_ini}", font=("Helvetica", 14))
        self.label.grid(row=3, columnspan=3)

        self.tombol_reset = tk.Button(self.jendela, text="Reset", font=("Helvetica", 14), command=self.reset)
        self.tombol_reset.grid(row=4, columnspan=3)

        self.start = len(self.daftar_tombol)

        self.jendela.mainloop()

    def tombol_klik(self, baris, kolom):
        if self.papan[baris][kolom] == "":
            self.papan[baris][kolom] = self.pemain_saat_ini
            self.daftar_tombol[baris][kolom].configure(text=self.pemain_saat_ini)
            if self.pemain_saat_ini == "X":
                self.pemain_saat_ini = "O"
            else:
                self.pemain_saat_ini = "X"
            self.label.configure(text=f"Pemain Saat Ini: {self.pemain_saat_ini}")
            pemenang = self.periksa_pemenang()
            if pemenang is not None:
                self.label.configure(text=f"Pemenang: {pemenang}")
                for i in range(3):
                    for j in range(3):
                        self.daftar_tombol[i][j].configure(state="disabled")
        else:
            raise ValueError("Index sudah terisi")
        

    def periksa_pemenang(self):
        for i in range(3):
            if self.papan[i][0] == self.papan[i][1] == self.papan[i][2] != "":
                return self.papan[i][0]
        for j in range(3):
            if self.papan[0][j] == self.papan[1][j] == self.papan[2][j] != "":
                return self.papan[0][j]
        if self.papan[0][0] == self.papan[1][1] == self.papan[2][2] != "":
            return self.papan[0][0]
        if self.papan[0][2] == self.papan[1][1] == self.papan[2][0] != "":
            return self.papan[0][2]

    def reset(self):
        try:
            self.pemain_saat_ini = "X"
            self.papan = [["", "", ""], ["", "", ""], ["", "", ""]]
            for i in range(3):
                for j in range(3):
                    self.daftar_tombol[i][j].configure(text="", state="normal")
        except:
            print("aaa")

if __name__ == "__main__":
    game = KotakTicTacToe()