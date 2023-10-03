print("SJC22MCA-2019-BLESSEY MARIA KURIAN-\nS3MCA")
def bubble_sort (arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j + 1],arr[j]
                swapped = True
            if not swapped:
                break
input_str = input("Enter elements seperated by spaces: ")
elements = [int(x) for x in input_str.split()]

print("Original list:", elements)
bubble_sort(elements)
print("Sorted lists:",elements)

