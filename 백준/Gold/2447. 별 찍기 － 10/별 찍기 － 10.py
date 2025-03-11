
n = int(input())
ans = [[' ']*n for _ in range(n)]
def recursion(x,y,size):
    if size == 3:
        for i in range(3):
            for j in range(3):
                if not (i == 1 and j == 1):
                    ans[x+i][y+j] = '*'
        return
    
    l = size // 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1: continue
            recursion(x+i*l,y+j*l,l)
recursion(0,0,n)
for i in range(n):
    print(''.join(ans[i]))