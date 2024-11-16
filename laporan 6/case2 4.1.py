print("Selamat datang di kalkulator Deret Pintar!\n\n")
jumlahBilangan = int(input("Masukkan banyak bilangan, kemudian ENTER: \n"))

totalBilangan = 0
rerataBilangan = 0
print("Deret bilangan : ", end="")
# for i in range(1,jumlahBilangan + 1 ,1):
#     if(i==jumlahBilangan):
#         print(f"{i} \n", end="")
#     else:
#         print(f"{i} + ", end="")
#     totalBilangan = totalBilangan + 1

count = 1

while count <= jumlahBilangan:
    totalBilangan += count
    if(count==jumlahBilangan):
        print(f"{count} \n", end="")
        break
    else:
        print(f"{count} + ", end="")
    count += 1
    
print(f"Total seluruh bilangan jika dijumlahkan: {totalBilangan}")
rerataBilangan = totalBilangan/jumlahBilangan
print(f"Rata-ratanya adalah {rerataBilangan}")