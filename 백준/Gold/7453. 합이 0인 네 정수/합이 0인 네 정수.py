from sys import stdin as input
from collections import Counter

n = int(input.readline())
a = []
b = []
c = []
d = []

for _ in range(n):
    a1,b1,c1,d1 = map(int,input.readline().split())
    a.append(a1)
    b.append(b1)
    c.append(c1)
    d.append(d1)

# ab와 cd로 만들어 질 수 있는 모든 경우의 수
ab = []
cd = []
for i in range(n):
    a1 = a[i]
    c1 = c[i]
    for j in range(n):
        b1 = b[j]
        d1 = d[j]
        ab.append(a1+b1)
        cd.append(c1+d1)

cnt = Counter(ab)
ans = 0
for ele in cd:
    ans += cnt.get(-ele,0)
print(ans)