from collections import deque
n,m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

# 2 = virus, 1 = wall
# wall must be 3
direction = [(0,1),(0,-1),(1,0),(-1,0)]
virus = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            virus.append((i,j))

def combination(arr,r):
    result = []
    rows = len(arr)
    cols = len(arr[0])

    all_rec = [(i,j) for i in range(rows) for j in range(cols)]
    def backtrack(start, cur_comb):
        if len(cur_comb) == r:
            result.append(cur_comb[:])
            return
        
        for idx in range(start,len(all_rec)):
            cur_comb.append(all_rec[idx])
            backtrack(idx+1, cur_comb)
            cur_comb.pop()

    backtrack(0,[])
    return result
comb = combination(arr,3)
def check(x,y):
    return 0 <= x < n and 0<= y < m

def bfs(virus,map):
    q = deque()
    cnt = 0
    for v in virus:
        a,b = v[0],v[1]
        q.append((a,b))
    
    while q:
        cx,cy = q.popleft()

        for i in range(4):
            nx,ny = cx + direction[i][0], cy + direction[i][1]
            if not check(nx,ny): continue
            if map[nx][ny] == 0:
                map[nx][ny] = 2
                q.append((nx,ny))
    for i in range(n):
        for j in range(m):
            if map[i][j] == 0:
                cnt += 1
    return cnt
# 반드시 다 막을 수 있는 보장은 없으니까,완전탐색으로 벽 3개를 세우고 bfs
# 중복을 허용하지 않는 조합
ans = 0
for w1,w2,w3 in comb:
    # 0이 아니라면 pass
    if arr[w1[0]][w1[1]] != 0 or arr[w2[0]][w2[1]] != 0 or arr[w3[0]][w3[1]] != 0:
        continue
    copy = [row[:] for row in arr]
    copy[w1[0]][w1[1]], copy[w2[0]][w2[1]], copy[w3[0]][w3[1]] = 1,1,1
    ans = max(ans,bfs(virus,copy))
print(ans)