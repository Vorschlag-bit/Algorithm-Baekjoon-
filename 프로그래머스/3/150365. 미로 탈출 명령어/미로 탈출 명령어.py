def solution(n, m, x, y, r, c, k):
    # x,y -> r,c 이동 거리가 총 k여야 한다. (이 때 x,y,r,c 포함 같은 격자 중복 방문 허용)
    # l: 왼쪽, r: 오른쪽, u: 위, d:아래
    # 미로 탈출 경로 중 사전 순으로 가장 빠른 경로로 탈출(d,l,r,u 순)
    directions = [(1,0),(0,-1),(0,1),(-1,0)]
    dkey = {1:'l',2:'r',3:'u',0:'d'}
    # s = 출발, e = 탈출
    # n,m <= 50
    # 0-based
    x,y,r,c = x-1,y-1,r-1,c-1
    ans = ''
    # dis가 k보다 크거나 남은 거리만큼 왔다갔다(짝수 이동)가 불가능하면 impossible
    dis = abs(r-x) + abs(c-y)
    if dis > k or (k-dis) % 2 != 0:
        return 'impossible'
    
    def check(a,b): return 0 <= a < n and 0 <= b < m

    # 현재 위치
    cx,cy = x,y
    for s in range(k):
        # 남은 시간
        remain = k - s
        
        for i,d in enumerate(directions):
            nx,ny = cx + d[0], cy + d[1]
            # 격자를 벗어나지 않고 거리가 줄어들고 이동한 좌표에서 도착지까지 k초로 도착할 수 있다면
            if check(nx,ny):
                # 새로운 거리와 시간
                dis = abs(r-nx) + abs(c-ny)
                nr = remain - 1
                # 시간 안에 도착이 가능하고 짝수인지 판별
                if dis <= nr and (nr-dis) % 2 == 0:
                    ans += dkey[i]
                    cx,cy = nx,ny
                    break
    
    return ans