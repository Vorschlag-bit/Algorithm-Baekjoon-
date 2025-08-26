from sys import stdin as input
r,c,k = map(int,input.readline().split())
r -= 1
c -= 1
arr = [list(map(int,input.readline().split())) for _ in range(3)]
ro = 3
co = 3

def cir_r(arr,ro,co):
    new = []
    new_c = 0
    for i in range(ro):
        cnt = dict()
        for num in arr[i]:
            if num == 0: continue
            cnt[num] = cnt.get(num,0) + 1
        # 등장 횟수가 커지는 순, 여러 개라면 수 오름차순
        pair = sorted(cnt.items(), key=lambda x: (x[1],x[0]))
        # 최대 길이
        flat = []
        for a,b in pair:
            flat.append(a)
            flat.append(b)
        if len(flat) > 100:
            flat = flat[:100]
        new.append(flat)
        new_c = max(new_c, len(flat))
    new_arr = [[0] * new_c for _ in range(ro)]
    for i in range(len(new)):
        row = new[i]
        for j in range(len(row)):
            new_arr[i][j] = row[j]
    return new_arr,ro,new_c

def cir_c(arr,ro,co):
    new = []
    new_r = 0
    for j in range(co):
        cnt = dict()
        for i in range(ro):
            if arr[i][j] == 0: continue
            cnt[arr[i][j]] = cnt.get(arr[i][j],0) + 1
        pair = sorted(cnt.items(), key=lambda x: (x[1],x[0]))
        flat = []
        for a,b in pair:
            flat.append(a)
            flat.append(b)
        if len(flat) > 100:
            flat = flat[:100]
        new_r = max(new_r, len(flat))
        new.append(flat)
    new_arr = [[0] * co for _ in range(new_r)]
    for j in range(len(new)):
        cols  = new[j]
        for i in range(len(cols)):
            new_arr[i][j] = cols[i]
    return new_arr,new_r,co

time = 0
while time <= 100:
    if r < ro and c < co and arr[r][c] == k:
        print(time)
        break
    if time == 100:
        print(-1)
        break
    # 행연산
    if ro >= co:
        arr,ro,co = cir_r(arr,ro,co)
    # 열연산
    else:
        arr,ro,co = cir_c(arr,ro,co)
    time += 1