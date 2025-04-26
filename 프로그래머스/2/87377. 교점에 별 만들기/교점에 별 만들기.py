from itertools import combinations as comb
def solution(line):
    ans = []
    l = set()
    for c in comb(line,2):
        a,b,e = c[0]
        c,d,f = c[1]
        div = a*d-b*c
        if div == 0: continue
        x = (b*f-e*d)/div
        y = (e*c-a*f)/div
        if x == int(x) and y == int(y): l.add((int(x),int(y)))
    maxX,maxY = -float('inf'),-float('inf')
    minX,minY = float('inf'),float('inf')
    for x,y in l:
        maxX = max(x,maxX)
        maxY = max(y,maxY)
        minX = min(x,minX)
        minY = min(y,minY)
    xsize = maxX - minX
    ysize = maxY - minY
    # 0으로 상대위치 바꾸기 (0,0), (0,2)
    arr = [['.'] * (xsize+1) for _ in range(ysize+1)]
    for x,y in l:
        arr[maxY - y][x - minX] = '*'
    for i in range(len(arr)):
        row = arr[i]
        ans.append(''.join(row))
    return ans