print("program yang bisa menampilkan output seperti berikut ini 1 //Input,1st //output dst")
print("===================================================================================\n")
def ordinal():
    print("Ordinal Number")
    print("ketik 0 untuk menghentikan program")
    while True:
        num = int(input("Masukan sebuah ankga: "))
        if num in [10, 11, 12, 13]:
            print("(", num, "'th'", ")")
        else:
            ka = num % 10
            if ka == 1:
                print("(", num, "'st", ")")
            elif ka == 2:
                print("(", num, "'nd'", ")")
            elif ka == 3:
                print("(", num, "'rd'", ")")
            else:
                print("(", num, "'th'", ")")
        if num == 0:
           
            print("THANK YOU FOR USING THIS PROGRAM.")
            print('CANDY SOEKA WIYONO_064002200012')

            break
a = ordinal()
print(a)

