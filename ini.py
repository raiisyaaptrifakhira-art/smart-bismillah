# Program Simulasi Smart Door Lock dengan Autentikasi Awal

pin_benar = "1234"
status_pintu = "Terkunci"
maks_percobaan = 3
sisa_percobaan = maks_percobaan
is_authenticated = False

print("="*35)
print("   SILAKAN MASUKKAN PIN TERLEBIH DAHULU   ")
print("="*35)

# 7. Minimal satu penggunaan for (atau perulangan untuk batas percobaan PIN di awal)
for percobaan in range(maks_percobaan):
    pin_input = input(f"Masukkan 4 digit PIN (Sisa percobaan {maks_percobaan - percobaan}): ")
    
    # 6. Operator perbandingan & 4. Percabangan if-else
    if pin_input == pin_benar:
        print("✔ PIN Benar! Akses diberikan.")
        is_authenticated = True
        status_pintu = "Siap Dibuka"
        break
    else:
        print("❌ PIN Salah!")
        sisa_percobaan -= 1 # 6. Operator aritmatika

# Cek apakah pengguna gagal setelah 3 kali percobaan
if not is_authenticated:
    print("\n⚠ Terlalu banyak salah memasukkan PIN. Sistem terkunci!")
else:
    # 2. Perulangan while agar menu dapat digunakan berulang setelah PIN benar
    while True:
        # 9. Tampilan program yang rapi
        print("\n" + "="*35)
        print("       APLIKASI SMART DOOR LOCK      ")
        print("="*35)
        print("1. Buka Pintu")
        print("2. Kunci Pintu")
        print("3. Batas Percobaan PIN")
        print("4. Exit")
        print("="*35)
# 5. Input dari pengguna
        pilihan = input("Pilih menu (1-4): ")
        
# 4. Minimal 3 percabangan if-elif-else121
        if pilihan == '1':
            print("\n--- Buka Pintu ---")
            if status_pintu == "Siap Dibuka" or status_pintu == "Terbuka":
                print("🚪 Pintu berhasil dibuka! Selamat datang.")
                status_pintu = "Terbuka"
            else:
                print("🔒 Pintu sudah dalam posisi terkunci.")
                
        elif pilihan == '2':
            print("\n--- Kunci Pintu ---")
            status_pintu = "Terkunci"
            print("🔒 Pintu telah dikunci kembali dengan aman.")
            
        elif pilihan == '3':
            print("\n--- Batas Percobaan PIN ---")
            print(f"Status Autentikasi : Berhasil")
            print(f"Status Pintu       : {status_pintu}")
            
        elif pilihan == '4':
            # 3. Tombol Exit menggunakan break
            print("\nTerima kasih telah menggunakan Smart Door Lock. Program dihentikan.")
            break 
            
        else:
            # 8. Validasi input sederhana
            print("\n⚠ Pilihan tidak valid! Harap masukkan angka antara 1 sampai 4.")