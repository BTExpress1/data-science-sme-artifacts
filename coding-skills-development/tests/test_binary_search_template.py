import time, pytest
from scripts.binary_search_template import binary_search

@pytest.mark.parametrize("nums, target, expected", [
    ([1, 3, 5, 7, 9], 5, 2),
    ([2, 4, 6, 8, 10], 7, None),
    ([-10, -5, 0, 5, 10], -10, 0),
    ([1], 1, 0),
    ([1], 2, None),
])

def test_basic(nums, target, expected):
    start = time.time() 
    assert binary_search(nums, target) == expected
    elapsed = time.time() - start
    if elapsed > 1.0:
        print(f"⚠️ Slow execution: {elapsed:.2f}s")

# def test_basic():    
#     nums, target = [1, 3, 5, 7, 9], 5    
#     start = time.time()   
#     assert binary_search(nums,target) == 2    
#     elapsed = time.time() - start
#     if elapsed > 1.0:
#         print(f"⚠️ Slow execution: {elapsed:.2f}s")


def test_zero():    
    nums, target = [0,0,0,0,0,0,0], 5    
    start = time.time()   
    assert binary_search(nums,target) == None    
    elapsed = time.time() - start
    if elapsed > 1.0:
        print(f"⚠️ Slow execution: {elapsed:.2f}s")



def test_empty():
    nums, target = [], 1    
    start = time.time()   
    assert binary_search(nums,target) == None    
    elapsed = time.time() - start
    if elapsed > 1.0:
        print(f"⚠️ Slow execution: {elapsed:.2f}s")

# def test_single():    
#     n = [1]    
#     start = time.time()
#     assert remove_duplicates_from_array(n) == [1]
#     elapsed = time.time() - start
#     if elapsed > 1.0:
#         print(f"⚠️ Slow execution: {elapsed:.2f}s")

def test_stress():  # This version also tests duplicates since nums is built with dups.   
    nums, target = [x for x in range(1,10000) for _ in range(10)], 100001 #5026 # [1, 1, 2, 2, 3,3,4,4,5,5] * 10000    
    start = time.time()
    index = binary_search(nums,target)
    assert index is None or nums[index] == target 
    elapsed = time.time() - start
    if elapsed > 1.0:
        print(f"⚠️ Slow execution: {elapsed:.2f}s")

def test_invalid_input():
    with pytest.raises(TypeError):
        binary_search("Hello world",12)

def test_duplicates():
    nums = [1, 3, 3, 3, 5, 7]
    target = 3
    index = binary_search(nums, target)
    assert index is None or nums[index] == target
