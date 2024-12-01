def cek_anagram(kata1, kata2):
    kata1 = kata1.replace(" ", "").lower()
    kata2 = kata2.replace(" ", "").lower()
    return (kata1) == (kata2)

kata1 = input("masukan kata1 pertama: ")
kata2 = input("maskan kata kedua: ")

if cek_anagram(kata1, kata2):
    print("kata1 dan kata2 adalah anagram")
else:
    print("kata 1 dana kata 2 bukan anagram")