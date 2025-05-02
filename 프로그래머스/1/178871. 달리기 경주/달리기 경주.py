def solution(p, call):
    ans = []
    player = dict()
    num = dict()
    cnt = 1
    for pl in p:
        player[pl] = cnt
        num[cnt] = pl
        cnt += 1
    for c in call:
        # 현재 등수
        i = player[c]
        # 제쳐진 선수
        temp = num[i-1]
        player[temp] = i
        player[c] = i-1
        num[i-1] = c
        num[i] = temp
    for n in num.keys():
        ans.append(num[n])
    return ans