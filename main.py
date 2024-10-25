import random

from libs import welcome_message

cuypy_position = random.randint(1,4)




bentuk_goa = "|_|"
goa = [bentuk_goa] * 4
isi_goa = goa.copy()
isi_goa[cuypy_position - 1] = "|0_0|"

welcome_message("Selamat datang di Cuypy games")


name_user = input("masukan nama kamu:")
while name_user == "":
    name_user = input("masukan nama kamu terlebih dahulu: ")
while True :    
    print(f"hai {name_user}, selamat datang di CUYPY game \n Perhatikan goa dibawah ini \n {''.join(goa)}  \n 1/2/3/4")

    pilihan_user = input("Menurut kamu digoa Nomor berapakah CUYPY berada ?: ")
    no_goa = ["1","2","3","4"]
    while pilihan_user == "":
            pilihan_user = input("\n Pilihan tidak boleh kosong : ")
    while pilihan_user not in no_goa :
            pilihan_user = input("\n pilih goa 1/2/3/4 : ")

        
    konfirmasi_user = input("\n apakah kamu yakin ? [y/n] :")
    ask = ["y","n"]
    while  konfirmasi_user not in ask :
        konfirmasi_user = input("\n apakah kamu yakin ? [y/n] :")

        
    if konfirmasi_user == "y":
        if int(pilihan_user) == cuypy_position:
            print(f"\n Selamat {name_user} kamu menang !!, CUYPY berada di goa {''.join(isi_goa)}")
        else:
            print(f"\n yah,,, jawaban mu salah, CUYPY ada di goa {''.join(isi_goa)}")
    elif konfirmasi_user == "n":
        print('program berhenti')
        exit()
    else:
        exit()
        
    lanjut = input("\n \n  apakah kamu ingin lanjut main ? [y/n]:")
    if lanjut == "n" :
        print(" \n \n terimakasih")
        break