from sys import stdin as input
n = int(input.readline())
arr = [0] + list(map(int,input.readline().split()))
s = arr[:]
# 최대로 획득할 수 있는 꿀의 양 return
ans = 0

# 누적합
for i in range(n):
    s[i+1] += s[i]

# 0,1에서 시작 - 투 포인터
ans += s[n] - s[2]
ans += s[n] - s[2]

# 로직
# s[n] - s[i-1] - arr[i]

# 벌통의 인덱스를 1 ~ N까지 둠
# 최대가 될 수 있는 건 
# 1. 양 벌 모두 왼쪽에서 -> 방향으로 출발
# 2. 양 벌 모두 오른쪽에서 <- 방향으로 출발
# 3. 각 벌이 왼,오른 끝에서 가운데 벌통으로 출발

for i in range(1,n+1):
    # 1번 케이스(1,i), 벌통은 N
    if i >= 2:
        cur = 0
        # 1번 벌
        cur += s[n] - s[0] - arr[1] - arr[i]
        # i번 벌
        cur += s[n] - s[i-1] - arr[i]
        ans = max(ans, cur)
    
    # 2번 케이스(i,N), 벌통은 1
    if i <= n-1:
        cur = 0
        # n번 벌
        cur += s[n] - s[0] - arr[n] - arr[i]
        # i번 벌
        cur += s[i] - s[0] - arr[i]
        ans = max(ans, cur)

    # 3번 케이스(1,n), 벌통은 i
    if 2 <= i <= n-1:
        cur = 0
        # 1번 벌
        cur += s[i] - s[0] - arr[1]
        # n번 벌
        cur += s[n] - s[i-1] - arr[n]
        ans = max(ans, cur)
print(ans)