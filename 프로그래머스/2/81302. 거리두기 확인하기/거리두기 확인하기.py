from itertools import combinations
def solution(places):
    answer = []
    
    for r in places:
        p = []
        for x,i in enumerate(r):
            for y,j in enumerate(i):
                if r[x][y] == 'P':
                    p.append((x,y))
        check = True
        for i in combinations(p, 2):
            x1,y1 = i[0][0], i[0][1]
            x2,y2 = i[1][0], i [1][1]
            if abs(x1 - x2) + abs(y1 - y2) <= 2:
                if x1 == x2:
                    if r[x1][(y1+y2)//2] != 'X':
                        check = False
                        break
                elif y1 == y2:
                    if r[(x1+x2)//2][y1] != 'X':
                        check = False
                        break
                else:
                    if r[x1][y2] != 'X' or r[x2][y1] != 'X':
                        check = False
                        break
        answer.append(1 if check else 0)
    return answer