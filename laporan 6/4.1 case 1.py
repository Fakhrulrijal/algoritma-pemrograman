jmlPisangGoreng = int(input("Banyak pisang goreng yang ingin dihitung: \n"))
hargaSatuan = int(input("Harga perbiji: \n"))
print("Daftar harga pisang goreng:")

# for i in range(1,jmlPisangGoreng + 1, 1):
    # print(f"{i} pisang goreng : \t Rp {i* hargaSatuan}")
    
count = 1
while count < jmlPisangGoreng + 1:
    print(f"{count} pisang goreng : \t Rp {count * hargaSatuan}")
    count += 1