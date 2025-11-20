def selection_sort(arr):
    for i in range(0,len(arr)):
        lowest_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[lowest_index]:
                lowest_index = j
        
        arr[i],arr[lowest_index] = arr[lowest_index],arr[i]
    
    return arr

# Examples
print(selection_sort([33,1,89,2,67,245]))
print(selection_sort([5,16,99,12,567,23,15,72,3]))
print(selection_sort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]))
