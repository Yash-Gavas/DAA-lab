def partition(arr, low, high):
    pivot = arr[low]
    i = low

    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[i] = arr[i], arr[low]
    return i

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

arr = list(map(int, input("Enter the numbers: ").split()))
n = len(arr)
quick_sort(arr, 0, n - 1)
print("Sorted array:", arr)
