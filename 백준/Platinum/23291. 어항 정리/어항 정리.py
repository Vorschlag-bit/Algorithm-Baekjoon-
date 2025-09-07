from sys import stdin as input

n, k = map(int, input.readline().split())
arr = list(map(int, input.readline().split()))

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
ans = 0

def fill_zero(arr):
    # 바닥어항 길이
    b = len(arr[-1])
    # 마지막항 제외하고
    for a in arr[:-1]:
        if len(a) < b: 
            a.extend([0] * (b - len(a)))

def control(arr):
    r = len(arr)
    change = []
    for x in range(r):
        for y in range(len(arr[x])):
            for d in directions:
                nx, ny = x + d[0], y + d[1]
                if 0 <= nx < r and 0 <= ny < len(arr[nx]):
                    # 현재 칸 물고기 수
                    cur = arr[x][y]
                    # 비교군
                    nxt = arr[nx][ny]
                    if cur > nxt:
                        diff = (cur - nxt) // 5
                        if diff > 0:
                            change.append((x, y, -diff))
                            change.append((nx, ny, diff))
    # 동시에 반영
    for x, y, diff in change:
        arr[x][y] += diff

def rearrange(arr):
    # 교체할 배열(다시 90도 돌리고 행 채우기)
    new_arr = []
    for j in range(len(arr[0])):
        for i in range(len(arr)-1,-1,-1):
            new_arr.append(arr[i][j])
    for i in range(len(arr[0]),len(arr[-1])):
        new_arr.append(arr[-1][i])

    return new_arr

while True:
    # 최대 물고기
    max_f = max(arr)
    # 최소 물고기
    min_f = min(arr)
    if max_f - min_f <= k:
        break
    for i in range(len(arr)):
        if arr[i] == min_f: 
            arr[i] += 1
    
    # 어항 올리기
    # 시작 배열
    c = [arr[0]]
    temp = arr[1:]
    arr = [c, temp]
    
    while True:
        if len(arr) > (len(arr[-1]) - len(arr[0])): break
        # 90도 돌릴 배열
        temp = []
        r = len(arr)
        c = len(arr[0])
        for i in range(r):
            t = []
            for j in range(c):
                t.append(arr[i][j])
            temp.append(t)
        # 어항 밑바닥만 남기고
        arr = arr[-1][len(temp[0]):]
        # 90도 회전
        temp = list(map(list, zip(*temp[::-1])))
        # 밑바닥깔기
        temp.append(arr)
        # 교체
        arr = temp
    
    # 물고기 수 조절
    control(arr)
    
    # 어항 일렬로 놓기
    arr = rearrange(arr)
    
    # 다시 공중부양 작업
    # 1회차
    half = len(arr) // 2
    cut = arr[:half]
    # 180회전
    cut.reverse()
    arr = arr[half:]
    new_arr = []
    new_arr.append(cut)
    new_arr.append(arr)
    arr = new_arr
    
    # 2회차
    half = len(arr[0]) // 2
    # 위에 쌓일 거
    top = []
    # 아래에 깔릴 거
    bottom = []
    for i in range(len(arr)):
        top.append(arr[i][:half])
        bottom.append(arr[i][half:])
    # 180회전
    top = [a[::-1] for a in top[::-1]]
    temp = []
    for t in top:
        temp.append(t)
    for b in bottom:
        temp.append(b)
    arr = temp
    
    # 다시 물고기 조절
    control(arr)
    
    # 다시 일렬로 놓기
    arr = rearrange(arr)
    ans += 1

print(ans)