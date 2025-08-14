from sys import stdin as input

n,k = map(int,input.readline().split())
arr = list(map(int,input.readline().split()))
ans = float('-inf')

l = 0
s = 0
for r in range(n):
    s += arr[r]
    if r-l+1 == k:
        ans = max(ans,s)
        s -= arr[l]
        l += 1

print(ans)