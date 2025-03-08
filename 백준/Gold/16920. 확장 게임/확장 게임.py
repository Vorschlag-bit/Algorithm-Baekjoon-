from collections import deque
from sys import stdin as input

n,m,p = map(int, input.readline().split())
dic = dict()
s = [0] + list(map(int, input.readline().split()))
for i in range(p):
    dic[i+1] = s[i]
arr = [list(map(str, input.readline().rstrip())) for _ in range(n)]
player = [deque() for _ in range(p+1)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
ans = dict()
for i in range(1,p+1):
    for j in range(n):
        for k in range(m):
            if arr[j][k] == str(i):
                player[i].append((j,k))
                ans[i] = ans.get(i, 0) + 1

def check(x,y):
    return 0 <= x < n and 0<= y < m

flag = True
while flag:
    flag = False
    # 각 플레이어턴
    for i in range(1,p+1):
        q = player[i]
        # 더이상 확장할 수 없다면 패스
        if not q: continue
        # si만큼 확장
        for _ in range(s[i]):
            # 더이상 확장불가면 break
            if not q: break
            for _ in range(len(q)):
                x,y = q.popleft()
                for j in range(4):
                    nx, ny = x + dx[j], y + dy[j]
                    if not check(nx,ny): continue
                    if arr[nx][ny] == '.':
                        arr[nx][ny] = str(i)
                        q.append((nx,ny))
                        ans[i] +=1
                        flag = True

print(" ".join(map(str, ans.values())))