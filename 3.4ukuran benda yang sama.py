try:
    # Meminta input ukuran dari tiga benda
    ukuran1 = float(input("Masukkan ukuran benda 1: "))
    ukuran2 = float(input("Masukkan ukuran benda 2: "))
    ukuran3 = float(input("Masukkan ukuran benda 3: "))
    # Menentukan apakah ada benda yang sama
    if ukuran1 == ukuran2 == ukuran3:
        print("3 benda sama")
    elif ukuran1 == ukuran2 or ukuran1 == ukuran3 or ukuran2 == ukuran3:
        print("2 benda sama")
    else:
        print("Tidak ada yang sama")
except:
    print("masukan angka")