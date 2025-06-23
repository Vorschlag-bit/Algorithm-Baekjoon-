def solution(arr):
    m = min(arr)
    arr.remove(m)
    return arr if arr else [-1]