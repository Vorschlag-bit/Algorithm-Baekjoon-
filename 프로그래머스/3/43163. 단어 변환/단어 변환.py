from collections import deque
def check(s1,s2):
    return sum(chr1 != chr2 for chr1,chr2 in zip(s1,s2))
def solution(begin, target, words):
    d = {begin:0}
    q = deque()
    q.append(begin)
    n = len(words)
    while q:
        c = q.popleft()
        if c == target:
            break
        for i in range(n):
            if d.get(words[i],0) == 0 and check(c,words[i]) == 1:
                d[words[i]] = d[c] + 1
                q.append(words[i])
    return d.get(target,0)