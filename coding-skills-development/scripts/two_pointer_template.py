def remove_duplicates_from_array(arr):
    # Given a sorted array nums, remove the duplicates in-place 
    # such that each element appears only once and return the new length. 
    # You must do this with O(1) extra space — meaning no new array 
    if len(arr) <= 1:
        return arr
    
    l,r = 0,0

    while r < len(arr) and l < len(arr) - 1:
        r = l + 1        
        if arr[r] == arr[l]:
            del arr[r]            
        else:
            l +=1
    return arr
    
# n = [0,0,0,0,0]
# n =  [1,1,2,2,3]
n = [1, 1, 2, 2, 3,3,4,4,5,5] * 10000 
n.sort()
print(remove_duplicates_from_array(n))
#remove_duplicates_from_array(n)
    
