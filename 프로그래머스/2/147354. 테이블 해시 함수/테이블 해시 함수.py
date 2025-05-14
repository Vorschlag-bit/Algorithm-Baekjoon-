def solution(data, col, rb, re):
    ans = 0
    # col번째 값을 기준으로 오름차순하되, 그 값이 동일하면
    # 기본키인 첫 번째 칼람의 기준으로 내림차순
    data.sort(key=lambda x: (x[col-1], -x[0]))
    for r in range(rb,re+1):
        si = sum(value % r for value in data[r-1])
        ans ^= si
    return ans