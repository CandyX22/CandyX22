#Candy soeka wiyono - 064002200012
#Program menghitung jarak antara dua titik di permukaan bumi menggunakan rumus dan fungsi trigonometri
import math
input("Masukan Nama Kota A = ")
x1 = float(input("Masukan Lattitude kota A = "))
y1 = float(input("Masukan longittude Kota A = "))

print("\n------------------------------------\n")

input("Masukan Nama Kota B = ")
x2= float(input("Masukan Lattitude kota B = "))
y2= float(input("Masukan longittude Kota B = "))

xlat = x2-x1
ylon = y2-y1

a = math.sin(math.radians(xlat/2)) **2 + math.cos(math.radians(x1)) * math.cos(math.radians(x2)) * math.sin(math.radians(ylon/2)) **2

# versi arc sinus
b = 2 * math.asin(math.sqrt(a))

# versi tangen 2
r = 6371.01

print("\n------------------------------------\n")

print("jarak antara dua kota adalah" , b*r , "kilometer")
