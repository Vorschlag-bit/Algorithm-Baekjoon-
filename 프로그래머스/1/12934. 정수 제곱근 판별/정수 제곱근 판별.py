def solution(n):
    answer = -1
    if int(n**0.5)**2 == n:
        answer = int(n**0.5) + 1
    return answer**2 if not answer == -1 else answer