import sys

m, n = map(int, sys.stdin.readline().strip().split())
x, y = 0, 0 # 현 좌표
cur_dir = 0 # 현재 방향(0:동, 1:북, 2:서, 3:남)
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# 좌표 유효성 검사
def valid(next_x, next_y):
    return 0 <= next_x <= m and 0 <= next_y <= m

def check(command, dir):
    global x, y, cur_dir
    match command:
        case "TURN":
            if dir == 0: # 왼쪽으로 90
                cur_dir = (cur_dir + 1) % 4
            else:
                cur_dir = (cur_dir - 1) % 4
        case "MOVE":
            dx, dy = move[cur_dir]
            next_x = x + dx * dir
            next_y = y + dy * dir
            if valid(next_x, next_y):
                x, y = next_x, next_y
                return True
            return False
    return True

for i in range(n):
    command, dir = sys.stdin.readline().strip().split()
    dir = int(dir)
    if not check(command, dir):
        print(-1)
        break
else:
    print(x, y)