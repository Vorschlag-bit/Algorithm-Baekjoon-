from sys import stdin as input

n = int(input.readline().rstrip())

arr = [list(map(int, input.readline().split())) for _ in range(n)]

dic = dict()
dic[-1] = 0
dic[0] = 0
dic[1] = 0

# 특정 종이를 확인할 시작점 + 종이 크기 + 그 종이 종류

def cut(x, y, size, num):
    if size == 1:
        dic[num] += 1
        return
    flag = True
    for i in range(x, x + size):
        if not flag: break
        for j in range(y, y + size):
            if arr[i][j] != num:
                flag = False
                break
    if flag:
        dic[num] += 1
    else:
        l = size // 3
        for i in range(3):
            for j in range(3):
                cut(x+i*l, y+j*l, l, arr[x+i*l][y+j*l])

cut(0,0,n,arr[0][0])
for i in dic.values():
    print(i)