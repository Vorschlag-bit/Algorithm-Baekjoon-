from itertools import combinations

def solution(n, q, ans):
    # 모든 가능한 5자리 조합을 구함
    all_possible = set()
    
    # 1부터 n까지의 숫자 중 5개를 선택하는 모든 조합
    for possible_code in combinations(range(1, n+1), 5):
        # 각 조합이 모든 질문에 대한 조건을 만족하는지 확인
        valid = True
        for i in range(len(q)):
            question = q[i]
            required_match = ans[i]
            
            # 현재 조합과 질문에 있는 숫자들의 교집합 개수 계산
            match_count = sum(1 for num in possible_code if num in question)
            
            # 조건을 만족하지 않으면 유효하지 않음
            if match_count != required_match:
                valid = False
                break
        
        # 모든 질문에 대한 조건을 만족하면 정답에 추가
        if valid:
            all_possible.add(possible_code)
    
    return len(all_possible)