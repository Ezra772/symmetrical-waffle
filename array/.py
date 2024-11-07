array = []

jumlah_elemen = int(input("masukkan jumlah elemennya: "))

for i in range (jumlah_elemen):
    elemen = int(input(f"masukkan angka ke {i + 1}: "))
    array.append(elemen)
    
angka_terkecil = min(array)
angka_terbesar = max(array)

print ("angka terkceilnya adalah : ", angka_terkecil)
print ("angka terbesarnya adalah : ", angka_terbesar)