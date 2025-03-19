from sys import stdin as input
import copy
n = int(input.readline().rstrip())
arr = [list(map(int, input.readline().split())) for _ in range(n)]
ans = 0

def play(dir,arr):
    # 오른쪽
    if dir == 0:
        for i in range(n):
            point = n-1
            for j in range(n-2,-1,-1):
                if arr[i][j]:
                    value = arr[i][j]
                    arr[i][j] = 0
                    if arr[i][point] == 0:
                        arr[i][point] = value
                    elif arr[i][point] == value:
                        arr[i][point] *= 2
                        point -= 1
                    else: 
                        point -= 1
                        arr[i][point] = value
    # 왼쪽
    elif dir == 1:
        for i in range(n):
            point = 0
            for j in range(1,n):
                if arr[i][j]:
                    value = arr[i][j]
                    arr[i][j] = 0
                    if arr[i][point] == 0:
                        arr[i][point] = value
                    elif arr[i][point] == value:
                        arr[i][point] *= 2
                        point += 1
                    else:
                        point += 1
                        arr[i][point] = value
    # 아래쪽
    elif dir == 2:
        for i in range(n):
            point = n - 1
            for j in range(n-2,-1,-1):
                if arr[j][i]:
                    value = arr[j][i]
                    arr[j][i] = 0
                    if arr[point][i] == 0:
                        arr[point][i] = value
                    elif arr[point][i] == value:
                        arr[point][i] *= 2
                        point -= 1
                    else:
                        point -= 1
                        arr[point][i] = value
    # 위쪽
    else:
        for i in range(n):
            point = 0
            for j in range(1,n):
                if arr[j][i]:
                    value = arr[j][i]
                    arr[j][i] = 0
                    if arr[point][i] == 0:
                        arr[point][i] = value
                    elif arr[point][i] == value:
                        arr[point][i] *= 2
                        point += 1
                    else:
                        point += 1
                        arr[point][i] = value
    return arr

def dfs(dep, map):
    global ans
    if dep == 5:
        for i in range(n):
            for j in range(n):
                if map[i][j] > ans:
                    ans = map[i][j]
        return
    # 우,좌,하,상
    for d in range(4):
        copy_board = copy.deepcopy(map)
        dfs(dep+1, play(d,copy_board))
dfs(0,arr)
print(ans)