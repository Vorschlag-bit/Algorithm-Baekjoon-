from sys import stdin as input
# 파이어볼은 질량,방향,속도,위치가 존재
# 파이어볼 방향은 칸과 인접한 아래의 8개 방향
directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
# 모든 파이어볼이 자신의 방향d로 속력s만큼 이동, 이동 중 같은 칸에 여러 파이어볼 존재 가능
# 이동을 마치고, 같은 칸 2개 이상의 파이어볼 존재 시 파이어볼은 모두 하나로 합쳐짐
# 파이어볼은 4개로 나눠짐. 질량 = (합쳐진 질량)/5, 속력 = (합쳐진 파이어볼 속력) / 파이어볼 개수
# 합쳐진 파이어볼 방향이 모두 홀수/짝수면 방향은 0,2,4,6 홀짝 섞이면 1,3,5,7
# 질량이 0인 파이어볼은 사라짐.
# k번 명령 후, 남아있는 파이어볼 질량
n,m,k = map(int,input.readline().split())
# 3차원
fireballs = []
for _ in range(m):
    r,c,m,s,d = map(int,input.readline().split())
    # 0-based
    r -= 1
    c -= 1
    fireballs.append((r,c,m,s,d))
# 0번 행/열은 n-1행/열과 연결되어 있다.

for _ in range(k):
    arr = [[[] for _ in range(n)] for _ in range(n)]    
    for fireball in fireballs:
        x,y,m,s,d = fireball
        nd = directions[d]
        nx,ny = (x+nd[0]*s) % n, (y+nd[1]*s)%n
        arr[nx][ny].append((m,s,d))
    # 새로운 파이어볼 리스트
    new_fireball = []
    for i in range(n):
        for j in range(n):
            if len(arr[i][j]) == 1:
                m,s,d = arr[i][j][0]
                new_fireball.append((i,j,m,s,d))
            elif len(arr[i][j]) > 1:
                # 파이어볼 2개 이상이면 합치고 나누기
                w = 0
                speed = 0
                odd = False
                even = False
                for t in arr[i][j]:
                    m,s,d = t
                    w += m
                    speed += s
                    if d % 2 == 0: even = True
                    else: odd = True
                eachW = w // 5
                # 나누는 질량 0이면 continue
                if eachW == 0: continue
                eachS = speed // len(arr[i][j])
                direction = [1,3,5,7] if odd and even else [0,2,4,6]
                for nd in direction:
                    new_fireball.append((i,j,eachW,eachS,nd))
    fireballs = new_fireball

ans = sum(fb[2] for fb in fireballs)
print(ans)