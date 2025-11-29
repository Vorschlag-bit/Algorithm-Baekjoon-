from sys import stdin as input

a = " " + input.readline().rstrip()
b = " " + input.readline().rstrip()

n = len(a)
m = len(b)

pre = [0] * m
ans = 0

for i in range(1,n):
    cur = [0] * m
    for j in range(1,m):
        if a[i] == b[j]:
            cur[j] = pre[j-1] + 1
            ans = max(ans, cur[j])
    pre = cur

print(ans)