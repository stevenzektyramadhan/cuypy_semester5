import random
import main
def start():
    while True :    
        bentuk_goa = "|_|"
        goa = [bentuk_goa] * 4
        isi_goa = goa.copy()
        cuypy_position = random.randint(1,4)
        isi_goa[cuypy_position - 1] = "|0_0|"
        print(f"Selamat datang di CUYPY game \n Perhatikan goa dibawah ini \n {''.join(goa)}  \n 1/2/3/4")
        # Pilihan user
        pilihan_user = input("Menurut kamu digoa Nomor berapakah CUYPY berada ?: ")
        no_goa = ["1","2","3","4"]
        while pilihan_user == "":
                pilihan_user = input("\n Pilihan tidak boleh kosong : ")
        while pilihan_user not in no_goa :
                pilihan_user = input("\n pilih goa 1/2/3/4 : ")

        # Mengecek jawaban User
        if int(pilihan_user) == cuypy_position:
                print(f"\n Selamat kamu menang ")
        else:
                print(f"\n yah,,, jawaban mu salah ")
        #  Apakah user pengen lanjut atau tidak
        lanjut = input("\n \napakah kamu ingin lanjut main ? [y/n]:")
        if lanjut == "n" :
                main.menu()
            
        
    
if __name__ == "__main__" :
    start()