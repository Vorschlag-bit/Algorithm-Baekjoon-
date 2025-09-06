from sys import stdin as input
from collections import deque, defaultdict

# 4 * 4 크기, m마리
directions = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
sharkd = [(-1,0),(0,-1),(1,0),(0,1)]

m, s = map(int, input.readline().split())
fish = defaultdict(list)

for _ in range(m):
    x, y, d = map(int, input.readline().split())
    fish[(x-1, y-1)].append(d-1)

sx, sy = map(int, input.readline().split())
sx -= 1
sy -= 1

smell = [[0] * 4 for _ in range(4)]

def check(x, y):
    return 0 <= x < 4 and 0 <= y < 4

def move_fish(x, y, d, new_fish):
    for i in range(8):
        nd = (d - i) % 8
        nx, ny = x + directions[nd][0], y + directions[nd][1]
        if not check(nx, ny):
            continue
        if (nx, ny) == (sx, sy):
            continue
        if smell[nx][ny] > 0:
            continue
        new_fish[(nx, ny)].append(nd)
        return
    new_fish[(x, y)].append(d)

def get_shark_moves():
    moves = []
    # 3칸 연속 이동의 모든 경우의 수 생성 (4^3 = 64가지)
    for i in range(4):
        for j in range(4):
            for k in range(4):
                moves.append([i, j, k])
    return moves

def simulate_shark_move(moves, new_fish):
    best_count = -1
    best_moves = 1000
    best_path = []
    
    for idx,move_seq in enumerate(moves):
        cx, cy = sx, sy
        path = [(cx, cy)]
        valid = True
        
        # 3칸 연속 이동이 가능한지 확인
        for move_dir in move_seq:
            nx, ny = cx + sharkd[move_dir][0], cy + sharkd[move_dir][1]
            if not check(nx, ny):
                valid = False
                break
            cx, cy = nx, ny
            path.append((cx, cy))
        
        if not valid:
            continue
        
        # 이 경로로 이동했을 때 먹을 수 있는 물고기 수 계산
        eaten_positions = set()
        count = 0
        for pos in path[1:]:  # 시작 위치 제외
            if pos not in eaten_positions and pos in new_fish:
                count += len(new_fish[pos])
                eaten_positions.add(pos)
        
        # 더 많은 물고기를 먹거나, 같은 수면 사전순으로 앞선 경우
        if count > best_count or (count == best_count and idx < best_moves):
            best_count = count
            best_moves = idx
            best_path = path[1:]  # 시작 위치 제외
    
    return best_path

for turn in range(1, s + 1):
    # 1. 물고기 복제
    clone = defaultdict(list)
    for pos, fish_list in fish.items():
        clone[pos] = fish_list[:]
    
    # 2. 물고기 이동
    new_fish = defaultdict(list)
    for pos, fish_list in fish.items():
        for d in fish_list:
            move_fish(pos[0], pos[1], d, new_fish)
    
    # 3. 상어 이동
    moves = get_shark_moves()
    shark_path = simulate_shark_move(moves, new_fish)
    
    if shark_path:
        # 상어가 지나간 칸의 물고기 제거 및 냄새 남기기
        eaten_positions = set()
        for pos in shark_path:
            if pos in new_fish and len(new_fish[pos]) > 0:
                if pos not in eaten_positions:
                    smell[pos[0]][pos[1]] = turn
                    eaten_positions.add(pos)
                new_fish[pos] = []  # 물고기 제거
        
        # 상어 위치 업데이트
        sx, sy = shark_path[-1]
    
    # 4. 2번 전 냄새 제거
    for i in range(4):
        for j in range(4):
            if smell[i][j] == turn - 2:
                smell[i][j] = 0
    
    # 5. 물고기 복제 완료
    for pos, fish_list in clone.items():
        new_fish[pos].extend(fish_list)
    
    fish = new_fish

# 결과 출력
ans = sum(len(fish_list) for fish_list in fish.values())
print(ans)