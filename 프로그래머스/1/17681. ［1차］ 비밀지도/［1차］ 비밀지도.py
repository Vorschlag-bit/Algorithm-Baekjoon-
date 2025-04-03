def solution(n, arr1, arr2):
    # 하나라도 벽 -> 모두 벽
    # 모두 공백 -> 모두 공백
    # arr1과 2 모두 2진수값으로 준다, 둘을 포갠 전체 지도 만들기
    map = [[' '] * n for _ in range(n)]
    # 1. arr1 지도 해석
    for idx,b in enumerate(arr1):
        # 2진법 문자로 바꾸고
        binary = bin(b)[2:]
        binary = binary.rjust(n,'0')
        for l in range(len(binary)):
            if binary[l] == '1':
                map[idx][l] = '#'
    # 2. arr2 지도 해석
    for idx,b in enumerate(arr2):
        binary = bin(b)[2:]
        binary = binary.rjust(n,'0')
        for l in range(len(binary)):
            if binary[l] == '1':
                map[idx][l] = '#'
    ans = []
    for i in range(n):
        ans.append("".join(map[i]))
    return ans