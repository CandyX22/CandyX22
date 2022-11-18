print("Program membuat Text File dengan nama Biodata.txt menggunakan impelementasi File Handling ")
print("==========================================================================================\n")
def buatfile(nama,Umur,alamat,email,dosenwali):

    file = open('Biodata.txt','w')
    file.write(f'Nama : {nama} \nUmur : {Umur} \nAlamat : {alamat} \nEmail : {email} \nDosen wali : {dosenwali}')
    file.close()
def bacafile():
    file = open('Biodata.txt','r')
    text = file.read()
    print(text)
    file.close()

nama = input('Masukkan Nama : ')
Umur = input('Masukkan Umur : ')
alamat = input('Masukkan alamat : ')
email = input('Masukkan email : ')
dosenwali = input('Masukkan dosen wali : ')
print('\nBerikut ini data kamu ')
data :(nama,Umur,alamat,email,dosenwali)
bacafile()
print("THANK YOU FOR USING THIS PROGRAM.")
print('CANDY SOEKA WIYONO_064002200012')
