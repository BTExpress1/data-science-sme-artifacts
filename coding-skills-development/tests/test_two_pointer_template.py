import time, pytest
from scripts.two_pointer_template import remove_duplicates_from_array


def test_basic():    
    n = [1, 1, 2, 2, 3]    
    start = time.time()   
    assert remove_duplicates_from_array(n) == [1,2,3]    
    elapsed = time.time() - start
    if elapsed > 1.0:
        print(f"⚠️ Slow execution: {elapsed:.2f}s")


def test_zero():    
    n = [0,0,0,0,0]    
    start = time.time()
    assert remove_duplicates_from_array(n) == [0]
    elapsed = time.time() - start
    if elapsed > 1.0:
        print(f"⚠️ Slow execution: {elapsed:.2f}s")



def test_empty():
    n = []    
    start = time.time()
    assert remove_duplicates_from_array(n) == []
    elapsed = time.time() - start
    if elapsed > 1.0:
        print(f"⚠️ Slow execution: {elapsed:.2f}s")

def test_single():    
    n = [1]    
    start = time.time()
    assert remove_duplicates_from_array(n) == [1]
    elapsed = time.time() - start
    if elapsed > 1.0:
        print(f"⚠️ Slow execution: {elapsed:.2f}s")

def test_stress():    
    n = [x for x in range(1,6) for _ in range(20000)] # [1, 1, 2, 2, 3,3,4,4,5,5] * 10000    
    start = time.time()
    assert remove_duplicates_from_array(n) == [1,2,3,4,5]
    elapsed = time.time() - start
    if elapsed > 1.0:
        print(f"⚠️ Slow execution: {elapsed:.2f}s")

def test_invalid_input():
    with pytest.raises(TypeError):
        remove_duplicates_from_array(1234,2)

# test_basic()
# test_zero()
# test_empty()
# test_single()
# test_stress()
# test_invalid_input()

# print('All tests passed!')
