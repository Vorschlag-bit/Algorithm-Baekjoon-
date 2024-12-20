from collections import deque

n = int(input())

candis = [str(i) for i in range(10)]

q = deque()
q.append('666')
ans = set()

while q:
    current = q.popleft()
    if len(current) == 7:
        break
    for candi in candis:
        q.append(str(current) + candi)
        ans.add(int(str(current) + candi))
        q.append(candi + str(current))
        ans.add(int(candi + str(current)))

print(sorted(list(ans))[n - 1])