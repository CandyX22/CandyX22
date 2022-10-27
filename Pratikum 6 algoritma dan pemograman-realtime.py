print('program yang sebelumnya telah dibuat yaitu program untuk merata-ratakan nilai sesuai dengan kategori huruf yang diinputkan dengan mengimpelementasikan fungsi yang sudah dipelajari. Persyaratan program yaitu fungsi menggunakan default argument/parameter dan mengimplementasikan pengembalian nilai')
print("\n======================================================================================\n")
def kategori(n = "0", total = 0, tampung = 0):
    while (n != ''):
        n = str(input('masukan nilai : '))
        tampung +=1
        if(n == ''):
            if(tampung == 1):
                return 0
            else:
                return total/(tampung - 1)
        elif (n == "A"):
                print('nilai = 4.0')
                total += 4.0
        elif (n == 'A-'):
                print('nilai = 3.25')
                total +=3.25
        elif (n == 'A+'):
                print('nilai = 3.15')
                total +=3.15
        elif (n == 'B+'):
                    print('nilai = 3.0')
                    total += 3.0
        elif (n == 'B'):
             print('nilai = 2.5')
             total += 2.5
        elif (n == 'B-'):
              print('nilai = 1.50')
              total += 1.50
        elif (n == 'C+'):
              print('nilai = 1.8')
              total += 1.8
        else:
            tampung -=1
            print("masukan nilai yang benar")
            
rerata = kategori()
print ("\n Rata-ratanya adalah: ", rerata)
print("THANK YOU FOR USING THIS PROGRAM.")
print('CANDY SOEKA WIYONO_064002200012')


                
                