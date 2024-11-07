import main
def start():
    while True:
        print("Selamat datang di Warung mini")
        ask = input("apakah kamu ingin melanjutkan program ? [y/n]: ")
        if ask == "n":
            main.menu()
        
        
if __name__ == "__main__" :
    start()