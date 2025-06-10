from itertools import combinations as comb
from itertools import product as prod
from bisect import bisect_left as binary
def duel(mydice,yourdice,dice):
    cnt = 0
    # 각 주사위로 승부([3,3,3,4,4,4,4] vs [1,2,3,4,5,6])
    # 주사위로 굴려서 만들 수 있는 모든 수 저장
    your_scores = []
    idx = [i for i in range(6)]
    for p in prod(idx, repeat=len(yourdice)):
        # (0..0) - (5..5)
        # yd의 #1, #2
        score = 0
        for i in range(len(yourdice)):
            score += yourdice[i][p[i]]
        your_scores.append(score)
    # 오름차순 정렬
    your_scores.sort()
    # 내 주사위로 만들 수 있는 모든 점수
    for p in prod(idx, repeat=len(mydice)):
        score = 0
        for i in range(len(mydice)):
            score += mydice[i][p[i]]
        # 내 점수가 네 주사위에서 이길 수 있는 경우의 수
        cnt += binary(your_scores,score)
    return cnt
def solution(dice):
    ans = []
    # 최대 승수
    max_win = 0
    n = len(dice)
    arr = [i for i in range(n)]
    for mine in comb(arr, n//2):
        # 상대 주사위
        your = []
        for a in arr:
            if a not in mine: your.append(a)
        mydice = [dice[i] for i in mine]
        yourdice = [dice[i] for i in your]
        wins = duel(mydice, yourdice,dice)
        if (wins > max_win):
            max_win = wins
            ans = mine
    ans = [a+1 for a in ans]
    return ans