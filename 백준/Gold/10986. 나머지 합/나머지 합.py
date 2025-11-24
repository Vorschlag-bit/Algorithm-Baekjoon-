from sys import stdin as input
n,m = map(int,input.readline().split())
arr = [0] + list(map(int,input.readline().split()))
ans = 0

# 나머지 개수를 보관할 배열(0~m-1)
cnt = [0] * m

for i in range(1,n+1):
    arr[i] += arr[i-1]

# 어떤 두 지점의 누적합을 나눈 나머지가 서로 같다면 두 지점 사이의 누적합은 반드시 m으로 나눠진다.
for i in range(n+1):
    r = arr[i] % m
    cnt[r] += 1

# cnt[r] >= 2이라면 rC2
for i in range(m):
    if cnt[i] >= 2:
        ans += cnt[i] * (cnt[i] - 1) // 2

print(ans)