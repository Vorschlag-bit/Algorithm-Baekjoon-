from itertools import combinations as comb
def solution(relation):
    # 1 ~ col 개수만큼 조합 생성 가능
    col = len(relation[0])
    row = len(relation)
    candid = []
    for r in range(1,col+1):
        for c in comb([i for i in range(col)],r):
            tmp = [tuple(item[i] for i in c) for item in relation]
            if len(set(tmp)) == row:
                check = True
                for can in candid:
                    if set(can).issubset(c):
                        check = False
                        break
                if check: candid.append(c)
    print(candid)
    return len(candid)