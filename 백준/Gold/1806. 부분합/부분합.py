from sys import stdin as input

n,s = map(int,input.readline().split())
arr = list(map(int,input.readline().split()))

l = 0
ans = float('inf')
cur_sum = 0
for r in range(n):
    cur_sum += arr[r]
    while cur_sum >= s:
        ans = min(ans, r-l+1)
        cur_sum -= arr[l]
        l += 1
print(ans if ans != float('inf') else 0)