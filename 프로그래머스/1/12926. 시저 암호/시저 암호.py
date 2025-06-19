def solution(s, n):
    ans = ''
    small = []
    big = []
    for i in range(26):
        small.append(chr(97+i))
        big.append(chr(65+i))
    for i in range(len(s)):
        if s[i] == " ": ans += s[i]
        else:
            # 소문자
            if ord(s[i]) >= 97:
                idx = (small.index(s[i])+n)%26
                ans += small[idx]
            # 대문자
            else:
                idx = (big.index(s[i])+n)%26
                ans += big[idx]
    return ans