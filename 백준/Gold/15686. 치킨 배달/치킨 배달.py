n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
chickens = []
houses = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2: chickens.append((i,j))
        elif arr[i][j] == 1: houses.append((i,j))
# 최소 치킨 거리
ans = float('inf')

def get_dis(combinations):
    # m의 조합에서 도시 치킨 거리 구하기
    total = 0
    for hx,hy in houses:
        # 각 집의 치킨 거리
        cd = float('inf')
        for cx,cy in combinations:
            cd = min(cd, abs(cx-hx) + abs(cy-hy))
        total += cd
    return total

# idx = 치킨집 순회하는 포인터, comb는 치킨집 조합
def dfs(idx,comb):
    global ans
    if m < len(comb):
        return
    # 치킨집을 모두 순회했을 때
    if idx == len(chickens):
        # 고른 치킨 집의 개수가 m개라면
        if len(comb) == m:
            # 도시의 치킨 거리 계산 후, ans와 비교
            ans = min(ans, get_dis(comb))
        return
    # 치킨집 포함
    dfs(idx+1, comb + [chickens[idx]])
    # 치킨집 안 포함
    dfs(idx+1, comb)
dfs(0,[])
print(ans)