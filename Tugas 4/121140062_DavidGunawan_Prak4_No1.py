"""
Tugas 4 No 1
DAVID GUNAWAN/121140062/PBO RB
"""

class komputer:
    def __init__(self,merk,jenis,harga):
        self.merk = merk
        self.jenis = jenis
        self.harga = harga

    def info(self):
        return f"{self.__class__.__name__} {self.jenis} produksi {self.merk}"

class Processor(komputer):
    def __init__ (self,merk,jenis,harga,jumlah_core,kecepatan_prosesor):
        super().__init__(merk,jenis,harga)
        self.core = jumlah_core
        self.kecepatan = kecepatan_prosesor

class RAM(komputer):
    def __init__(self,merk,jenis,harga,kapasitas):
        super().__init__(merk,jenis,harga)
        self.kapasitas = kapasitas

class HDD(komputer):
    def __init__(self,merk,jenis,harga,kapasitas,rpm):
        super().__init__(merk,jenis,harga)
        self.kapasitas = kapasitas
        self.rpm = rpm

class VGA(komputer):
    def __init__(self,merk,jenis,harga,kapasitas):
        super().__init__(merk,jenis,harga)
        self.kapasitas = kapasitas

class PSU(komputer):
    def __init__(self,merk,jenis,harga,daya):
        super().__init__(merk,jenis,harga)
        self.daya = daya



p1 = Processor('Intel','Core i7 7740X',4350000,4,'4.3GHz')
p2 = Processor('AMD','Ryzen 5 3600',250000,4,'4.3GHz')
ram1 = RAM('V-Gen','DDR4 SODimm PC19200/2400MHz',328000,'4GB')
ram2 = RAM('G.SKILL','DDR4 2400MHz',328000,'4GB')
hdd1 = HDD('Seagate','HDD 2.5 inch',295000,'500GB',7200)
hdd2 = HDD('Seagate','HDD 2.5 inch',295000,'1000GB',7200)
vga1 = VGA('Asus','VGA GTX 1050',250000,'2GB')
vga2 = VGA('Asus','1060Ti',250000,'8GB')
psu1 = PSU('Corsair','Corsair V550',250000,'500W')
psu2 = PSU('Corsair','Corsair V550',250000,'500W')


rakit = [[p1,ram1,hdd1,vga1,psu1],[p2,ram2,hdd2,vga2,psu2]]

count = 0
for i in rakit:
    count+=1
    print(f"komputer {count}")
    for j in i:
        print(j.info())
    print()
