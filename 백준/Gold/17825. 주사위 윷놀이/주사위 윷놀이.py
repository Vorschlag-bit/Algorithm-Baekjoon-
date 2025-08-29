from sys import stdin as input
dice = list(map(int,input.readline().split()))
# idx칸에서 +1 이동할 경우 갈 수 있는 칸(32=도착)
graph = [[1],[2],[3],[4],[5],
        [6,21],[7],[8],[9],[10],
        [11,27],[12],[13],[14],[15],
        [16,29],[17],[18],[19],[20],
        # 20  21   22   23   24
        [32],[22],[23],[24],[25],
        # 25  26  27   28   29
        [26],[20],[28],[24],[30],
        # 30  31  32   33   34
        [31],[24],[32]]
score = [0,2,4,6,8,
        10,12,14,16,18,
        20,22,24,26,28,
        30,32,34,36,38,
        #20
        40,13,16,19,25,
        #25 26 27 28 29
        30,35,22,24,28,
        27,26,0]
ans = 0

def dfs(depth, s, h):
    global ans
    if depth == 10:
        ans = max(ans, s)
        return
    
    for i in range(4):
        # dice만큼 움직일 말의 인덱스
        cur = h[i]
        # 현재 말이 2갈래길인지 파악 후 확실하게 이동하기
        if len(graph[cur]) > 1:
            cur = graph[cur][1]
        else: cur = graph[cur][0]
        # 위에서 한 번 움직였으니 -1
        for num in range(1,dice[depth]):
            cur = graph[cur][0]
        # 목적지 도착 or 도착한 칸에 이미 말이 존재한 게 아니라면 dfs
        if cur == 32 or (cur < 32 and cur not in h):
            ex = h[i]
            h[i] = cur
            dfs(depth+1,s+score[cur],h)
            h[i] = ex
dfs(0,0,[0,0,0,0])
print(ans)