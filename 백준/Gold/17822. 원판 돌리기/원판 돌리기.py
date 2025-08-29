from sys import stdin as input
n,m,t = map(int,input.readline().split())
arr = [[0] * m for _ in range(n+1)]
# directions = [(0,1),(1,0),(0,-1),(-1,0)]
for i in range(1,n+1):
    numbers = list(map(int,input.readline().split()))
    for j in range(m):
        arr[i][j] = numbers[j]
cmd = []
for _ in range(t):
    # x번 원판, d 방향(0 -> 시계, 1 -> 반시계), k번 회전
    x,d,k = map(int,input.readline().split())
    cmd.append((x,d,k))

for i in range(t):
    num,d,k = cmd[i]
    # num배수인 번호 원판 돌리기
    # arr[i][0]은 항상 맨 위, 시계방향으로 인덱스 증가
    for v in range(1,100):
        # 배수 넘으면 break
        idx = v * num
        if idx > n: break
        l = len(arr[idx])
        copy = [0] * l
        # 시계방향
        if d == 0:
            for index,value in enumerate(arr[idx]):
                nxt = (index+k) % l
                copy[nxt] = value
            arr[idx] = copy
        # 반시계 방향
        else:
            for index,value in enumerate(arr[idx]):
                nxt = (index-k) % l
                copy[nxt] = value
            arr[idx] = copy
    # 원판에 인접하면서 수가 같은 거 판별    
    flag = False
    # 모든 원판 돌면서 판별
    s = set()
    for r in range(1,n+1):
        for c in range(m):
            # 0이면 무시
            if arr[r][c] == 0: continue
            # 자신과 같은 번호면서 인접한 원판 조사
            prev = (c-1) % m
            nxt = (c+1) % m
            if arr[r][prev] == arr[r][c]:
                flag = True
                s.add((r,c))
                s.add((r,prev))
            if arr[r][nxt] == arr[r][c]:
                flag = True
                s.add((r,c))
                s.add((r,nxt))
            # 자신과 같은 열이면서 +-1인 행조사
            prev = r - 1
            nxt = r + 1
            if prev >= 1 and arr[prev][c] == arr[r][c]:
                flag = True
                s.add((r,c))
                s.add((prev,c))
            if nxt <= n and arr[nxt][c] == arr[r][c]:
                flag = True
                s.add((r,c))
                s.add((nxt,c))
    # flag가 True면 지우기
    if flag:
        for x,y in s:
            arr[x][y] = 0
    else:
        # False면 원판별 평균 구하기
        cnt = 0
        avg = 0
        for r in range(1,n+1):
            for c in range(m):
                if arr[r][c] == 0: continue
                avg += arr[r][c]
                cnt += 1
        if cnt > 0:
            avg = avg / cnt
            for r in range(1,n+1):
                for c in range(m):
                    if arr[r][c] == 0: continue
                    if arr[r][c] > avg: arr[r][c] -= 1
                    elif arr[r][c] < avg: arr[r][c] += 1

ans = 0
for i in range(1,n+1):
    ans += sum(arr[i])
print(ans)