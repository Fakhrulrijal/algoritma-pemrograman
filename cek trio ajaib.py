def cek_trio_ajaib(a, b, c,):
    return (a + b == c) or (a + c == b) or ( b + c == a)

print(cek_trio_ajaib(6, 5, 4))
print(cek_trio_ajaib(5, 3, 8))
print(cek_trio_ajaib(2, 5, 7))