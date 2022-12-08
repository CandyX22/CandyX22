class mahasiswa :
    mahcount = 0
    
    def __init__(self, nama, nim, angkatan):
        self.nama = nama
        self.nim = nim
        self.angkatan = angkatan
        mahasiswa.mahcount +=1
        
    def displaycount(self):
        print("total mahasiswa %d" % mahasiswa.mahcount)
        
    def displaymahasiswa(self):
        print("Nama :", self.nama, "\nNim :", self.nim, "\nAngkatan :", self.angkatan)
        
nama = str(input("masukan nama : "))
nim = str(input("masukan nim : "))
angkatan = int(input("masukan angkatan  : "))

mah1 = mahasiswa(nama,nim,angkatan)
mah1.displaymahasiswa()

print("total mahasiswa %d" %mahasiswa.mahcount)

