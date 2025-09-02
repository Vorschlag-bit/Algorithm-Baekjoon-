from sys import stdin as input
from collections import deque
directions = [(0,1),(1,0),(0,-1),(-1,0)]
# 2n의 배열, 원형으로 한 칸씩 이동
# idx 0 = 올리는 위치, idx n - 1 = 내리는 위치
# 로봇을 올리거나 이동하면 해당 칸 내구도 1감소
# 1. 벨트가 칸 위의 로봇과 함께 1칸씩 앞으로 이동
# 2. 가장 먼저 올라간 로봇부터 벨트 회전 방향으로 1칸 이동 가능 시 이동. 안 되면 가만히
# 3. 로봇이 이동하려면 빈 칸이고 내구도가 1이상이여야 함
# 4. 올리는 위치에 내구도가 0이 아니면 올리는 위치에 로봇 올리기
# 5. 내구도 0인 칸의 개수가 k가 이상이라면 사이클 종료 아니면 1번부터 반복
ans = 1
n,k = map(int,input.readline().split())
# 로봇 번호를 저장할 벨트 arr
robot_arr = [0 for _ in range(2*n)]
r = 1
arr = list(map(int,input.readline().split()))
l = 2*n
while True:
    # 내구도 배열과 로봇 배열을 동시에 이동
    new_arr = [0] * n * 2
    new_robot = [0] * n * 2
    move_robot = []
    for i in range(2*n):
        if arr[i] == 0: cnt += 1
        nxt = (i+1) % l
        new_arr[nxt] = arr[i]
        # 컨베이어 이동으로 n-1에 도착하면 그대로 내리기
        if nxt != n-1:
            new_robot[nxt] = robot_arr[i]
        # 빈 칸이 아니라면, 로봇 번호와 새로운 idx 저장
        if robot_arr[i] != 0 and nxt != n-1:
            move_robot.append((robot_arr[i],nxt))
    # 덮어씌우기
    arr = new_arr
    robot_arr = new_robot
    # 가장 먼저 올라간 로봇부터 벨트 회전 방향으로 1칸 이동
    move_robot.sort(key=lambda x: (x[0]))
    for num,idx in move_robot:
        nxt = (idx + 1) % l
        # 내구도 > 0 and 로봇 없어야 함
        if arr[nxt] > 0 and robot_arr[nxt] == 0:
            arr[nxt] -= 1
            robot_arr[idx] = 0
            # 내리는 위치라면 그냥 패스
            if nxt == n-1: robot_arr[nxt] = 0
            else: robot_arr[nxt] = num
    # 올리는 위치 = 0, 내리는 위치 = n-1
    if arr[0] > 0:
        arr[0] -= 1
        robot_arr[0] = r
        r += 1
    cnt = 0
    for i in range(l):
        if arr[i] == 0: cnt += 1
    if cnt >= k: break
    ans += 1
print(ans)