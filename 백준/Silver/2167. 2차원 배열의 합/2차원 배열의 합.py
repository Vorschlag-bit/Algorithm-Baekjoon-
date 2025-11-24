from sys import stdin as input

n,m = map(int,input.readline().split())
arr = []
for _ in range(n):
    arr.append([0] + list(map(int,input.readline().split())))
k = int(input.readline())

cmd = []
for _ in range(k):
    i,j,x,y = map(int,input.readline().split())
    cmd.append((i,j,x,y))

# 누적합 계산
for i in range(n):
    for j in range(1,m+1):
        arr[i][j] += arr[i][j-1]

# i,j부터 x,y 위치에 저장되어 있는 수의 합 구하기
for i,j,x,y in cmd:
    s = 0
    for r in range(i,x+1):
        s += arr[r-1][y] - arr[r-1][j-1]
    print(s)