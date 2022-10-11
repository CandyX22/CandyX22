#CANDY SOEKA WIYONO_(064002200012)
#PROGRAM MENCETAK 10 BILANGAN YANG LEBIH BESAR DARI BILANGAN TERSEBUT
#PROGRAM MENCETAK 10 BILANGAN YANG LEBIH KECIL DARI BILANGAN TERSEBUT

ulang = "z"
listA = []
listB = []
while ulang == "z":
    x = int(input("Masukkan Angka: "))
    b=x
    a=x


    for i in range(10):
        a += 1
        listA.append(a)
    
    for i in range(10):
        b -= 1
        listB.append(b)
        
    print("10 angka setelah",x,"yaitu", listA )   
    print("10 angka sebelum",x,"yaitu", listB )
    ulang = input("Ketik z untuk ulang, ketik 0 untuk berhenti ")
    if ulang == "0":
        print("THANK YOU FOR USING THIS PROGRAM.")
        print('CANDY SOEKA WIYONO_064002200012')
        break