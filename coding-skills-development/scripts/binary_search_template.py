
def binary_search(nums: list[int], target: int) -> int:
    #Given a sorted array of integers nums and an integer target, 
    # implement a function to determine whether target exists in the array.
    # Return the index of target if found. Otherwise, return -1.

    if nums == []:
        return None
    
    l, r = 0, len(nums) -1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return None

nums, target = [x for x in range(1,10000) for _ in range(10)], 100001
print(binary_search(nums,target)) 
