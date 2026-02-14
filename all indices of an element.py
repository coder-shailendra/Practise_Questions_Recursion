def print_indices(arr, key, index=0):
    if index == len(arr):
        return
    if arr[index] == key:
        print(index)
    print_indices(arr, key, index + 1)
arr = [1, 2, 3, 2, 4, 2, 5]
key = 2
print_indices(arr, key)
