import main
from services import db


# Tambah barang
def add():
    kode_barang = input("Kode barang: ") 
    nama_barang = input("Nama Barang: ")
    harga_barang = int(input("Harga Barang: ")) 
    stok_barang = int(input("Stok Barang: "))
    
    db.insert_items(kode_barang, nama_barang, harga_barang, stok_barang)
    
# Menampilkan barang
def check():
    print("*** List barang start***")
    db.fetch_item()
    print("*** List barang end ***")
    
# Update Barang berdasarkan kode_barang
def update():
    kode_barang = input("Kode barang yang ingin di ubah: ") 
    nama_barang = input("Nama Barang: ")
    harga_barang = int(input("Harga Barang: ")) 
    stok_barang = int(input("Stok Barang: "))
    db.update_item(nama_barang, harga_barang, stok_barang,kode_barang)
    
# Delete
def delete():
    kode_barang = input("masukkan kode barang yang ingin dihapus: ")
    db.delete_item(kode_barang)
    
def start():
    while True:
        menu = int(input("Menu:\n1.Tambah Barang\n2.check\n3.Update Barang\n4,Hapus barang\n5.keluar\n\nMasukkan Pilihan anda: "))
        
        if menu == 1:
            add()
        elif menu == 2:
            check()
        elif menu == 3:
            update()
        elif menu == 4:
            delete()
        elif menu == 5:
            main.menu()
        
        
if __name__ == "__main__" :
    start()