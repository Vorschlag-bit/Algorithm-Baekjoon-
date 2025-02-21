from collections import deque
def solution(b, t, words):
    ans = 0
    q = deque()
    def check_d(str1, str2):
        return sum(c1 != c2 for c1, c2 in zip(str1, str2))
    n = len(words)
    
    q.append(b)
    dic = {b: 0}
    while q:
        cur = q.popleft()
        if cur == t:
            break
        for i in range(n):
            if words[i] not in dic and check_d(words[i], cur) == 1:
                dic[words[i]] = dic[cur] + 1
                q.append(words[i])
    return dic.get(t , 0)