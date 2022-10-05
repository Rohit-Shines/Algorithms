# Optimized Bubble sort in Python
# https://www.programiz.com/dsa/bubble-sort
# the highest number will go to end automatically
# the second highgest number goes to last second row


def bubbleSort(nums=[-2, 3,11,45, 0, 11, -9]):
    for i in range(len(nums)):# 0,1,2,3,4
        # swapped = False
        for j in range(0, len(nums) - i - 1): # Main logic to avoid last index number every time
            if nums[j] > nums[j + 1]:
                temp = nums[j]     # Bubble Logic
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
        print( nums)
    print('Sorted Array in Ascending Order:',nums)

bubbleSort()

