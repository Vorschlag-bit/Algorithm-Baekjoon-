from sys import stdin as input
from collections import defaultdict

name = input.readline().strip()
d = defaultdict(int)

for chr in name:
    d[chr] += 1

middle = ""
odd_count = 0
for k, v in d.items():
    if v % 2 == 1:
        odd_count += 1
        middle = k

if odd_count > 1:
    print("I'm Sorry Hansoo")
    exit()

sorted_keys = sorted(d.keys())
ans = ""
for k in sorted_keys:
    cnt = d[k] // 2
    ans += k * cnt

ans += middle

for k in reversed(sorted_keys):
    cnt = d[k] // 2
    ans += k * cnt

print(ans)