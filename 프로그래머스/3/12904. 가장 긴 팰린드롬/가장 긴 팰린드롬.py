def solution(s):
    ans = 1
    n = len(s)
    for i in range(n):
        l = i-1
        r = i+1
        # 홀수길이
        while l >= 0 and r < n and s[l] == s[r]:
                ans = max(ans, r - l + 1)
                r += 1
                l -= 1
    for i in range(n-1):
        l = i
        r = i+1
        # 짝수길이
        while l >= 0 and r < n and s[l] == s[r]:
            ans = max(ans, r - l + 1)
            r += 1
            l -= 1
    return ans