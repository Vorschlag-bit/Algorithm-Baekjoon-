def solution(numbers):
    def check(bi, idx):
        # 루트 노드 idx이자 자식 노드 개수
        L  = len(bi) // 2
        # 자식이 존재한다면
        if L > 0:
            if bi[L] == '0' and ('1' in bi):
                numbers[idx] = 0
            else:
                check(bi[:L],idx)
                check(bi[L+1:],idx)
    
    for idx, n in enumerate(numbers):
        # 우선 2진수로 만들기
        bi = bin(n)[2:]
        l, numbers[idx] = len(bi), 1
        s = 1
        while l >= s:
            s *= 2
        bi = bi.rjust(s-1,'0')
        check(bi, idx)
    return numbers