def main():
    produk_harga = []  # Menyimpan harga-harga produk yang dimasukkan oleh admin
    
    while True:
        try:
            # Meminta input harga produk dari admin
            harga = input("Masukkan harga produk (ketik 'stop' untuk berhenti): ")
            
            if harga.lower() == 'stop':
                break  # Keluar dari loop jika admin mengetik 'stop'
            
            # Mengonversi harga yang dimasukkan ke tipe data float
            harga = float(harga)
            
            # Memastikan harga produk lebih besar dari 0
            if harga <= 0:
                print("Harga produk harus lebih besar dari 0. Coba lagi.")
                continue
            
            # Menambahkan harga ke list produk_harga
            produk_harga.append(harga)
        
        except ValueError:
            # Menangani jika input tidak dapat diubah menjadi angka
            print("Input tidak valid. Harap masukkan angka yang valid.")
    
    # Menampilkan harga produk termahal dan termurah
    if produk_harga:
        harga_termahal = max(produk_harga)
        harga_termurah = min(produk_harga)
        print(f"Harga produk termahal: Rp {harga_termahal}")
        print(f"Harga produk termurah: Rp {harga_termurah}")
    else:
        print("Tidak ada harga produk yang dimasukkan.")

if __name__ == "__main__":
    main()
