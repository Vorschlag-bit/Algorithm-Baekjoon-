from sys import stdin as input
from bisect import bisect_left as bi
arr = []
n = int(input.readline())
for _ in range(n):
    arr.append(int(input.readline()))
dp = [arr[0]]
for i in range(1,len(arr)):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        dp[bi(dp,arr[i])] = arr[i]
print(n-len(dp))