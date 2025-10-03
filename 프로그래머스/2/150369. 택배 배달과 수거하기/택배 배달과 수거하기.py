def solution(cap, n, deli, pick):
    ans = 0
    # 트럭에는 재활용 택배 상자 최대 cap개 싣기 가능.
    # 각 집에 배달하면서 빈 재활용 상자 수고
    # 트럭 하나로 모든 배달과 수거를 마치고 올 때 최단 거리
    l = len(deli)
    
    # 배달과 수거가 모두 0이 될 때까지 반복
    d = 0 # 남은 배달
    p = 0 # 남은 수거
    
    for i in range(l-1,-1,-1):
        d += deli[i]
        p += pick[i]
        
        # 현재 집 idx에서 처리할 게 남을 때까지 왕복
        while d > 0 or p > 0:
            d -= cap
            p -= cap
            ans += (i+1) * 2
    
    return ans