from sys import stdin as input
from collections import defaultdict
# 맨하튼 거리 1인 두 점이 인접
# 1. 비어있는 칸 중 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리 정하기
# 2. 1이 여러 개일 경우, 인접한 칸 중 빈 칸이 가장 많은 칸으로 정하기
# 3. 2도 여러 개일 경우, 행의 번호가 가장 적은 칸으로,  그것도 여러 개면 열 번호가 가장 적은 칸으로
# 특정 학생이 앉을 수 있는 후보군: [(좋아하는 학생 수, 빈 칸 수, 행,열)]
# 후보군은 반드시 빈 칸이며, 완전 탐색으로 찾기 400 * 400 -> 160000
n = int(input.readline())
arr = [[0] * n for _ in range(n)]
# 만족도
satisfaction = {0:0,1:1,2:10,3:100,4:1000}
# 맨하튼 거리 directions
directions = [(1,0),(0,1),(0,-1),(-1,0)]
# 학생 번호 - k, 최애 set - v
favor = defaultdict(set)
# 학생 배치 순서
students = []
for _ in range(n*n):
    l = list(map(int,input.readline().split()))
    student = l[0]
    students.append(student)
    s = set(l[1:])
    favor[student] = s

def check(x,y):
    return 0 <= x < n and 0 <= y < n

def get_can(x,y,student,can):
    f = favor[student]
    # 빈 칸 수
    blank = 0
    # 최애 수
    cnt = 0
    for d in directions:
        nx,ny = x + d[0], y + d[1]
        if not check(nx,ny): continue
        if arr[nx][ny] == 0:
            blank += 1
        elif arr[nx][ny] in f:
            cnt += 1
    can.append((cnt,blank,x,y))

for student in students:
    can = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                get_can(i,j,student,can)
    
    # 최적의 장소 찾기
    can.sort(key=lambda x: (-x[0],-x[1],x[2],x[3]))
    place = can[0]
    x,y = place[2], place[3]
    arr[x][y] = student

ans = 0

def get_satis(x,y):
    global ans,arr
    student = arr[x][y]
    f = favor[student]
    cnt = 0
    for d in directions:
        nx,ny = x + d[0], y + d[1]
        if not check(nx,ny): continue
        if arr[nx][ny] in f: cnt += 1
    
    ans += satisfaction[cnt]

# 만족도 구하기
for i in range(n):
    for j in range(n):
        get_satis(i,j)

# print(students)

# for i in range(n):
#     print(arr[i])

print(ans)