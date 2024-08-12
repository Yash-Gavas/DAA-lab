def merge_sort_count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left_half, left_inversions = merge_sort_count_inversions(arr[:mid])
    right_half, right_inversions = merge_sort_count_inversions(arr[mid:])

    merged_arr, merge_inversions = merge_and_count(left_half, right_half)

    total_inversions = left_inversions + right_inversions + merge_inversions

    return merged_arr, total_inversions

def merge_and_count(left, right):
    merged = []
    inversions = 0
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inversions += len(left) - i  # Count inversions

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inversions

# Taking user input for the number of arrays
num_arrays = int(input("Enter the number of arrays: "))

arrays = []
for i in range(num_arrays):
    arr = list(map(int, input(f"Enter the elements of array {i + 1} (space-separated): ").split()))
    arrays.append(arr)

# Processing each array
for i, arr in enumerate(arrays):
    sorted_arr, inversions = merge_sort_count_inversions(arr)
    print(f"\nArray {i + 1}: {arr}")
    print(f"Sorted array: {sorted_arr}")
    print(f"Number of inversions: {inversions}")
