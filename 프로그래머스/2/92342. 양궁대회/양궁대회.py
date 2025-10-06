def solution(n, info):
    # 최적의 배열
    best_a = [0]*11
    # 최대의 차이
    best_d = 0
    
    # 만약 k점에 대해서 a >= b일 경우 a가 점수 획득, a < b면 b가 점수 획득
    # 둘 다 0이면 아무도 점수 획득 x
    # a를 가장 큰 점수 차로 이기기 위해 n발의 화살을 어떤 과녁 점수에 맞혀야 하는지 구하기
    # 가장 큰 점수 차이로 우승할 수 있는 방법이 여러 개일 경우, 가장 낮은 점수를 더 많이 맞힌 경우로 return
    
    def dfs(idx,score,left):
        nonlocal info,best_a,best_d
        # 끝까지 다 점수를 매겼다면
        if idx == -1:
            # 남은 화살 0점에 매기기(복사)
            final_score = score[:]
            final_score[10] += left
            # 점수 계산
            a_total = 0
            b_total = 0
            for i in range(11):
                # 둘 다 0이면 점수 획득 불가
                if info[i] == 0 and final_score[i] == 0: continue
                # 라가 명확하게 어보다 점수가 커야만 함
                elif final_score[i] > info[i]: b_total += 10 - i
                # 다른 모든 경우는 어 점수 획득
                else: a_total += 10 - i
            # 라가 명확하게 이긴 경우
            if b_total > a_total:
                diff = b_total - a_total
                # 최고 차이를 넘거나 더 작은 점수 화살을 많이 맞힌 경우(배열 비교 사용)
                if (diff > best_d or
                   (diff == best_d and best_a[::-1] < score[::-1])):
                    best_d = diff
                    best_a = final_score
            return
        
        # 이 점수 포기
        dfs(idx-1,score,left)
        
        # 이 점수 a보다 많이 넣기(1 더 쏘기)
        if left > info[idx]:
            score[idx] = info[idx] + 1
            dfs(idx-1,score,left-score[idx])
            score[idx] = 0
        
    dfs(10,[0]*11,n)
    
    return [-1] if best_d == 0 else best_a