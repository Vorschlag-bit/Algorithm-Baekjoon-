from sys import stdin as input
ans = 0
n = int(input.readline())

arr = [list(map(str,input.readline().strip())) for _ in range(n)]

def seq(seq):
    n = len(seq)
    l = 0
    d = 0
    while l < n:
        r = l
        while r + 1 < n and seq[r+1] == seq[l]:
            r += 1
        d = max(d, r-l+1)
        l = r + 1
    return d

def check_row(x,y):
    return seq(arr[x])

def check_col(x,y):
    return seq([arr[i][y] for i in range(n)])

for i in range(n):
  ans = max(ans, check_row(i,0))

for j in range(n):
  ans = max(ans, check_col(0,j))

for i in range(n):
    for j in range(n):
        # 오른쪽과 스왑
        if j + 1 < n and arr[i][j+1] != arr[i][j]:
            arr[i][j],arr[i][j+1] = arr[i][j+1],arr[i][j]
            ans = max(ans,check_row(i,j),check_col(i,j),check_col(i,j+1))
            arr[i][j],arr[i][j+1] = arr[i][j+1],arr[i][j]
        # 아래와 스왑
        if i + 1 < n and arr[i+1][j] != arr[i][j]:
            arr[i][j],arr[i+1][j] = arr[i+1][j],arr[i][j]
            ans = max(ans,check_row(i,j),check_col(i,j),check_row(i+1,j))
            arr[i][j],arr[i+1][j] = arr[i+1][j],arr[i][j]

print(ans)