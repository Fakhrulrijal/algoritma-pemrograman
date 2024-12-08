import os

def compare_files(file1, file2):
    if not os.path.exists(file1) or not os.path.exists(file2):
        print("Salah satu atau kedua file tidak ditemukan.")
        return

    
    def count_lines(file):
        with open(file, 'r', encoding='utf-8') as f:
            return sum(1 for _ in f)

    
    def get_file_size(file):
        return os.path.getsize(file)

    
    lines1 = count_lines(file1)
    lines2 = count_lines(file2)
    size1 = get_file_size(file1)
    size2 = get_file_size(file2)

    # Menampilkan hasil perbandingan
    print(f"File 1: {file1}")
    print(f"  - Jumlah baris : {lines1}")
    print(f"  - Ukuran (byte): {size1}")
    print()
    print(f"File 2: {file2}")
    print(f"  - Jumlah baris : {lines2}")
    print(f"  - Ukuran (byte): {size2}")
    print()
    
    if lines1 > lines2:
        print(f"File '{file1}' memiliki lebih banyak baris ({lines1} vs {lines2}).")
    elif lines1 < lines2:
        print(f"File '{file2}' memiliki lebih banyak baris ({lines2} vs {lines1}).")
    else:
        print(f"Kedua file memiliki jumlah baris yang sama ({lines1}).")

    if size1 > size2:
        print(f"File '{file1}' lebih besar ukurannya ({size1} byte vs {size2} byte).")
    elif size1 < size2:
        print(f"File '{file2}' lebih besar ukurannya ({size2} byte vs {size1} byte).")
    else:
        print(f"Kedua file memiliki ukuran yang sama ({size1} byte).")

file1 = input("Masukkan path file pertama: ")
file2 = input("Masukkan path file kedua: ")
compare_files(file1, file2)
