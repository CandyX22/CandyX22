#CANDY SOEKA WIYONO_064002200012
#Program untuk menghitung Tiket Masuk Kebun Binatang Berdasarkan Umur beserta Pembayarannya dengan aturan 
umur = "0"
total = 0
while (umur != ""):
    umur = input("Masukkan Umur = ")
    if umur != '':
        umur_angka = int(umur)
        if umur_angka <= 2:
            print("Gratis!!")
            price = 0
        elif umur_angka >= 3 and umur_angka <= 12:
            print("Harga $10")
            price = 10
        elif umur_angka >= 65:
            print("Harga $15")
            price = 15
        else:
            print("Harga $20")
            price = 20
        total = total + price
        print("Total: %0.2f" % total)
        
jumlah = int(input("Masukkan Jumlah Uang: "))
hasil = jumlah - total
print("Kembalian: %0.2f" % hasil)
