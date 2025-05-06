from itertools import combinations as comb
def solution(wall):
    # drag -> 왼쪽에서 오른쪽으로 이동, drag d = 맨하튼 거리
    arr = []
    n = len(wall)
    m = len(wall[0])
    mini,maxi = float('inf'),0
    minj,maxj = float('inf'),0
    for i in range(n):
        for j in range(m):
            if wall[i][j] == '#':
                arr.append((i,j))
                if mini > i:
                    mini = i
                if i > maxi:
                    maxi = i
                if minj > j:
                    minj = j
                if maxj < j:
                    maxj = j
    print(mini,minj,maxi,maxj)
    return [mini,minj,maxi+1,maxj+1]