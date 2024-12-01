kalimat = input("Masukkan sebuah kalimat: ")
kata_kata = kalimat.split()

kata_terpendek = min(kata_kata, key=len)
kata_terpanjang = max(kata_kata, key=len)

print(f"Kata terpendek: {kata_terpendek}")
print(f"Kata terpanjang: {kata_terpanjang}")