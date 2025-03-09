from sys import stdin as input

n = int(input.readline().rstrip())

arr = [list(map(int, input.readline().split())) for _ in range(n)]
dic = dict()
dic[0] = 0
dic[1] = 0
# x, y, 길이, 종이색
def cut(x,y,size,color):
    if size == 1:
        dic[color] += 1
        return
    flag = True
    for i in range(x, x+size):
        if not flag: break
        for j in range(y, y+size):
            if arr[i][j] != color:
                flag = False
                break
    if flag:
        dic[color] += 1
    else:
        # 4토막 내기
        l = size // 2
        for i in range(2):
            for j in range(2):
                cut(x+l*i,y+l*j,l,arr[x+l*i][y+l*j])
cut(0,0,n,arr[0][0])
for v in dic.values():
    print(v)