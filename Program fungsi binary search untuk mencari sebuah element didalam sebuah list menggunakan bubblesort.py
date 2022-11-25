print("program fungsi binary search untuk mencari sebuah element didalam sebuah list menggunakan bubblesort ")
print("====================================================================================================\n")
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1
arr = [ 28, 77, 46, 99, 12, 22]
x = int(input("massukan angka yang dicari: "))
arr.sort()
print(arr)


result = binary_search(arr, 0, len(arr)-1, x) + 1
 
if result > 1:
    print("Element ditemukan pada posisi ke", str(result))
else:
    print("Element tidak ditemukan pada list")

    print("\n THANK YOU FOR USING THIS PROGRAM.")
    print(' CANDY SOEKA WIYONO_064002200012')

