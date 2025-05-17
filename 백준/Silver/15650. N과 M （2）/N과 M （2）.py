from itertools import combinations as comb
n,k = map(int,input().split())
arr=[i+1 for i in range(n)]
ans = []
for c in comb(arr,k):
    ans.append(c)
ans.sort()
for a in ans:
    a = list(map(str,a))
    print(' '.join(a))