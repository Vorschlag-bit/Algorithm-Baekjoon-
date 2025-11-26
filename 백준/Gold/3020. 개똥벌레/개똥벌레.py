from sys import stdin as input

n,h = map(int,input.readline().split())

up = [0] * (h+1)
down = [0] * (h+1)
i = 0

for _ in range(n):
    num = int(input.readline())
    # i가 짝수면 h-1부터 0
    # i가 홀수면 0부터 h-1
    if i % 2 == 0:
        up[num] += 1
    else:
        down[num] += 1
    i += 1

# 높은 곳에서 낮은 곳으로 누적합
for i in range(h-1,0,-1):
    up[i] += up[i+1]
    down[i] += down[i+1]

ans = float('inf')
cnt = 0

for i in range(1,h+1):
    # 종유석은 역순으로 누적해서 down[i] 이상의 것들만 걸림
    # 석순은 h-1-i 이상의 것들만 걸림
    count = down[i] + up[h + 1 -i]
    if count < ans:
        ans = count
        cnt = 1
    elif count == ans:
        cnt += 1

print(f"{ans} {cnt}")