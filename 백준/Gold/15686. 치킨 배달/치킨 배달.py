n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
chickens = []
houses = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2: chickens.append((i,j))
        elif arr[i][j] == 1: houses.append((i,j))
# 최소 치킨 거리
min_ch_dis = float('inf')
# 치킨집을 m개의 조합으로 구성하기
comb = []
def combination(l,new_arr,r):
    if l == len(new_arr):
        comb.append(new_arr[:])
        return
    for i in range(r,len(chickens)):
        combination(l,new_arr + [i],i+1)
combination(m,[],0)

# 조합을 돌면서, 각 조합만의 최소 치킨 거리를 구하고, 그 치킨 거리 중 최소가 되는 값이 정답
for c in comb:
    # 도시의 치킨 거리 후보군
    total_chickDis = 0
    for h in houses:
        hx,hy = h[0],h[1]
        # 한 집의 치킨 거리
        cD = 1000
        for ch in c:
            x,y = chickens[ch][0], chickens[ch][1]
            cD = min(cD, abs(hx-x) + abs(hy-y))
        total_chickDis += cD
    min_ch_dis = min(min_ch_dis, total_chickDis)
print(min_ch_dis)