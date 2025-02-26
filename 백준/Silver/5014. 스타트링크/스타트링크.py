from collections import deque
f, s, g, u, d = map(int, input().split())

ans = "use the stairs"

arr = [0] * (f + 1)
q = deque()
arr[s] = 1
q.append((s, 0))

while q:
    now, cnt = q.popleft()
    if now == g:
        ans = cnt
        break
    U = now + u
    D = now - d
    if 1 <= U <= f and arr[U] == 0:
        arr[U] += 1
        q.append((U, cnt + 1))
    if 1 <= D <= f and arr[D] == 0:
        arr[D] += 1
        q.append((D, cnt + 1))
print(ans)