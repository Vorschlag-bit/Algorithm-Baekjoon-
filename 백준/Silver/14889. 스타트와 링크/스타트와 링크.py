# 스타트팀과 링크팀의 능력 차이의 최솟값
# arr[i][j] + arr[j][i]를 저장해두고
# status = [4, 6, 3, 10] <- 정확히 반으로 나눴을 때, 차이가 최소인 경우의 수 찾기
# nC(n/2)의 경우의 수에서 최소의 차 찾기
n = int(input())
team = [i for i in range(n)]
arr = [list(map(int, input().split())) for _ in range(n)]
# 선수 번호는 반드시 -1하기
# 여전히 nC(n/2)의 (1,2,3...)에서 팀을 반으로 나누고, 그 팀에서 nC(n/2)C2를 통해서 팀원 2명 당 포인트를 계산해서 더하기
# 중복을 허용하는 조합
ans = 101
def getDiff(t1):
    t2 = [i for i in range(n) if i not in t1]
    t1P = 0
    t2P = 0

    for i in t1:
        for j in t1:
            if i != j:
                t1P += arr[i][j]
    for i in t2:
        for j in t2:
            if i != j:
                t2P += arr[i][j]
    return abs(t1P - t2P)

def backtrack(idx, selected):
    global ans

    if len(selected) == n//2:
        minD = getDiff(selected)
        ans = min(ans, minD)
        return
    
    if idx == n:
        return
    
    backtrack(idx+1, selected)
    backtrack(idx+1, selected + [idx])

backtrack(0,[])
print(ans)