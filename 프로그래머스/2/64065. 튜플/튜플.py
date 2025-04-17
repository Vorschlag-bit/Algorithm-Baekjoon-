def solution(s):
    s = s[2:-2]
    s = s.split('},{')
    s.sort(key=len)
    ans = dict()
    arr = []
    for unit in s:
        l = map(int, unit.split(','))
        for i in l:
            ans[i] = 0
    for k in ans.keys():
        arr.append(k)
    return arr