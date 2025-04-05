def solution(s):
    ans = 10001
    
    # 1부터 len(s)까지 짜르기
    for l in range(1,len(s) + 1):
        cur = ''
        comb = 1
        tmp = s[:l]
        for i in range(l,len(s) + l,l):
            if tmp == s[i:l+i]:
                comb += 1
            else:
                if comb != 1:
                    cur += str(comb) + tmp
                else:
                    cur += tmp
                tmp = s[i:i+l]
                comb = 1
        ans = min(ans, len(cur))
    
    return ans