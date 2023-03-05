class mhs:
    def __init__(self,nama,nim,kelamin,umur, kelas,sks):
        self.Nama = nama
        self.Nim = nim
        self.Kelamin = kelamin
        self.Umur = umur
        self.Kelas = kelas
        self.Sks = sks
    
    def print (self):
        print (f"Nama    : {self.Nama}")
        print (f"NIM     : {self.Nim}")
        print (f"Kelamin : {self.Kelamin}")
        print (f"Umur    : {self.Umur}")
        print (f"Kelas   : {self.Kelas}")
        print (f"SKS     : {self.Sks}")


Nama = input("Masukan Nama : ")
Nim = input("Masukan NIM : ")
Kelamin = input ("Masukan Kelamin : ")
Umur = input ("Masukan Umur : ")
Kelas = input ("Masukan Kelas : ")
Sks = input ("Masukan Jumlah SKS : ")

mahasiswa = mhs(Nama,Nim,Kelamin,Umur,Kelas,Sks)

mahasiswa.print()
    