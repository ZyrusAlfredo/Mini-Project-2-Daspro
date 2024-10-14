from prettytable import PrettyTable

# Admin (Menu Utama)
def IniAdmin():
    while True:
        tabel_menu = PrettyTable()
        tabel_menu.title = "=== Menu Admin, GoCleaning Zyrus ==="
        tabel_menu.field_names = ["No", "Pilihan Layanan"]
        tabel_menu.add_row(["1", "Melihat Layanan"])
        tabel_menu.add_row(["2", "Menambah Layanan"])
        tabel_menu.add_row(["3", "Mengupdate Layanan"])
        tabel_menu.add_row(["4", "Menghapus Layanan"])
        tabel_menu.add_row(["5", "Keluar"])

        print(tabel_menu)

        pilihan = input("Pilih Layanan: ")

        if pilihan == '1':
            TampilkanLayanan()
        elif pilihan == '2':
            TambahLayanan()
        elif pilihan == '3':
            UpdateLayanan()
        elif pilihan == '4':
            HapusLayanan()
        elif pilihan == '5':
            print("Keluar dari menu admin.")
            login()
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi.")

# Admin (Menampilkan Layanan)
def TampilkanLayanan():
        tabel = PrettyTable()
        tabel.title = "Daftar Layanan GoCleaning Zyrus"
        tabel.field_names = ["ID", "Jenis Layanan"]
        for Layanan in ListLayanan:
            tabel.add_row([Layanan["Id"], Layanan["NamaLayanan"]])
        print(tabel)

# Admin (Menambah Layanan)
def TambahLayanan():
    if ListLayanan:
        NewId = ListLayanan[-1]["Id"] + 1
    else:
        NewId = 1

    while True:
        TambahkanLayananBaru = input("Tambahkan Nama Layanan Yang Baru: ")
        if TambahkanLayananBaru:
            break
        else:
            print("Nama Layanan Tidak Boleh Kosong, Silahkan Coba Lagi")

    layanan_baru = {"Id": NewId, "NamaLayanan": TambahkanLayananBaru}
    ListLayanan.append(layanan_baru)
    
    print(f"Layanan '{TambahkanLayananBaru}' Berhasil Ditambahkan.")

# Admin (Mengupdate Layanan)
def UpdateLayanan():
    TampilkanLayanan()
    try:
        nomor = int(input("Pilih ID Layanan Yang Ingin Diupdate: "))

        LayananTerpilih = None
        for layanan in ListLayanan:
            if layanan["Id"] == nomor:
                LayananTerpilih = layanan
                break
        
        if LayananTerpilih is None:
            print(f"Layanan Dengan ID {nomor} Tidak Ditemukan.")
            return

        NamaBaru = input(f"Masukkan Nama Baru Untuk Layanan '{LayananTerpilih['NamaLayanan']}': ")
        
        if NamaBaru:
            LayananTerpilih['NamaLayanan'] = NamaBaru
            print(f"Nama Layanan Berhasil Diubah Menjadi '{NamaBaru}'.")
        else:
            print("Nama Layanan Tidak Boleh Kosong.")
    
    except ValueError:
        print("Input Harus Berupa Angka.")


# Admin (Menghapus Layanan)
def HapusLayanan():
    TampilkanLayanan()
    try:
        HapusId = int(input("Masukkan ID layanan yang ingin dihapus: "))

        for layanan in ListLayanan:
            if layanan["Id"] == HapusId:
                ListLayanan.remove(layanan)
                print(f"Layanan dengan ID {HapusId} berhasil dihapus")
                
                i = 1
                for layanan in ListLayanan:
                    layanan["Id"] = i
                    i += 1
                break
        else:
            print(f"Layanan dengan ID {HapusId} tidak ditemukan.")
    
    except ValueError:
        print("ID harus berupa angka.")

ListLayanan = [
    {"Id": 1, "NamaLayanan": "Membersihkan AC"},
    {"Id": 2, "NamaLayanan": "Hydro Cleaning"},
    {"Id": 3, "NamaLayanan": "Fogging Disinfektan"}
]
# User
def Layanan():
    print("== Pilihan Layanan Kebersihan ==")
    if not ListLayanan:
        print("Tidak Ada Layanan Yang Tersedia")
    else:
        tabel = PrettyTable()
        tabel.title = "Layanan GoCleaning Zyrus"
        tabel.field_names = ["ID", "Jenis Layanan"]
        for Layanan in ListLayanan:
            tabel.add_row([Layanan["Id"], Layanan["NamaLayanan"]])
        print(tabel)

def Pricelist():
    print("== Pilih Paket Pembersihan ==")
    tabel = PrettyTable()
    tabel.title = "Daftar Paket Pembersihan Berdasarkan Durasi Pengerjaan"
    tabel.field_names = ["No", "Durasi", "Harga"]
    tabel.add_row([1, "2 Jam", "Rp 130.000"])
    tabel.add_row([2, "3 Jam", "Rp 195.000"])
    tabel.add_row([3, "4 Jam", "Rp 260.000"])
    tabel.add_row([4, "5 Jam", "Rp 325.000 (Diskon 5%)"])
    print(tabel)

def DataUser():
    Nama = input("Masukkan Nama Lengkap: ")
    Nomor_HandPhone = input("Masukkan Nomor HandPhone: ")
    Alamat = input("Masukkan Alamat Lengkap: ")
    return Nama, Nomor_HandPhone, Alamat

# Login Admin/user
Akun = {
    "admin": "123",
    "user": "456"
}

def login():
    print("---------------------------------------------------------------------------")    
    print("Selamat Datang! Di Sistem GoCleaning Zyrus, Silahkan Login Terlebih Dahulu")
    print("---------------------------------------------------------------------------")
    while True:
        Username = input("Username: ")
        Password = input("Password: ")
        if Username in Akun and Akun[Username] == Password:
            if Username == "admin":
                print('+' + '-'* 22 + '+')
                print('| Selamat Datang Admin |')
                print('+' + '-'* 22 + '+')
                IniAdmin()
            else:
                print('+' + '-'* 49 + '+')
                print('| Halo, Selamat Datang Di Sistem GoCleaning Zyrus |')
                print('+' + '-'* 49 + '+')
            break
        else:
            print("Username dan Password tidak sesuai, silahkan coba lagi")

# Menampilkan Rincian Pesanan
def RincianPesanan(Nama, Nomor_HandPhone, Alamat, jenis_layanan, LayananPaket, Harga):
    tabel = PrettyTable()
    tabel.title = "Rincian Pesanan Anda"
    tabel.field_names = ["Keterangan", "Detail"]
    tabel.add_row(["Nama Lengkap", Nama])
    tabel.add_row(["Nomor Handphone", Nomor_HandPhone])
    tabel.add_row(["Alamat", Alamat])
    tabel.add_row(["Jenis Layanan", jenis_layanan])
    tabel.add_row(["Durasi Paket", LayananPaket])
    tabel.add_row(["Harga Total", f"Rp. {Harga:,.2f}"])
    print(tabel)

def Utama():
    login()

    while True:
        Layanan()
        Pilih_Layanan = input("Silahkan Memilih Layanan Berdasarkan ID: ")
        
        layanan_terpilih = None
        for layanan in ListLayanan:
            if str(layanan["Id"]) == Pilih_Layanan:
                layanan_terpilih = layanan
                break
        
        if layanan_terpilih is None:
            print("Pilihan Anda Salah, Silahkan Coba Lagi")
            continue
        
        Pricelist()
        Pilih_Paket = input("Silahkan Memilih Daftar Paket Sesuai Kebutuhan Anda: ")
        if Pilih_Paket not in ["1", "2", "3", "4"]:
            print("Pilihan Anda Tidak Ada Di Daftar Paket, Silahkan Coba Lagi")
            continue

        DaftarPaket = {
            "1": "2 Jam",
            "2": "3 Jam",
            "3": "4 Jam",
            "4": "5 Jam (Diskon 5%)"
        }
        LayananPaket = DaftarPaket.get(Pilih_Paket, "Paket Tidak Valid")

        Harga = 0
        if Pilih_Paket == "1":
            Harga = 130000
        elif Pilih_Paket == "2":
            Harga = 195000
        elif Pilih_Paket == "3":
            Harga = 260000
        elif Pilih_Paket == "4":
            Harga = 325000 * 0.95

        Nama, Nomor_HandPhone, Alamat = DataUser()

        RincianPesanan(Nama, Nomor_HandPhone, Alamat, layanan_terpilih["NamaLayanan"], LayananPaket, Harga)

        # Memberikan pilihan Apakah Ingin Menggunakan Program Kembali?
        Pilihan = input("Apakah Anda Ingin Menggunakan Program Ini Kembali? (Ya/Tidak): ")
        if Pilihan.lower() != "ya":
            print("Terimakasih, Have A Nice Day!")
            break

Utama()