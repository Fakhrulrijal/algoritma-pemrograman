teks_berita = "pukul 8 telah terjadi gempa bumi berkekuatan 4,5 maknitudo dan gempa bumi susulan sekitar jam 2"
kata_kunci = "gempa bumi"
jumlah = teks_berita.lower().count(kata_kunci.lower())

print(f"Kata '{kata_kunci}' muncul sebanyak {jumlah} kali dalam teks berita.")