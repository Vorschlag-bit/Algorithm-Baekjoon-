from sys import stdin as input

n = int(input.readline().rstrip())

arr = [list(map(int, input.readline().rstrip())) for _ in range(n)]
ans = ""
def r(x,y,size,num):
    global ans
    if size == 1:
        ans += str(num)
        return
    flag = True
    for i in range(x,x+size):
        if not flag: break
        for j in range(y,y+size):
            if arr[i][j] != num:
                flag = False
                break
    if flag:
        ans += str(num)
    else:
        l = size // 2
        ans += "("
        for i in range(2):
            for j in range(2):
                r(x+i*l,y+j*l,l,arr[x+i*l][y+j*l])
        ans += ")"
r(0,0,n,arr[0][0])
print(ans)