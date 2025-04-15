def solution(alp, cop, problems):
    # dp[i][j] = al(i), co(j)의 능력을 갖추는 데 드는 소요시간
    t_al = max(p[0] for p in problems)
    t_co = max(p[1] for p in problems)
    
    # 초기값이 목표보다 큰 경우 목표로 맞추기
    alp = min(alp, t_al)
    cop = min(cop, t_co)
    
    dp = [[float('inf')] * (t_co + 1) for _ in range(t_al + 1)]
    dp[alp][cop] = 0
    
    for i in range(alp, t_al+1):
        for j in range(cop, t_co+1):
            
            if i + 1 <= t_al:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            
            if j + 1 <= t_co:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    a = min(t_al, i + alp_rwd)
                    b = min(t_co, j + cop_rwd)
                    dp[a][b] = min(dp[a][b], dp[i][j] + cost)
    
    return dp[t_al][t_co]