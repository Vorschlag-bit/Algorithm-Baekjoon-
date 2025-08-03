from collections import defaultdict

def solution(points, routes):
    ans = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    # 목표 번호 = key, 좌표 = value
    p = dict()
    for i, (r, c) in enumerate(points):
        p[i + 1] = (r, c)
    
    # robot 현재 위치
    robot = [list(p[r[0]]) for r in routes]
    
    # robot 목표 리스트
    robot_dest = []
    rs = set()
    for i, r in enumerate(routes):
        dest_list = []
        for j in range(1, len(r)):
            dest_list.append(p[r[j]])
        robot_dest.append(dest_list)
        if len(dest_list) > 0:  # 목적지가 있는 로봇만 활성화
            rs.add(i)
    
    # 초기 위치에서의 충돌 체크
    position = defaultdict(int)
    for i, pos in enumerate(robot):
        k = tuple(pos)
        position[k] += 1
    
    for v in position.values():
        if v > 1:
            ans += 1
    
    # 시뮬레이션
    while len(rs) > 0:
        robot_list = list(rs)
        rs.clear()
        moved_robots = []  # 이번 턴에 움직인 로봇들
        
        # 각 로봇 이동
        for i in robot_list:
            target = robot_dest[i][0]
            cur = robot[i]
            for d in directions:
                nx, ny = cur[0] + d[0], cur[1] + d[1]
                if 0 < nx and 0 < ny and abs(target[0] - nx) + abs(target[1] - ny) < abs(target[0] - cur[0]) + abs(target[1] - cur[1]):
                    robot[i] = [nx, ny]
                    moved_robots.append(i)  # 움직인 로봇 기록
                    break
            if tuple(robot[i]) == target:
                robot_dest[i].pop(0)
            if len(robot_dest[i]) > 0: 
                rs.add(i)
        
        # 이번 턴에 움직인 모든 로봇들로 충돌 체크
        pos = {}
        for r in moved_robots:
            k = tuple(robot[r])
            pos[k] = pos.get(k, 0) + 1
        for v in pos.values():
            if v > 1:
                ans += 1

    return ans