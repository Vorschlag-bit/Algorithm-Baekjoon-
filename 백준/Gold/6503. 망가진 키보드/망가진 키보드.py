import sys

while True:
    m = int(sys.stdin.readline().strip())
    if m == 0: 
        break

    str = sys.stdin.readline().strip()
    char_count = {} # 현재 윈도우에 있는 각 문자의 등장 횟수를 저장
    max_len = 0
    left = 0 # 왼쪽 포인터

    for right in range(len(str)):
        # 현재 문자의 등장 횟수 증가
        char_count[str[right]] = char_count.get(str[right], 0) + 1

        # 윈도우 내의 서로 다른 문자가 m 초과 시
        # 왼쪽 포인터를 이동시키면 윈도우 축소
        while len(char_count) > m:
            char_count[str[left]] -= 1
            if char_count[str[left]] == 0:
                del char_count[str[left]]
            left += 1
        
        # 현재 윈도우의 길이와 최대 길이 비교
        max_len = max(max_len, right - left + 1)
    
    print(max_len)