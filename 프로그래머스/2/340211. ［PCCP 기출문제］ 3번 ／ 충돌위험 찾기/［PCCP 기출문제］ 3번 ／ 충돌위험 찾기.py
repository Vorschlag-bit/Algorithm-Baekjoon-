from collections import defaultdict
def solution(points, routes):
    ans = 0
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    # 물류센터 번호 - k, 좌표 - v
    p = dict()
    # robot 번호 - k, 다음 목표 좌표 - v
    robot_dest = defaultdict(list)
    rs = set()
    for i,point in enumerate(points):
        p[i+1] = tuple(point)
    # robot 번호 - k, 좌표 - v
    robot = [list(p[r[0]]) for r in routes]
    for idx,r in enumerate(routes):
        each_list = []
        for i in range(1,len(r)):
            each_list.append(p[r[i]])
        robot_dest[idx] = each_list
        rs.add(idx)
    # 시작부터 충돌확인
    position = defaultdict(int)
    for i,r in enumerate(robot):
        k = tuple(r)
        position[k] += 1
    for v in position.values():
        if v > 1: ans += 1
    print(robot_dest)
    while len(rs) > 0:
        moved_robot = []
        robots = list(rs)
        rs.clear()
        for i in robots:
            # i = 로봇 번호
            target = robot_dest[i][0]
            cur = robot[i]
            for d in directions:
                nx,ny = cur[0] + d[0], cur[1] + d[1]
                if 0 < nx and 0 < ny and abs(nx-target[0])+abs(ny-target[1]) < abs(cur[0]-target[0])+abs(cur[1]-target[1]):
                    robot[i] = [nx,ny]
                    moved_robot.append(i)
                    break
            # 도착을 했다면 제거
            if target == tuple(robot[i]):
                robot_dest[i].pop(0)
            # robot_dest[i]가 남았다면 추가
            if len(robot_dest[i]) > 0:
                rs.add(i)
        # 움직인 로봇들만 충돌 계산
        position = defaultdict(int)
        for r in moved_robot:
            k = tuple(robot[r])
            position[k] += 1
        for v in position.values():
            if v > 1: ans += 1
    return ans