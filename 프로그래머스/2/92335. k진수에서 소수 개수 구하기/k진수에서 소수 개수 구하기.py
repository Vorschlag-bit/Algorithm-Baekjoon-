def isPrime(number):
    if number == 1: return False
    if number == 2: return True
    for n in range(3,int(number**0.5)+1):
        # 나눠지면 소수아님
        if number % n == 0:
            return False
    return True

def t2k(number,k):
    s = ''
    while number > 0:
        m = number % k
        s = str(m) + s
        number //= k
    return int(s)
        

def solution(n, k):
    ans = 0
    # n을 k진수로 바꿀 때 변환된 수 안에 아래 조건에 맞는 소수가 몇 개인지 확인
    # 020처럼 소수 양쪽에 0이 있는 경우
    # 20처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
    # 02처럼 소수 왼쪽에 0이 있고 오른쪽에는 아무것도 없는 경우
    # 2처럼 소수 양쪽에 아무것도 없는 경우
    # 일단 k진수로 바꾸고, idx 0 -> n-1까지 윈도우 슬라이딩으로 수를 구하고 소수 판별
    p = t2k(n,k)
    # 문자열 p의 길이
    s = str(p)
    l = len(s)
    idx = 0
    num = ''
    while idx < l:
        # 0이면 현재부터 
        if s[idx] == '0':
            # 빈 칸이 아니라면 prime 체크
            if num != '':
                if isPrime(int(num)): ans += 1
            # num 초기화
            num = ''
        else:
            num += s[idx]
        idx += 1
    # 마지막 num
    if len(num) > 0:
        if isPrime(int(num)): ans += 1
    return ans