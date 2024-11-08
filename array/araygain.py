
baris = int(input("masukkan jumlah baris: "))
kolom = int(input("masukkan jumlah kolom: "))

arr_1 = []
arr_2 = []
hasil_arr = []

print("masukkan angka untuk array 1")
for i in range (baris):
    baris_arr_1 = []
    for j in range (kolom):
        angka = int(input(f"masukkan angka [{i + 1}][{j + 1}]"))
        baris_arr_1.append(angka)
    arr_1.append(baris_arr_1)
    
    

print (f"array 1: {arr_1}")


print("masukkan angka untuk array ke 2")
for i in range (baris):
    baris_arr_2 = []
    for j in range (kolom):
        angka_2 = int(input(f"masukkan angka [{i + 1}][{j + 1}]"))
        baris_arr_2.append(angka_2)
    arr_2.append(baris_arr_2)
        
print (f"array 1: {arr_2}")

for i in range (baris):
    hasil_hasil_arr = []
    for j in range (kolom):
        hasil = arr_1 [i][j] + arr_2 [i][j]
        hasil_hasil_arr.append(hasil)
    hasil_arr.append(hasil_hasil_arr)
    
        
print (f"hasil penjumlahan array nya adalah: {hasil_arr}")

