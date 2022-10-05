# Insertion sort in Python
def insertionSort(nums):
    for i in range(1, len(nums)):
        key = nums[i]; j = i - 1
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<nums[j] to key>nums[j].
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        nums[j + 1] = key


data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)