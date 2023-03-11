class mahasiswa:
    Jumlah_mahasiswa = 0 #Atribut class
    def __init__ (self,nama, nim, ipk):
        self.nama = nama #Atribut public
        self._nim = nim #Atribut Protected
        self.__ipk = ipk #Atribut Private
        mahasiswa.Jumlah_mahasiswa += 1
    
    def lihat_nama (self): #Metode Public
        print (self.nama)

    def _lihat_nim (self): #Metode Protected
        print (self._nim)

    def __lihat_ipk (self): #Metode Private
        print (self.__ipk)

    def ipk (self): #metode publik yang berisikan pemanggilan metode private
        self.__lihat_ipk()

    def getipk (self): #metode getter untuk mengakses atribut private
        return self.__ipk
    
    def setipk (self, ipk): #metode setter untuk memanipulasi atribut private
        self.__ipk = ipk

    @property #Decorator
    def ipkmod (self): #Getter untuk decorator
        return self.__ipk
    
    @ipkmod.setter #Decorator
    def ipkmod(self, ipk_baru): #Setter untuk decorator
        self.__ipk = ipk_baru

    def jumlahmhs (self):
        print (self.Jumlah_mahasiswa)

class ozt(mahasiswa): #Inheritance atau penurunan class
    def __init__(self,nama,nim,ipk, juara):
        super().__init__(nama,nim,ipk)
        self.ranking = juara
    
    def nim (self):
        return mahasiswa._lihat_nim(self) #Metode Protected dapat diakses oleh class Turunannya
    
    def ipk (self):
        return mahasiswa.__lihat_ipk(self) #Metode Private tidak dapat diakses oleh class turunannya


mhs1 = mahasiswa("David", 121140062, 4)
print ("Output Pemanggilan atribut")
print (mhs1.nama) #Atribut public dapat diakses diluar classnya
print (mhs1._nim) #Atribut Protected dapat diakses diluar classnya
#print (mhs1.__ipk) #sedangkan untuk Atribut Private hanya dapat diakses didalam classnya
#Jika comment pada print ipk dihapus, maka program akan error karna tidak bisa mengakses atribut private

print ("Output pemanggilan atribut Private")
print (mhs1.getipk()) #Atribut Private dapat diakses dengan cara metode getter yaitu mereturn value atribut private
print ()

print ("Output memanipulasi value dari atribut")
mhs1.nama = "Adi" #Atribut Public dapat dimanipulasi diluar classnya
mhs1._nim = 121140040 #Atribut Protected dapat dimanipulasi diluar classnya
mhs1.__ipk = 1 #Atribut private tidak dapat dimanipulasi diluar classnya
mhs1.lihat_nama()
mhs1._lihat_nim()
mhs1.ipk() #ipk pada instance mhs1 tetap 4 karna atribut private tidak dapat diubah diluar classnya

print ("Output memanipulasi value dari atribut private")
mhs1.setipk(2) #Atribut private dapat dimanipulasi nilainya dengan cara getter dan setter
mhs1.ipk()
mhs1.ipkmod = 4 #Atribut private juga dapat dimanipulasi dengan cara decorator
#Decorator mempermudah pemanggilan karna nama fungsi setter dan getternya sama
mhs1.ipk()

print ()
print ("Output pemanggilan metode")
mhs1.lihat_nama() #Metode Public dapat dipanggil di luar classnya
mhs1._lihat_nim() #Metode Protected dapat dipanggil di luar classnya
#mhs1.__lihat_ipk() #Metode Private hanya dapat dipanggil didalam classnya
#Jika comment pada mhs1.__lihat_ipk() dihapus, maka program akan error karna tidak dapat memanggil metode tersebut

print("Output pemanggilan metode private diluar class")
mhs1.ipk() #Metode Private dapat dipanggil diluar class dengan cara membungkusnya dengan metode public
print()

print ("Output pemanggilan atribut class")
mhs2 = mahasiswa ("Bambang", 123123123, 3.6)
print (mhs1.Jumlah_mahasiswa) 
print (mhs2.Jumlah_mahasiswa) #Atribut class bersifat konsisten untuk setiap instance mhs1 maupun mhs2
print ()

print ("Output pemanggilan metode class turunan")
mhs3 = ozt("Budi", 123155732, 4, 1)
mhs3.nim() #Metode nim yang mereturn Metode Protected pada mahasiswa dapat dipanggil
# mhs3.ipk() #metode ipk yang mereturn Metode Private pada mahasiswa tidak dapat dipanggil karna akan terjadi error
