def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        # Print the array after each iteration
        print(f"Step {i+1}: {arr}")

# Example array to sort
arr = [64, 25, 12, 22, 11]
print(f"Original array: {arr}")
selection_sort(arr)
print(f"Sorted array: {arr}")
