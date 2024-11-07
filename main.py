from libs import welcome_message, exit_program
from games import cuypy
from tools import warung
import sys


def menu(): 
    while True:
        pilihan_user= int(input("Menu Program:\n1. Games Cuypy\n2. Warung mini\n3. Tutup Program \n\nSilahkan Pilih program:"))
        
        if pilihan_user == 1:
            cuypy.start()
        elif pilihan_user == 2:
            warung.start()
        elif pilihan_user == 3:
            exit_program()
            break
        else:
            print("hanya boleh memilih yang ada di list")


def main():
    welcome_message()
    menu()


if __name__ == '__main__' :
    main()