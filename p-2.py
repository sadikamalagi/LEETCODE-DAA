def find_max_min(arr, low, high):
    
    if low == high:
        return arr[low], arr[low]
    
    
    elif high == low + 1:
        if arr[low] > arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    
    
    else:
        mid = (low + high) // 2

       
        max1, min1 = find_max_min(arr, low, mid)

       
        max2, min2 = find_max_min(arr, mid + 1, high)

       
        return max(max1, max2), min(min1, min2)



arr = [12, 123, 2, 35, 45, 99, 7, 19]
n = len(arr)

max_val, min_val = find_max_min(arr, 0, n - 1)
print(f"Maximum element is {max_val}")
print(f"Minimum element is {min_val}")
