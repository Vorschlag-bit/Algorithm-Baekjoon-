def solution(dartResult):
    answer = 0
    result = ''
    prev = ''
    d2s = dict()
    s2d = dict()
    for i in range(10,-1,-1):
        d2s[str(i)] = " " + chr(ord('a') + i)
        s2d[chr(ord('a') + i)] = i
    for k in d2s.keys():
        dartResult = dartResult.replace(k, d2s[k])
    result = dartResult.split()
    prevS = 0
    for r in result:
        score,area = s2d[r[0]], r[1]
        if area == 'D':
            score = score ** 2
        elif area == 'T':
            score = score ** 3
        # 옵션 판단
        if len(r) == 3:
            if r[2] == '*':
                answer += prevS
                score *= 2
            elif r[2] == '#': 
                score *= -1
        answer += score
        prevS = score
    return answer