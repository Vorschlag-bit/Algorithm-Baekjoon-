from itertools import combinations as comb, product as prod
from bisect import bisect_left
def getWin(mydice,yourdice):
    # yd = [[3,3,3,3,3,3],[1,2,3,4,5,6]]
    # 이 주사위로 만들 수 있는 합의 1차원 배열 생성
    win = 0
    l = list(range(6))
    b = []
    for i in prod(l, repeat=len(yourdice)):
        # i = (0,0) - (5,5)
        value = 0
        for j in range(len(yourdice)):
            value += yourdice[j][i[j]]
        b.append(value)
    b.sort()
    for i in prod(l, repeat=len(mydice)):
        # (0,0) - (5,5)
        # (0,0)의 합을 구하고, 그게 상대방의 배열에서 이길 수 있는 수 구하기
        value = 0
        for j in range(len(mydice)):
            value += mydice[j][i[j]]
        win += bisect_left(b,value)
    return win

def solution(dice):
    # 서로 주사위를 반반 나누고, 나올 수 있는 합의 배열을 만든 후, 상대방 배열에서
    # 이진탐색으로 이길 수 있는 인덱 = 승 개수
    maxWin = 0
    answer = []
    size = list(range(len(dice)))
    for md in comb(size, len(dice)//2):
        yd = []
        for n in size:
        # 내게 없는 주사위 idx는 상대 꺼
            if n not in md:
                yd.append(n)
        m = [dice[i] for i in md]
        y = [dice[i] for i in yd]
        
        wins = getWin(m,y)
        
        if wins > maxWin:
            maxWin = wins
            answer = md
        
    answer = [x+1 for x in answer]
    return answer