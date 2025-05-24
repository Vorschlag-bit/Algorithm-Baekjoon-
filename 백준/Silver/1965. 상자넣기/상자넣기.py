from sys import stdin as input
from bisect import bisect_left as bi
n = int(input.readline())
arr = list(map(int,input.readline().split()))
ans = [arr[0]]
for i in range(len(arr)):
    num = arr[i]
    if num > ans[-1]:
        ans.append(num)
    else:
        ans[bi(ans,num)] = num
print(len(ans))