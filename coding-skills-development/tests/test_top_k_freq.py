import time, pytest
from scripts.top_k_freq import longest_substring_k_distinct


def test_basic():    
    s = 'eceba'
    k = 2
    start = time.time()
    assert longest_substring_k_distinct(s,k) == 3
    elapsed = time.time() - start
    if elapsed > 1.0:
        print(f"⚠️ Slow execution: {elapsed:.2f}s")


def test_zero():    
    s = 'aabbcc'
    k = 0       
    start = time.time()
    assert longest_substring_k_distinct(s,k) == 0
    elapsed = time.time() - start
    if elapsed > 1.0:
        print(f"⚠️ Slow execution: {elapsed:.2f}s")



def test_empty():
    s = ''
    k = 2
    start = time.time()
    assert longest_substring_k_distinct(s,k) == 0
    elapsed = time.time() - start
    if elapsed > 1.0:
        print(f"⚠️ Slow execution: {elapsed:.2f}s")

def test_single():    
    s = 'aa'
    k = 1
    start = time.time()
    assert longest_substring_k_distinct(s,k) == 2
    elapsed = time.time() - start
    if elapsed > 1.0:
        print(f"⚠️ Slow execution: {elapsed:.2f}s")

def test_stress():    
    s = 'abc' * 10000
    k = 3
    start = time.time()
    assert longest_substring_k_distinct(s, k) == len(s)
    elapsed = time.time() - start
    if elapsed > 1.0:
        print(f"⚠️ Slow execution: {elapsed:.2f}s")

def test_invalid_input():
    with pytest.raises(TypeError):
        longest_substring_k_distinct(1234,2)

test_basic()
test_zero()
test_empty()
test_single()
test_stress()
test_invalid_input()

print('All tests passed!')
