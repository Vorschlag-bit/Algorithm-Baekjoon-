from sys import stdin as input
from itertools import permutations as perm
n = int(input.readline())
pool = []
l = [i+1 for i in range(9)]
for p in perm(l,3):
    pool.append(p)

for _ in range(n):
    check,s,b = map(int,input.readline().split())
    filter = []
    for num in pool:
        bl,st = 0,0
        for i,number in enumerate(str(check)):
            if int(number) == num[i]: st += 1
            if int(number) != num[i] and int(number) in num: bl += 1
        if bl == b and st == s: filter.append(num)
    pool = filter
print(len(pool))