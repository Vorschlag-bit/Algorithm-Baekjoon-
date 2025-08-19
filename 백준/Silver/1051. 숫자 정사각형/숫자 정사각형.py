from sys import stdin as input

n,m = map(int, input.readline().split())

arr = []
ans = 1
for _ in range(n):
    arr.append(list(map(int,input.readline().strip())))

# arr[x][y]에서 대각선과 행으로 l거리에 같은 점이 위치하는지 판단
def check(x,y,l):
    v = l - 1
    if x + v >= n: return False
    if y + v >= m: return False
    if arr[x+v][y] != arr[x][y]: return False
    if arr[x+v][y+v] != arr[x][y]: return False
    return True

for i in range(n):
    for j in range(m):
        for k in range(m-1,-1,-1):
            if arr[i][j] == arr[i][k]:
                l = abs(k-j+1)
                if check(i,j,l):
                    ans = max(ans,l*l)
                    break

print(ans)