def solution(seq):
    ans = max(seq)
    # -,+를 입힌 배열
    marr = []
    # +,-를 입힌 배열
    parr = []
    for i,n in enumerate(seq):
        if i % 2 == 0:
            marr.append(-n)
            parr.append(n)
        else:
            marr.append(n)
            parr.append(-n)
    # 두 배열의 부분합 최대
    cur = 0
    for n in marr:
        cur += n
        if cur < 0:
            cur = 0
        ans = max(cur,ans)
    cur = 0
    for n in parr:
        cur += n
        if cur < 0:
            cur = 0
        ans = max(cur,ans)
    return ans