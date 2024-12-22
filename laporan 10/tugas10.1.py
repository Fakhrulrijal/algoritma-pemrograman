kamus = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("key/tvalue/titem")
for i, (key, value) in enumerate(kamus.items(),start=1):
    print(f"{key}\t{value}\t{i}")