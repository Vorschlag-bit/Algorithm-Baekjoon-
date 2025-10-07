def solution(alp, cop, problems):
    ans = 0
    # 모든 문제들을 1번 이상 풀 필요는 x
    # 최대 코딩력 증가량 + 시간
    # 최대 알고력 증가량 + 시간을 각각 관리
    max_cop,max_alg = max(p[1] for p in problems), max(p[0] for p in problems)
    alp = min(alp,max_alg)
    cop = min(cop,max_cop)
    # dp[i][j] = 알고 i와 코딩 j를 갖추는데 필요한 최소 시간
    dp = [[float('inf')] * (max_cop+1) for _ in range(max_alg+1)]
    dp[alp][cop] = 0
    for i in range(alp,max_alg+1):
        for j in range(cop,max_cop+1):
            # 만약 1증가한 게 max이하일 경우 기존값과 더 작은 값을 넣기
            if i + 1 <= max_alg:
                dp[i+1][j] = min(dp[i+1][j],dp[i][j]+1)
            if j + 1 <= max_cop:
                dp[i][j+1] = min(dp[i][j+1],dp[i][j]+1)
            # 풀 수 있는 문제들을 풀면서 최소 변경
            for alp_req,cop_req,alp_rwd,cop_rwd,cost in problems:
                if alp_req <= i and cop_req <= j:
                    # i + alp_rwd가 max보다 클 수 있으므로
                    a = min(i+alp_rwd,max_alg)
                    c = min(j+cop_rwd,max_cop)
                    dp[a][c] = min(dp[a][c], dp[i][j] + cost)
    # 어떤 문제를 풀 때 부족한 능력에 대해서 필요한 전체 시간 계산
    # 1/1씩 증가할 때랑 최대 코딩력/시간으로 늘릴 때 비교
    # 
    return dp[max_alg][max_cop]