# this will move minimum number to 1st index
# second minimum number to 2nd index

def selection_sort(arr=[6,4,0,1,3]):
    for i in range(len(arr)): # 0 - 4
        minimum = i
        for j in range(i + 1, len(arr)): # 1-4 / 2-4 / 3-4 // leaving first index
            if arr[j] < arr[minimum]: # 4<6
                minimum = j
                print("test")
        arr[minimum], arr[i] = arr[i], arr[minimum] # # Place it at the front of the

        print(arr)
selection_sort()