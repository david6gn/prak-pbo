"""
LATIHAN MODUL 6
DAVID GUNAWAN/121140062/PBO RB
"""

from abc import ABC, abstractmethod

class AkunBank(ABC):
    def __init__(self, nama, tahun, saldo):
        self.nama = nama
        self.tahun = tahun
        self.saldo = saldo

    def lihat_saldo(self):
        print(f"Saldo anda : {self.saldo}")

    @abstractmethod
    def transfer_saldo(self,tf):
        pass

    @abstractmethod
    def lihat_bunga(self):
        pass

class AkunGold(AkunBank):
    def __init__(self, nama, tahun, saldo):
        super().__init__(nama, tahun, saldo)
        self.umur = 2023-self.tahun
    
    def transfer_saldo(self,tf):
        if self.umur >=3 and tf>=100000:
            print(f"Transfer Berhasil sebanyak {tf} dan biaya adminnya Rp.0")
        elif self.umur<3 and tf>100000:
            print(f"Transfer Berhasil sebanyak {tf} dan biaya adminnya Rp.2000")
            tf+=2000
        else:
            print(f"Transfer Berhasil sebanyak {tf} dan biaya adminnya Rp.0")
        self.saldo-=tf

    def lihat_bunga(self):
        if self.umur>=3 and self.saldo>=1000000000:
            print("Bunga Bulanan anda adalah 1%")
        elif self.umur<3 and self.saldo>=1000000000:
            print("Bunga Bulanan anda adalah 2%")
        else:
            print("Bunga Bulanan anda adalah 3%")

class AkunSilver(AkunBank):
    def __init__(self, nama, tahun, saldo):
        super().__init__(nama, tahun, saldo)
        self.umur = 2023-self.tahun
    

    def transfer_saldo(self,tf):
        if self.umur >=3 and tf>=100000:
            print(f"Transfer Berhasil sebanyak {tf} dan biaya adminnya Rp.2000")
            tf+=2000
        elif self.umur<3 and tf>100000:
            print(f"Transfer Berhasil sebanyak {tf} dan biaya adminnya Rp.5000")
            tf+=5000
        else:
            print(f"Transfer Berhasil sebanyak {tf} dan biaya adminnya Rp.0")
        self.saldo-=tf


    def lihat_bunga(self):
        if self.umur>=3 and self.saldo>=10000000:
            print("Bunga Bulanan anda adalah 1%")
        elif self.umur<3 and self.saldo>=10000000:
            print("Bunga Bulanan anda adalah 2%")
        else:
            print("Bunga Bulanan anda adalah 3%")
        

#Contoh Implementasi
p1 = AkunSilver("Budi", 2021, 2000000)
p1.lihat_saldo()
p1.lihat_bunga()
p1.transfer_saldo(150000)
p1.lihat_saldo()