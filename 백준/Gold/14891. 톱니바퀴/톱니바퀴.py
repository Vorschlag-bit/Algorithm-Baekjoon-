# 톱니8개로 이뤄진 바퀴 4개
clockwork = [list(map(int, input().rstrip())) for _ in range(4)]
# n=0, s=1
k = int(input().rstrip())
# command = [[태엽번호, 방향]...], cw = 1, ccw = -1
commands = [list(map(int, input().split())) for _ in range(k)]
ans = 0

for com in commands:
    no,d = com[0]-1,com[1]
    rotation = [0,0,0,0]
    rotation[no] = d
    # 왼쪽 방향 결정
    for i in range(no,0,-1):
        if clockwork[i-1][2] != clockwork[i][6]:
            rotation[i-1] = -rotation[i]
        else: break
    # 오른쪽 방향 결정
    for i in range(no,3):
        if clockwork[i][2] != clockwork[i+1][6]:
            rotation[i+1] = -rotation[i]
        else: break
    # 회전 시작
    for i in range(4):
        if rotation[i] == 1:
            t = clockwork[i][-1]
            clockwork[i] = [t] + clockwork[i][:7]
        elif rotation[i] == -1:
            h = clockwork[i][0]
            clockwork[i] = clockwork[i][1:] + [h]
        else: continue
for idx,clock in enumerate(clockwork):
    # 12시가 s(1)면 2**(idx + 1)
    if clock[0] == 1:
        ans += 2**(idx)
print(ans)