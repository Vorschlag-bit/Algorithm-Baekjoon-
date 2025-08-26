from sys import stdin as input
# 등수: 자신보다 잘하는 나라 수 + 1
n,k = map(int, input.readline().split())
# n = 국가 수, k는 등수 출력할 나라
arr = []
for _ in range(n):
    country, gold, silver, bronze = map(int, input.readline().split())
    arr.append((country,gold,silver,bronze))
arr.sort(key=lambda x: (-x[1],-x[2],-x[3]))
rank = dict()
prev = arr[0]
prev_rank = 1
rank[prev[0]] = prev_rank

for i in range(1,n):
    cur = arr[i]
    if cur[1] == prev[1] and cur[2] == prev[2] and cur[3] == prev[3]:
        rank[cur[0]] = prev_rank
    else:
        # i명만큼 앞서있음.
        prev_rank = i + 1
        rank[cur[0]] = prev_rank
    prev = cur
print(rank[k])