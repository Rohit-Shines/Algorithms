# this will move minimum number to 1st index
# second minimum number to 2nd index

def selection_sort(nums=[6, 4, 0, 1, 3]):
    for i in range(len(nums)): # 0 - 4
        minimum = i
        for j in range(i + 1, len(nums)): # 1-4 / 2-4 / 3-4 // leaving first index
            if nums[j] < nums[minimum]: # 4<6
                minimum = j
                print("test")
        nums[minimum], nums[i] = nums[i], nums[minimum] # # Place it at the front of the

        print(nums)
selection_sort()