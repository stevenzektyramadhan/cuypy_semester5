import mysql.connector

#  koneksi ke database
db = mysql.connector.connect(
    host = "localhost",
    user= "root",
    password="",
    database="mini_market"
)

# insert Data
def insert_items(kode_barang, nama_barang, harga_barang, stok_barang) :
    cursor = db.cursor()
    cursor.execute("INSERT INTO tbl_barang (kode_barang, nama_barang, harga_barang, stok_barang) VALUES (%s, %s, %s, %s)", (kode_barang, nama_barang, harga_barang, stok_barang))
    db.commit()

    if cursor.rowcount > 0 :
        return print("\n\nData berhasil ditambah\n\n")
    else:
        return print("\n\nData gagal ditambah\n\n")
    
    # Menampilkan Data 
def fetch_item():
    cursor = db.cursor()
    cursor.execute("select * from tbl_barang")
    items = cursor.fetchall()
    
    for item in items:
        print(f'''
Kode: {item[1]}
{item[2]} | Rp{item[3]}
stok: {item[4]}
              ''')
        
# update data
def update_item(nama_barang, harga_barang, stok_barang, kode_barang):
    cursor = db.cursor()
    sql = "update tbl_barang set nama_barang=%s, harga_barang=%s, stok_barang=%s where kode_barang = %s"
    cursor.execute(sql,(nama_barang, harga_barang, stok_barang, kode_barang))
    db.commit()
    if cursor.rowcount > 0:
         return print("\n\nData berhasil diupdate\n\n")
    else:
        return print("\n\nData gagal diupdate\n\n")
    
# Hapus data
def delete_item(kode_barang):
    cursor = db.cursor()
    sql = "delete from tbl_barang where kode_barang=%s"
    cursor.execute(sql,(kode_barang,))
    db.commit()
    if cursor.rowcount > 0:
         return print("\n\nData berhasil di hapus\n\n")
    else:
        return print("\n\nData gagal di hapus\n\n")