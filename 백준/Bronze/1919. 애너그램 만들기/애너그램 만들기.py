import sys
import math
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

dic1 = {}
dic2 = {}

for i in range(len(str1)):
    alp = str1[i]
    dic1[alp] = dic1.get(alp, 0) + 1

for i in range(len(str2)):
    alp = str2[i]
    dic2[alp] = dic2.get(alp, 0) + 1
ans = 0
for k in dic1.keys():
    if k not in dic2.keys():
        ans += dic1[k]
    elif k in dic2.keys() and dic1[k] != dic2[k]:
        ans += abs(dic1[k] - dic2[k])
for k in dic2.keys():
    if k not in dic1.keys():
        ans += dic2[k]
print(ans)