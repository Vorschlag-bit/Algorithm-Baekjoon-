import sys

input = sys.stdin.readline

n = int(input().strip())

arr = list(map(int, input().split()))
ans = {}
for i in arr:
    ans[i] = ans.get(i, 0) + 1

t = int(input().strip())

print(ans.get(t, 0))