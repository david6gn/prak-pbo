class AkunBank:
    list_pelanggan = []
    def __init__ (self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.NoPelanggan = no_pelanggan
        self.NamaPelanggan = nama_pelanggan
        self.__JumlahSaldo = jumlah_saldo
    
    def lihat_menu(self):
        while True:
            print ("Selamat datang di Bank Jago")
            print (f"Halo {self.NamaPelanggan}, ingin melakukan apa?")
            print ("1. Lihat Saldo")
            print ("2. Tarik Tunai")
            print ("3. Transfer Saldo")
            print ("4. Keluar")
            menu = input ("Masukan Pilihan (1-4) : ")
            if (menu == '1'):
                self.lihat_saldo()
            elif(menu == '2'):
                self.tarik_tunai()
            elif(menu == '3'):
                self.transfer()
            elif(menu == '4'):
                break
            else:
                print ("Input Salah!")

    def lihat_saldo(self):
        print (f"Jumlah saldo anda : {self.__JumlahSaldo}")
        print()

    def tarik_tunai(self):
        while True:
            jumlahtarik = int(input("Masukan Jumlah yang ingin ditarik : "))
            if (self.__JumlahSaldo-jumlahtarik < 0):
                print ("Saldo anda tidak mencukupi untuk ditarik!")
                print()
            else:
                self.__JumlahSaldo-= jumlahtarik
                print ("Saldo berhasil Ditarik!")
                print()
                break

    def transfer (self):
        ketemu = False
        while ketemu == False:
            target = int(input("Masukan nomor pelanggan yang ingin ditransfer : "))
            for nopel in self.list_pelanggan:
                if (nopel.NoPelanggan == target):
                    ketemu = True
                    break
            if (ketemu == False):
                print ("No Pelanggan Tidak Ditemukan!")
        while True:
            tf = int(input("Masukan Jumlah yang ingin ditransfer : "))
            if (self.__JumlahSaldo < tf):
                print ("Saldo Tidak Mencukupi Untuk Melakukan Transfer")
            else:
                nopel.__JumlahSaldo += tf
                self.__JumlahSaldo -= tf
                print ("Transfer Berhasil!")
                print()
                break
    

bank1 = AkunBank(1234,"David", 5000000)
bank2 = AkunBank(2345, "Ukraina", 6666666666)
bank3 = AkunBank(3456, "Elon Musk", 9999999999)

AkunBank.list_pelanggan = [bank1,bank2,bank3]

bank1.lihat_menu()
        