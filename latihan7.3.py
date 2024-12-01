def hapus_spasi_ganda(teks):
    return ' '.join(teks.split())
teks = "dingin    tetapi     tidak     kejam."
print(hapus_spasi_ganda(teks))