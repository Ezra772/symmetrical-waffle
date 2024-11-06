def konversi_suhu(nilai_suhu,satuan_asal):

    if satuan_asal == "C":
        hasil_f = ( nilai_suhu * 9/5) + 32
        hasil_k = nilai_suhu + 273.15
        print (f"F:{hasil_f},K:{hasil_k}")
        return {'F': hasil_f,'K':hasil_k}
    elif satuan_asal == "F":
        hasil_c = (nilai_suhu - 32) * 5/9
        hasil_k = (nilai_suhu - 32 ) * 5/9 + 273.15
        print (f"C:{hasil_c},K:{hasil_k}")
        return {'C': hasil_c,'K':hasil_k}
    elif satuan_asal == "K":
        hasil_c = nilai_suhu - 273.15
        hasil_f = (nilai_suhu -273.15) * 9/5 + 32
        print (f"C:{hasil_c},f:{hasil_f}")
        return {'C': hasil_c,'F':hasil_f}
    else:
        print("satuan tidak dikenal masukkan satuan yang benar")
        return None
        

nilai_suhu = float(input("masukkan suhu: "))
satuan_asal = (input("masukkan satuan asala seperti( (C,K,F) : "))

konversi_suhu(nilai_suhu,satuan_asal)
        