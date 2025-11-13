def longest_substring_exactly_k_distinct(s,k):
    # Given a string s and an integer k, 
    # return the length of the longest substring that contains exactly k distinct characters.

    if k == 0:
        return 0
    
    freq= {}
    l = 0
    max_len = 0

    for r in range(len(s)):
        freq[s[r]] = freq.get(s[r],0) + 1
   
        # Shrink window if too many distinct chars
        while len(freq) > k:
            freq[s[l]] -= 1
            if freq[s[l]] == 0:
                del freq[s[l]]
            l += 1

        # Log window state
        print(f"Window: s[{l}:{r+1}] = '{s[l:r+1]}', Distinct: {len(freq)}")

        if len(freq) == k:
            max_len = max(max_len, r-l+1)

    return max_len

# s = "abcabcdabcabcabcabc"
# k = 3
# print(longest_substring_exactly_k_distinct(s,k))