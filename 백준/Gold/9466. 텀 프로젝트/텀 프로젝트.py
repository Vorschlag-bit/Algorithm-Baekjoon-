import sys
from sys import stdin as input
sys.setrecursionlimit(10**6)  # 재귀 제한 증가
t = int(input.readline().rstrip())

def dfs(i):
    global ans, team
    visit[i] = True
    # 팀원 배열에 추가
    team.append(i)
    # i가 고른 팀원
    select = arr[i]
    # 방문한 적이 없다면
    if not visit[select]:
        dfs(select)
    # 방문한 적이 있다면
    else:
        # 팀원 배열에 선택한 사람이 있다면 사이클 발견
        # 사이클 시작점부터 끝까지가 한 팀
        if select in team:
            ans += len(team[team.index(select):])
for _ in range(t):
    n = int(input.readline().rstrip())
    arr = [0] + list(map(int, input.readline().split()))
    visit = [False for _ in range(n + 1)]
    # 팀을 찾은 사람 수
    ans = 0
    for i in range(1, n+1):
        if not visit[i]:
            # 사이클이 들어갈 팀원 배열
            team = []
            dfs(i)
    print(n - ans)