def solution(seq, k):
    ans = []
    n = len(seq)
    l = 0
    r = 0
    min_l = float('inf')
    cur_s = 0
    while r < n:
        cur_s += seq[r]
        
        while cur_s > k and l <= r:
            cur_s -= seq[l]
            l += 1
            
        if cur_s == k:
            length = r - l + 1
            if length < min_l:
                min_l = length
                ans = [l,r]
        r += 1
    return ans