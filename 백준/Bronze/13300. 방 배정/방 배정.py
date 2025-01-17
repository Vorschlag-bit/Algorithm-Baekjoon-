import sys

input = sys.stdin.readline

n, k = map(int, input().split())

room = {}

for i in range(n):
    p = input().strip()
    room[p] = room.get(p, 0) + 1
ans = 0
for key in room:
    if (room[key] // k == 0):
        ans += 1
    elif (room[key] // k > 0 and room[key] % k == 0):
        ans += room[key] // k
    else:
        ans += room[key] // k + 1
print(ans)