import socket
from time import sleep

pc_name = socket.gethostname()
def welcome_message():
    star = "*" * (len(pc_name) + 6)
    print(star)
    print(f"** {pc_name} **")
    print(star)
    
def exit_program():
    print("program akan dihentikan")
    sleep(1)
    print("3...")
    sleep(1)
    print("2...")
    sleep(1)
    print("1...")
    sleep(1)
    print("program dihentikan ...")
    exit()
    
    
if __name__ == '__main__' :
    welcome_message()
    exit_program()