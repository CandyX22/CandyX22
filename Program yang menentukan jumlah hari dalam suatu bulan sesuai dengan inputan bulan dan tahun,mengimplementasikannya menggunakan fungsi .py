print("Program yang menentukan jumlah hari dalam suatu bulan sesuai dengan inputan bulan dan tahun,mengimplementasikannya menggunakan fungsi ")
print("\n=================================================================================================")
ulangi = "y"
print("\nTekan 0 untuk keluar dari program")
print("Silahkan tekan angka bulan dari ke-1 hingga ke-12")

def Perhitungan(B):
    if (bulan == 0 ):
        print("")
        
    elif (bulan == 1 ):
        print("Bulan ke-1 adalah bulan Januari yang memiliki 31 hari.")
        
    elif (bulan == 2 ):
        tahun = int(input("Masukkan tahun = tahun ke-"))
        t = tahun%4
        
        if (t == 0):
            print("Bulan ke-2 adalah bulan Februari yang memiliki 29 hari.")
            print("Alasan adanya 29 hari karena adanya tahun kabisat.")
        else :
            print("Bulan ke-2 adalah bulan Februari yang memiliki 28 hari.")
            print("Tahun ini tidak termasuk tahun kabisat.")
            
    elif (bulan == 3 ):
        print("Bulan ke-3 adalah bulan Maret yang memiliki 31 hari.")
        
    elif (bulan == 4 ):
        print("Bulan ke-4 adalah bulan April yang memiliki 30 hari.")
        
    elif (bulan == 5 ):
        print("Bulan ke-5 adalah bulan Mei yang memiliki 31 hari.")
        
    elif (bulan == 6 ):
        print("Bulan ke-6 adalah bulan Juni yang memiliki 30 hari.")
        
    elif (bulan == 7 ):
        print("Bulan ke-7 adalah bulan Juli yang memiliki 31 hari.")
        
    elif (bulan == 8 ):
        print("Bulan ke-8 adalah bulan Agustus yang memiliki 31 hari.")
        
    elif (bulan == 9 ):
        print("Bulan ke-9 adalah bulan September yang memiliki 30 hari.")
        
    elif (bulan == 10 ):
        print("Bulan ke-10 adalah bulan Oktober yang memiliki 31 hari.")
        
    elif (bulan == 11 ):
        print("Bulan ke-11 adalah bulan November yang memiliki 30 hari.")
        
    elif (bulan == 12 ):
        print("Bulan ke-12 adalah bulan Desember yang memiliki 31 hari.")
        
    else :
        print("Maaf, anda salah memasukkan angka. Silahkan coba lagi")
        
    return bulan

while (ulangi == "y" or ulangi == "Y"):
    bulan  = int(input("Masukkan bulan = bulan ke-"))
    Perhitungan(bulan)
    
    if (bulan == 0):
        break
    
    ulangi = input("\nApakah anda ingin mengulanginya lagi?(tekan y untuk mengulang atau tekan t untuk berhenti) = ")
    
print("THANK YOU FOR USING THIS PROGRAM.")
print('CANDY SOEKA WIYONO_064002200012')
