bulan = int(input("Masukkan nomor bulan (1-12): "))
    
try :
    if bulan < 1 or bulan > 12:
        print("Bulan yang diinputkan tidak valid. Harus antara 1 dan 12.")
    
    # Jumlah hari dalam setiap bulan
    if bulan == 1:   # Januari
        jumlah_hari = 31
    elif bulan == 2: # Februari
        jumlah_hari = 28  # Untuk kesederhanaan, tidak menghitung tahun kabisat
    elif bulan == 3: # Maret
        jumlah_hari = 31
    elif bulan == 4: # April
        jumlah_hari = 30
    elif bulan == 5: # Mei
        jumlah_hari = 31
    elif bulan == 6: # Juni
        jumlah_hari = 30
    elif bulan == 7: # Juli
        jumlah_hari = 31
    elif bulan == 8: # Agustus
        jumlah_hari = 31
    elif bulan == 9: # September
        jumlah_hari = 30
    elif bulan == 10: # Oktober
        jumlah_hari = 31
    elif bulan == 11: # November
        jumlah_hari = 30
    elif bulan == 12: # Desember
        jumlah_hari = 31
    
    print("jumlah hari = ", jumlah_hari)

except :
    print("masukkan keyword dengan benar")