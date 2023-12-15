arr = [5,3,7,9,2,5,2,6]

arr_min = 10000
for i in range(len(arr)):
    if arr[i] < arr_min:
        arr_min = arr[i]
print(arr_min)