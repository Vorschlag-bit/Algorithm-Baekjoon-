from sys import stdin as input

n,s = map(int,input.readline().split())
arr = list(map(int,input.readline().split()))
l = 0
cur = 0
ans = float('inf')

for i in range(n):
    cur += arr[i]
    while cur >= s:
        cur -= arr[l]
        ans = min(ans, i-l+1)
        l += 1
print(ans) if ans != float('inf') else print(0)