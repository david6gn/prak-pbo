username = "informatika"
password = "12345678"

for i in range (3):
    name = input ("Username anda : ")
    pw = input ("Password anda : ")
    if (name == username and pw == password):
        print ("Berhasil Login!")
        break
    else:
        print ("Username atau password salah coba lagi")

if (i == 2):
    print ("Akun anda diblokir")