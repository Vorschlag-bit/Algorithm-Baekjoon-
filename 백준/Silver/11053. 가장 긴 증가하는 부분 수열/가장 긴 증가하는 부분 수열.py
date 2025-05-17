from sys import stdin as input
from bisect import bisect_left
n = int(input.readline())
arr = list(map(int, input.readline().split()))
ans = [arr[0]]
for i in range(1,len(arr)):
    num = arr[i]
    if num > ans[-1]:
        ans.append(num)
    else:
        idx = bisect_left(ans,num)
        ans[idx] = num
print(len(ans))