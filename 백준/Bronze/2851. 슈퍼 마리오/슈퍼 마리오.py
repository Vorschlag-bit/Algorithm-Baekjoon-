from sys import stdin as input
m = []
for _ in range(10):
    m.append(int(input.readline()))

for i in range(1,10):
    m[i] += m[i-1]

ans = 0
for i in range(10):
    if m[i] == 100:
        ans = 100
        break
    else:
        if abs(100-m[i]) <= abs(100-ans):
            ans = m[i]

print(ans)