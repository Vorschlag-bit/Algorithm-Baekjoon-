def solution(N, stages):
    # 각 스테이지별 도달했으나 클리어하지 못한 사용자 수
    not_clear = [0] * (N + 2)
    for stage in stages:
        not_clear[stage] += 1
    
    # 각 스테이지에 도달한 사용자 수
    reach = [0] * (N + 2)
    for i in range(1, N + 1):
        # i번 스테이지에 도달한 사용자 = i번 스테이지에 머물러 있는 사용자 + i보다 높은 스테이지에 있는 사용자
        reach[i] = sum(not_clear[i:])
    
    # 각 스테이지의 실패율 계산
    failure_rates = []
    for i in range(1, N + 1):
        if reach[i] == 0:  # 스테이지에 도달한 유저가 없는 경우
            failure_rates.append((i, 0))
        else:
            failure_rates.append((i, not_clear[i] / reach[i]))
    
    # 실패율이 높은 스테이지부터 내림차순으로 정렬
    failure_rates.sort(key=lambda x: (-x[1], x[0]))
    
    # 스테이지 번호만 반환
    return [stage for stage, _ in failure_rates]