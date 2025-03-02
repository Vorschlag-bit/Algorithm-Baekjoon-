from sys import stdin as input

t = int(input.readline().rstrip())

for _ in range(t):
    n = int(input.readline().rstrip())
    arr = [0] + list(map(int, input.readline().split()))
    visit = [0] * (n + 1)
    for i in range(1,n+1):
        start = i
        while visit[i] == 0:
            visit[i] = start
            i = arr[i]
        while visit[i] == start:
            visit[i] = -1
            i = arr[i]
    mate = visit.count(-1)
    print(n - mate)