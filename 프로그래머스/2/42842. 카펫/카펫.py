def solution(b, y):
    ans = []
    size = b + y
    # y = 6 * 4(가로,세로)라 가정하면
    # (a+2)*2 + b*2 = brown가 가능하다면 정답
    # (a+2),(b+2)
    yellow = []
    for i in range(1,y+1):
        if y % i == 0:
            yellow.append((i,y//i))
    for x,y in yellow:
        if (x+2)*2+y*2 == b:
            ans.append(y+2)
            ans.append(x+2)
            break
    return ans