def solution(answers):
    ans = []
    s1 = 0
    s2 = 0
    s3 = 0
    p1 = [1,2,3,4,5]
    n = len(p1)
    p2 = [2,1,2,3,2,4,2,5]
    k = len(p2)
    p3 = [3,3,1,1,2,2,4,4,5,5]
    m = len(p3)
    c = 1
    for idx,a in enumerate(answers):
        if p1[idx%n] == a: s1 += 1
        if p2[idx%k] == a: s2 += 1
        if p3[idx%m] == a: s3 += 1
        c += 1
    mx = max(s1,s2,s3)
    if mx == s1: ans.append(1)
    if mx == s2: ans.append(2)
    if mx == s3: ans.append(3)
    return ans