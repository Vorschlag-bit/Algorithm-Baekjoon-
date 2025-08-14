from sys import stdin as input

n,m = map(int,input.readline().split())
arr = list(map(int,input.readline().split()))
ans = 0

l = 0
s = 0
for r in range(n):
    s += arr[r]
    while s >= m:
        if s == m: ans += 1
        s -= arr[l]
        l += 1
print(ans)