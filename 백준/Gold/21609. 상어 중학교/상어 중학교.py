from sys import stdin as input
from collections import deque,defaultdict
# 검은색 -1, 일반 m이하의 자연수, 무지개 블록 0 존재. 
# 블록 그룹에는 적어도 하나 이상의 일반 블록이 존재해야 하며, 일반 블록은 같은 색상이어야 함.
# 무지개 블록은 몇 개든 상관없고 검은색은 있어선 안 된다.
# 그룹에 속한 블록 최소 2개 이상이어야 한다.
# 그룹의 기준블록 -> 무지개가 아닌 블록 중에서 행의 번호가 가장 작은 블록, 
# 그게 여러 개면 열의 번호가 가장 작은 블록
# 그룹 블록이 존재할 때까지 반복
# 1. 크기가 가장 큰 그룹 블록 찾기, 여러 개라면 무지개 블록 최대, 여러 개면 행 최대, 열 최대
# 2. 1에서 찾은 블록 그룹의 모든 블록 제거. 블록 수**2만큼 점수 획득
# 3. 격자에 중력작용
# 4. 격자가 반시계 90도 회전
# 5. 다시 중력
# 중력이 작동할 경우 검은색(-1)을 제외한 모든 블록이 행 아래로 이동
n,m = map(int,input.readline().split())
arr = [list(map(int,input.readline().split())) for _ in range(n)]
ans = 0
directions = [(0,1),(1,0),(0,-1),(-1,0)]
def check(x,y):
    return 0 <= x < n and 0 <= y < n

def bfs(x,y,color,no,group,group_dict):
    q = deque()
    visit = [[False] * n for _ in range(n)]
    visit[x][y] = True
    # 블록 크기
    size = 1
    # 무지개 개수
    rainbow = 0
    # 대표 블록 행,열
    row = x
    col = y
    l = [(x,y)]
    q.append((x,y))
    while q:
        cx,cy = q.popleft()
        if arr[cx][cy] == 0: rainbow += 1
        # 무지개 제외 기준 블록 후보 고려
        if arr[cx][cy] > 0:
            if row > cx or (row == cx and col > cy):
                row,col = cx,cy
        for d in directions:
            nx,ny = cx + d[0], cy + d[1]
            if not check(nx,ny): continue
            nxc = arr[nx][ny]
            if not visit[nx][ny] and (nxc == 0 or nxc == color):
                visit[nx][ny] = True
                size += 1
                l.append((nx,ny))
                q.append((nx,ny))
    # 최소 2개 이상
    if size < 2: return
    group_dict[no] = l
    group.append((size,rainbow,row,col,no))


def gravity(arr):
    for j in range(n):
        write = n-1
        for i in range(n-1,-1,-1):
            if arr[i][j] == -1:
                # 검은색 만날 경우 그 외로 조정
                write = i-1
            elif arr[i][j] >= 0:
                # 빈 칸 아닌 경우 중력
                if write != i:
                    arr[write][j],arr[i][j] = arr[i][j],-2
                write -= 1

while True:
    # 그룹 블록 찾기
    # 그룹 번호
    no = 1
    # k = 그룹 번호, v = 그룹 좌표 리스트
    group_dict = defaultdict(list)
    # (크기,무지개 블록 수, 행,열,그룹 번호)
    group = []
    for i in range(n):
        for j in range(n):
            # 그룹은 무조건 일반 블록이 하나 이상있어야 함.
            if arr[i][j] > 0:
                bfs(i,j,arr[i][j],no,group,group_dict)
                no += 1
    # 그룹 블록 없으면 종료
    if len(group) == 0: break

    # 제거할 그룹 블록 찾기(다 최대)
    group.sort(key=lambda x: (-x[0],-x[1],-x[2],-x[3]))
    num = group[0][4]
    for x,y in group_dict[num]:
        # 제거하면 -2
        arr[x][y] = -2
    # 점수 반영
    ans += group[0][0]**2
    # 격자 중력작용
    gravity(arr)
    # 반 시계 90도 회전 -> 행렬 반대 행 뒤집기
    pre = list(zip(*arr))
    rotate = pre[::-1]
    arr = list(map(list, rotate))
    # 다시 중력
    gravity(arr)
print(ans)