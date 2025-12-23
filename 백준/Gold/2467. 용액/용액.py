from sys import stdin as input

n = int(input.readline())

# 산성 = 1부터 1-10억, 알칼리성 = -1부터 -10억
# 정렬된 순서로 산성,알칼리성 용액이 주어질 때 이 중 서로 다른 2개의 용액을 혼합했을 때 0에 가장 가까운
# 만들 수 있는 두 용액 return

arr = list(map(int,input.readline().split()))

# 1. 투 포인터로 풀어보자!
l = 0
r = n-1
ans = float('inf')
al = -1
ar = -1
while r > l:
    cur = arr[r] + arr[l]
    if abs(cur) > ans: pass
    else:
        ans = abs(cur)
        al = l
        ar = r
    # 현재 합이 1 이상이면 알칼리 줄이기
    if cur > 0:
        r -= 1
    # 음수면 산성줄이기
    else:
        l += 1
print(f'{arr[al]} {arr[ar]}')