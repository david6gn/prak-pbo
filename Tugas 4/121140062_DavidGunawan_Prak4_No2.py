"""
Tugas 4 No 2
DAVID GUNAWAN/121140062/PBO RB
"""

class Robot:
    jumlah_turn = 0
    def __init__(self, health, damage,buff):
        self.nama = type(self).__name__
        self.health = health
        self.damage = damage
        self.buff = buff

    def skill(self):
        pass

    def lakukan_aksi(self):
        if self.jumlah_turn != 0 and self.jumlah_turn % self.buff == 0:
            attack = self.skill()
            print (f"menyerang sebanyak {round(attack)} DMG ")
            return attack
        else:
            print (f"menyerang sebanyak {self.damage} DMG ")
            return self.damage

    def terima_aksi(self,damage):
        self.health-=damage

class Antares(Robot):
    def __init__(self, health = 50000, damage = 5000,buff = 3):
        super().__init__(health, damage,buff)

    def skill(self):
        print ("Menambah damage menjadi 1.5x dan ", end='')
        return self.damage*1.5
        
class Alphasetia(Robot):
    def __init__(self, health = 40000, damage = 6000,buff = 2):
        super().__init__(health, damage,buff)

    def skill(self):
        print ("Menambah darah sebanyak 4000 HP ",end='')
        self.health+=4000
        return self.damage

class Lecalicus(Robot):
    def __init__(self, health = 45000, damage = 5500, buff = 4):
        super().__init__(health, damage,buff)

    def skill(self):
        self.health+=7000
        print ("Menambah darah sebanyak 7000 HP dan menambah damage menjadi 2x dan ",end='')
        return self.damage*2
        

print ("Selamat datang di pertandingan robot Yamako")
m1 = int(input("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): "))
m2 = int(input("Pilih robot lawan (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): "))

if m1 == 1:
    player = Antares()
elif m1 == 2:
    player = Alphasetia()
elif m1 == 3:
    player = Lecalicus()
else:
    pass

if m2 == 1:
    enemy = Antares()
elif m2 == 2:
    enemy = Alphasetia()
elif m2 == 3:
    enemy = Lecalicus()
else:
    pass

print ("Selanjutnya, pilih 1 untuk batu, 2 untuk kertas, dan 3 untuk gunting")

menang = False
print()
while True:
    aksiplayer = 0
    Robot.jumlah_turn+=1
    print (f"Turn saat ini : {Robot.jumlah_turn}")
    print (f"Robotmu ({player.nama} - {round(player.health)}), robot lawan ({enemy.nama} - {round(enemy.health)})")
    opsi_p = int(input(f"Pilih tangan robotmu ({player.nama}): "))
    opsi_e = int(input(f"Pilih tangan robot lawan ({enemy.nama}): "))
    
    if opsi_p == 1 and opsi_e == 1:
        print ("Draw")
        aksiplayer = 3
    elif opsi_p == 2 and opsi_e == 2:
        print ("Draw")
        aksiplayer = 3
    elif opsi_p == 3 and opsi_e == 3:
        print ("Draw")
        aksiplayer = 3
    elif opsi_p == 1 and opsi_e == 2:
        pass
    elif opsi_p == 1 and opsi_e == 3:
        aksiplayer = 1
    elif opsi_p == 2 and opsi_e == 1:
        aksiplayer = 1
    elif opsi_p == 2 and opsi_e == 3:
        pass
    elif opsi_p == 3 and opsi_e == 1:
        pass
    elif opsi_p == 3 and opsi_e == 2:
        aksiplayer = 1
    else:
        print ("Terdapat kesalahan input, coba lagi")
        Robot.jumlah_turn-=1
        aksiplayer = 3
        
    if aksiplayer == 1:
        print (f"Robotmu ({player.nama}) ",end='')    
        enemy.terima_aksi(player.lakukan_aksi())
    elif aksiplayer == 0:
        print (f"Robot lawan ({enemy.nama}) ",end='')    
        player.terima_aksi(enemy.lakukan_aksi())
    else:
        pass

    if player.health<0:
        break
    elif enemy.health<0:
        menang = True
        break
    else:
        pass
    print()

print()
print("Permainan Berakhir")
if menang == True:
    print (f"Robot anda ({player.nama}) menang melawan robot lawan ({enemy.nama})")
elif menang == False:
    print (f"Robot anda ({player.nama}) kalah melawan robot lawan ({enemy.nama})")
        

    
    





