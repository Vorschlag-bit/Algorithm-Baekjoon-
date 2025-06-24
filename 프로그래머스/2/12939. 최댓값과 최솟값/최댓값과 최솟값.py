def solution(s):
    arr = sorted(list(map(int, s.split())))
    return f"{arr[0]} {arr[-1]}"