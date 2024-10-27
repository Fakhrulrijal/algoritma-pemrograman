try:
    bilangan = int(input("masukan sebuah bilangan"))
    if bilangan > 0:
        print("positif")
    elif bilangan < 0:
        print("negatif")
    else:
        print("nol")   
except:
    print("tolong input angaka saja")           