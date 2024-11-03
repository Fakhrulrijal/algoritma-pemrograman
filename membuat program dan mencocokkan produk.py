def cocokkan_produk(kode1, kode2, kode3):
    digit_terakhir = [kode1 % 10, kode2 % 10, kode3 % 10]
    
    digit_terakhir1 = kode1 % 10
    digit_terakhir2 = kode2 % 10
    digit_terakhir3 = kode3 % 10
    
    return (digit_terakhir1 == digit_terakhir2 ) or (digit_terakhir1 == digit_terakhir3) or (digit_terakhir2 == digit_terakhir3)
    
print(cocokkan_produk(900, 10, 38))  
print(cocokkan_produk(276, 6, 75))   
print(cocokkan_produk(63, 391, 108))  
print(cocokkan_produk(654, 24, 74))  
