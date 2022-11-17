print("Program fungsi perpangkatan menggunakan konsep rekursif (tanpa for/while). User hanya perlu memasukkan base number (angka awal) dan power (pangkatnya). Hasil akhir berupa perhitungan perpangkatannya ")
print("====================================================================\n")
def nilai():
    print()
    print("Ini merupakan program pemangkatan negatif dan positif, Tekan enter untuk berhenti")
    a = input("Masukkan Angka: ")
    if a == '':
        print("Terima Kasih telah menggunakan Program ini. Program selesai")
        return 0
    p = input("Masukkan Pangkatnya: ")
    hasil = int(a)**int(p)
    print("Hasilnya adalah: ",hasil)
    nilai()

nilai()
print("\n====================================================================")
print("THANK YOU FOR USING THIS PROGRAM.")
print('CANDY SOEKA WIYONO_064002200012')
