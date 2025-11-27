from sys import stdin as input

n,h = map(int,input.readline().split())

# 죽순 누적합
up = [0] * (h+1)
# 종유석 누적합
down = [0] * (h+1)

i = 0
for _ in range(n):
    num = int(input.readline())
    if i % 2 == 0:
        up[num] += 1
    else:
        down[num] += 1
    i += 1

# 누적합을 역으로 쌓는 의미: 높이(인덱스) 이상의 값의 개수
for i in range(h-1,0,-1):
    up[i] += up[i+1]
    down[i] += down[i+1]

ans = float('inf')
cnt = 0

for i in range(1,h+1):
    c = up[i] + down[h + 1 - i]
    if c < ans:
        ans = c
        cnt = 1
    elif c == ans:
        cnt += 1
print(f"{ans} {cnt}")