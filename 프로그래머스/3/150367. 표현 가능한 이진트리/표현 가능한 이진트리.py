def t2k(n,k):
    s = ''
    while n > 0:
        r = n % k
        s = str(r) + s
        n //= k
    return s

def find(n):
    b = 1
    while b < n:
        b *= 2
    return b-1

def pre_order(s):
    l = len(s)
    
    # 단일 노드면 항상 True
    if l == 1: return True

    # 루트 노드 찾기
    r = l // 2
    root = s[r]
    
    # 루트 기준으로 왼/오른 순으로 순회
    left = s[:r]
    right = s[r+1:]
    
    # 루트가 0인데 자식이 1이 있다면 False
    if root == '0':
        if '1' in left or '1' in right: return False
    
    return pre_order(left) and pre_order(right)
    

def solution(numbers):
    ans = []
    # 리프 노드가 아닌 노드는 자신의 왼쪽 자식이 루트인 서브 트리
    # pre_order로 순회
    # 어떤 수를 2진수로 만들기
    # 해당 2진수가 포화 이진트리를 만족하는지 검증
    # 7 -> 111, 5 -> 101, 42 -> 101010 -> 완전포화가 되기 위해선 반드시 홀수 길이
    # 노드가 l개인 트리의 높이 = (l+1) = 2**h
    # pre_order로 순회하다가 자식이 있는데 0일 경우 return False
    # root node가 0인 경우 False
    for n in numbers:
        # n보다 크면서 가장 가까운 2진수-1(완전 포화 트리) 구하기
        s = t2k(n,2)
        # len(s)가 속하는 완전 포화 트리 구하기
        l = 1
        while l <= len(s):
            l *= 2
        l -= 1
        s = s.rjust(l,'0')
        if pre_order(s): ans.append(1)
        else: ans.append(0)
    return ans