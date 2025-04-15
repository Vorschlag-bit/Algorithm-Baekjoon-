def base_to_deci(s, base):
    n = 0
    for char in s:
        # s가 숫자들로만 이루어졌다고 가정
        digit = ord(char) - ord('0')
        n = n * base + digit
    return n

def deci_to_base(num, base):
    if num == 0:
        return "0"
    digits = ""
    while num > 0:
        r = num % base
        digits = str(r) + digits
        num //= base
    return digits

def solution(expressions):
    answer = []
    unknown_expressions = []
    min_base = 2
    # 모든 식에서 최소 진법을 결정 (숫자+1이 최소 진법)
    for exp in expressions:
        n1, op, n2, eq, n3 = exp.split()
        for s in [n1, n2]:
            for ch in s:
                min_base = max(min_base, int(ch) + 1)
        if n3 != 'X':
            for ch in n3:
                min_base = max(min_base, int(ch) + 1)
        else:
            unknown_expressions.append(exp)
    
    # 후보 진법은 min_base부터 9진법(10 미만)까지
    candidate_bases = list(range(min_base, 10))
    
    # 알려진 결과를 가진 식들을 사용하여 후보 진법 필터링
    for exp in expressions:
        n1, op, n2, eq, n3 = exp.split()
        if n3 == 'X':
            continue
        valid_bases = []
        for base in candidate_bases:
            dec_n1 = base_to_deci(n1, base)
            dec_n2 = base_to_deci(n2, base)
            dec_n3 = base_to_deci(n3, base)

            if op == '+':
                if dec_n1 + dec_n2 == dec_n3:
                    valid_bases.append(base)
            elif op == '-':
                if dec_n1 - dec_n2 == dec_n3:
                    valid_bases.append(base)
        # 후보 진법 목록과 valid_bases의 교집합을 다시 후보로 유지
        candidate_bases = [b for b in candidate_bases if b in valid_bases]
    
    # 미지수 식에 대해, 각 후보 진법마다 계산한 결과를 구해서
    # 결과가 모두 일치하면 정답, 아니라면 '?'로 표시
    for exp in unknown_expressions:
        n1, op, n2, eq, n3 = exp.split()
        op = op.strip()

        results = set()
        for base in candidate_bases:
            dec_n1 = base_to_deci(n1, base)
            dec_n2 = base_to_deci(n2, base)
            if op == '+':
                calc = dec_n1 + dec_n2
            elif op == '-':
                calc = dec_n1 - dec_n2
            result_str = deci_to_base(calc, base)
            results.add(result_str)
        if len(results) == 1:
            # 유일한 결과가 나오면 해당 결과값을 식에 붙임
            answer.append(f"{n1} {op} {n2} = {results.pop()}")
        else:
            answer.append(f"{n1} {op} {n2} = ?")
    return answer