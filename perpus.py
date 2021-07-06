import os
def layarkosong(msg):
    input(msg)
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def main_menu(x):
    if x == "1":
        readal1()
    elif x ==  "2":
        judul = input("Masukkan Judul Buku : ")
        create(judul)
    elif x == "3":
        judul = input("Masukkan Judul Yang Dicari : ")
        readone(judul)
    elif x == "4":
        judul = input("Masukkan Judul Yang Dicari : ")
        delete(judul)
    elif x == "5":
        print("Program Shutting Down...")
    else:
        print("Option Not Found")

def create(judul):
    buku.append(judul)
    layarkosong("Data berhasil ditambahkan, tekan apa saja untuk melanjutkan...")

def readal1():
    print ("Daftar Buku : ")
    no = 1
    for i in buku:
        print(str(no)+","+i)
        no += 1
    layarkosong("Tekan Apa Saja Untuk Melanjutkan...")

def readone(judul):
    filter_object = filter(lambda a: judul in a, buku)
    p = list(filter_object)
    if(not p):
        layarkosong("Data Tidak Ditemukan, Tekan Apa Saja Untuk Melanjutkan...")
    else:
        layarkosong("Buku Berjudul '"+", ".join(p)+"'berhasil ditemukan.")

def delete(judul):
    if buku.count(judul) >= 1:
        buku.remove(judul)
        layarkosong("Data berhasil dihapus, tekan apa saja untuk melanjutkan...")
    else:
        layarkosong("Buku Tidak ditemukan, harap mengetik secara detail untuk keamanan")

buku = ["Suara Orang Kampung", "Senja Dan Pagi", "Laskar Pelangi", "Dilan 1990", "Dilan 1991","Mati di Jogjakarta"]

x = "0"
while x != "5":
    print("Program Pendataan Inventaris Buku Perpustakaan")
    print("[1] Tampilkan Semua Data Buku")
    print("[2] Tambahkan Data Buku")
    print("[3] Cari Data Buku")
    print("[4] Menghapus Data Buku")
    print("[5] Exit")
    print()

    x = input("Pilihan : ")
    main_menu(x)