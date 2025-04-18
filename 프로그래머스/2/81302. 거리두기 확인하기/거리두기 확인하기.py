from itertools import combinations as comb
def solution(places):
    ans = []
    for place in places:
        person = []
        arr = [[''] * 5 for _ in range(5)]
        for i,r in enumerate(place):
            for j,c in enumerate(r):
                if c == 'P':
                    person.append((i,j))
                arr[i][j] = c
        flag = True
        for p1,p2 in comb(person, 2):
            x1,y1 = p1[0],p1[1]
            x2,y2 = p2[0],p2[1]
            dis = abs(x1-x2) + abs(y1-y2)
            if dis == 1:
                flag = False
                break
            elif dis == 2:
                if x1 == x2:
                    if arr[x1][(y1+y2)//2] != 'X':
                        flag = False
                        break
                elif y1 == y2:
                    if arr[(x1+x2)//2][y1] != 'X':
                        flag = False
                        break
                else:
                    if arr[x1][y2] != 'X' or arr[x2][y1] != 'X':
                        flag = False
                        break
                    
            
        ans.append(1) if flag else ans.append(0)
    
    return ans