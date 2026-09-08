daftar_buku = (
    "Tentang kamu","Pulang","Hujan","Bumi","Negeri para bedebah"
)

pinjaman = []

print("Perpustakaan Azis")
print("Daftar buku:")

for buku in daftar_buku:
    print("-", buku)

while True:
    print("\nMenu:")
    print("1. Pinjam buku")
    print("2. Hapus pinjaman")
    print("3. Lihat daftar pinjaman")
    print("4. Selesai")
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        buku = input("Masukkan judul buku yang ingin dipinjam: ")

        if buku in daftar_buku:
            pinjaman.append(buku)
            print("buku berhasil dipinjam")
        else:
            print("Buku tidak tersedia di perpustakaan")

    elif pilihan == "2":
        buku = input("Masukkan judul buku yang ingin dihapus: ")

        if buku in pinjaman:
            pinjaman.remove(buku)
            print("Buku berhasil dihapus dari pinjaman")
        else:
            print("Buku tidak ada dalam daftar pinjaman")

    elif pilihan == "3":
        print("\nbuku yang dipinjam:")
        for buku in pinjaman:
            print("-", buku)

    elif pilihan == "4":
        print("Terima kasih telah menggunakan layanan perpustakaan")
        break

    else:
        print("pilhan tidak valid")

print("\nbuku yang dipinjam:")

if len(pinjaman) == 0:
    print("Tidak ada buku yang dipinjam")
else:
    for buku in pinjaman:
        print("-", buku)

