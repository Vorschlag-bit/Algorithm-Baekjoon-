def check(x,y,n):
    return 0 <= x <= n and 0 <= y <= n

# x = 행, y = 열
def check_c(x,y,col,bor,n):
    # '기둥'
    # 1. 바닥 위에 있기
    if y == 0:
        return True
    # 2. 보의 한 쪽 끝 부분 위에 있기
    # 보의 오른 끝에 위치한 건지 확인
    if bor[x][y]:
        return True
    # 보의 왼 끝에 위치한 건지 확인
    elif check(x-1,y,n) and bor[x-1][y]:
        return True
    # 3. 다른 기둥 위에 있기
    if y > 0 and col[x][y-1]:
        return True
    return False

def check_b(x,y,col,bor,n):
    # '보'
    # 설치할 경우, (x,y),(x+1,y)에 설치해야 함
    # 1. 한쪽 끝 부분이 기둥 위에 있기
    # 오른 끝
    if check(x+1,y-1,n) and col[x+1][y-1]:
        return True
    # 왼 끝
    elif col[x][y-1]:
        return True
    # 2. 양쪽 끝이 다른 보와 동시에 연결
    if bor[x-1][y] and check(x+1,y,n) and bor[x+1][y]:
        return True
    return False

def solution(n, build_frame):
    ans = []
    # 기둥
    col = [[False] * (n+1) for _ in range(n+1)]
    # 보
    bor = [[False] * (n+1) for _ in range(n+1)]
    # '보'
    # 1. 한쪽 끝 부분이 기둥 위에 있기
    # 2. 양쪽 끝이 다른 보와 동시에 연결
    
    # bf -> x,y,a,b
    # x,y는 기둥,보를 설치/삭제할 좌표(가로 세로)
    # a = 설치/삭제할 구조물 종류(0=기둥,1=보)
    # b = 0 - 삭제, 1 - 설치
    # 구조물은 교차점 좌표를 기준으로 보는 오른쪽, 기둥은 위쪽 방향으로 설치/삭제를 진행
    
    # 1000 * 10000
    
    for (x,y,a,b) in build_frame:
        # 기둥
        if a == 0:
            # 설치
            if b == 1:
                if check_c(x,y,col,bor,n): 
                    col[x][y] = True
            # 삭제
            else:
                col[x][y] = False
                # 모든 기둥 혹은 보가 조건 만족하는지 체크
                flag = True
                for i in range(n+1):
                    for j in range(n+1):
                        if col[i][j]:
                            if not check_c(i,j,col,bor,n):
                                flag = False
                                break
                        if bor[i][j]:
                            if not check_b(i,j,col,bor,n):
                                flag = False
                                break
                    if not flag: break
                # 모든 기본 or 보가 조건 만족하지 않으면 삭제 불가
                if not flag: 
                    col[x][y] = True
        # 보
        else:
            # 설치
            if b == 1:
                if check_b(x,y,col,bor,n):
                    bor[x][y] = True
            # 삭제
            else:
                bor[x][y] = False
                flag = True
                for i in range(n+1):
                    for j in range(n+1):
                        if bor[i][j]:
                            if not check_b(i,j,col,bor,n):
                                flag = False
                                break
                        if col[i][j]:
                            if not check_c(i,j,col,bor,n):
                                flag = False
                                break
                    if not flag: break
                if not flag:
                    bor[x][y] = True
    # x,y 좌표가 모두 같은 경우 기둥이 보보다 앞에 와야 함
    for i in range(n+1):
        for j in range(n+1):
            if col[i][j]: ans.append([i,j,0])
            if bor[i][j]: ans.append([i,j,1])
    return ans