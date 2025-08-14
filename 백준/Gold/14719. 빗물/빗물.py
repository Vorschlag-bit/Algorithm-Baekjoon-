from sys import stdin as input

n,m = map(int,input.readline().split())
l = list(map(int,input.readline().split()))
arr = [[0] * m for _ in range(n)]
# 각 행별 min(왼쪽 최대 높이, 오른쪽 최대 높이) - 현재 높이, 단 0,m-1은 제외
ans = 0
for i,v in enumerate(l):
    if i == 0 or i == m - 1: continue
    left_max = 0
    right_max = 0
    # 왼쪽 탐색
    for idx in range(i-1,-1,-1):
        left_max = max(left_max,l[idx])
    # 오른쪽 탐색
    for idx in range(i+1,m):
        right_max = max(right_max,l[idx])
    h = min(left_max,right_max) - l[i]
    if h > 0: ans += h
print(ans)