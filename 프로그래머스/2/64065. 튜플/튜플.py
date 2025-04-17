def solution(s):
    s = s[2:-2]
    s = s.split('},{')
    s.sort(key=len)
    ans = []
    for unit in s:
        l = list(map(int, unit.split(',')))
        for i in l:
            if i not in ans:
                ans.append(i)
    return ans