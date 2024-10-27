try:
    suhu = int(input("masukan suhu anda: "))
    if suhu > 38:
      print("anda deman")
    else:
      print("anda tidak deman:") 
except:
   print("tolong imput angka saja")