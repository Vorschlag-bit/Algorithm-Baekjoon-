from sys import stdin as input
# 벽장의 개수
n = int(input.readline())
# 초반에 열린 벽장의 번호(1-based)
f,s = map(int,input.readline().split())
# 사용할 벽장의 개수
m = int(input.readline())
l = []
for _ in range(m):
    l.append(int(input.readline()))

ans = float('inf')

# 현재 풀 idx, 열린 문 번호1, 열린 문 번호2
def solve(idx,o1,o2,s):
    global ans
    # 가지치기
    if s >= ans: return

    if idx == len(l):
        ans = min(ans,s)
        return
    
    t = l[idx]
    # t를 열기 위한 최소 횟수
    c1 = abs(t - o1)
    c2 = abs(t - o2)

    # 둘 다 시도
    solve(idx+1,o1,t,s + c2)
    solve(idx+1,o2,t,s + c1)

solve(0,f,s,0)
print(ans)