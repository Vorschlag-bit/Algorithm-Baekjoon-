def solution(places):
    def check(x,y):
        return 0<= x < 5 and 0<= y < 5
    answer = []
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    hx = [-1,-1,1,1]
    hy = [1,-1,-1,1]
    for place in places:
        flag = True
        for i in range(5):
            if not flag:
                break
            for j in range(5):
                if not flag:
                    break
                if place[i][j] == 'P':
                    for d in range(4):
                        nx, ny = i + dx[d], j +dy[d]
                        if check(nx,ny) and place[nx][ny] == 'P':
                            flag = False
                            break
                        ax, by = i + 2*dx[d], j + 2*dy[d]
                        if check(ax,by) and place[ax][by] == 'P' and place[nx][ny] != 'X':
                            flag = False
                            break
                    for d in range(4):
                        mx,my = i + hx[d], j + hy[d]
                        if not check(mx,my): continue
                        if place[mx][my] == 'P':
                            p1 = place[mx][j]
                            p2 = place[i][my]
                            if p1 != 'X' or p2 != 'X':
                                flag = False
                                break
        
        if flag:
            answer.append(1)
        else:
            answer.append(0)
    return answer