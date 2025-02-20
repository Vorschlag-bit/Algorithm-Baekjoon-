from itertools import product
def solution(word):
    w = ['A', 'E', 'I', 'O', 'U']
    arr = []
    answer = 0
    # a e i o u로 만들 수 있는 모든 중복 조합(중복 순열)
    for i in range(1, 6):
        # 중복을 허용하는 i자리 수 순열 리스트
        com = list(product(w, repeat=i))
        arr.extend(''.join(j) for j in com)
    arr.sort()
    answer = arr.index(word) + 1
    return answer