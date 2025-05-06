def solution(n, y, photo):
    ans = []
    score = dict()
    for i,s in enumerate(y):
        score[n[i]] = s
    for pic in photo:
        total = 0
        for per in pic:
            total += score.get(per,0)
        ans.append(total)
    return ans