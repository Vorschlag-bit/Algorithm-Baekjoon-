def solution(dirs):
    ans = 0
    dic = {'U':(-1,0,0), 'D':(1,0,1), 'R':(0,1,2), 'L':(0,-1,3)}
    arr = [[[0]*11 for _ in range(11)] for _ in range(4)]
    x, y = 5, 5

    for d in dirs:
        dx, dy, cd = dic[d]
        nx, ny = x + dx, y + dy

        if 0 <= nx < 11 and 0 <= ny < 11:
            if arr[cd][x][y] == 0 and arr[cd^1][nx][ny] == 0:
                ans += 1
            arr[cd][x][y] = 1
            arr[cd^1][nx][ny] = 1
            x, y = nx, ny  # 마지막에 이동
    return ans