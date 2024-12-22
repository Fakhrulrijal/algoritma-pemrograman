def buat_dictionary_warna(nama_warna, kode_hex):
    """
    Membuat dictionary dari dua list: nama warna dan kode hex.
    
    Args:
        nama_warna (list): List berisi nama warna.
        kode_hex (list): List berisi kode hex warna.
    
    Returns:
        dict: Dictionary di mana nama warna menjadi key dan kode hex menjadi value.
    """
    if len(nama_warna) != len(kode_hex):
        raise ValueError("Panjang kedua list harus sama.")
    
    return dict(zip(nama_warna, kode_hex))

# Contoh penggunaan
nama_warna = ["Merah", "Hijau", "Biru"]
kode_hex = ["#FF0000", "#008000", "#0000FF"]

hasil = buat_dictionary_warna(nama_warna, kode_hex)
print(hasil)
