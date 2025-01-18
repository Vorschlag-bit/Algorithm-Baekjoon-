from collections import Counter
import sys

input = sys.stdin.readline
n = int(input().strip())
for _ in range(n):
    str1, str2 = input().split()
    # Counter 객체로 각 문자의 빈도수를 한 번에 계산
    print("Possible" if Counter(str1) == Counter(str2) else "Impossible")