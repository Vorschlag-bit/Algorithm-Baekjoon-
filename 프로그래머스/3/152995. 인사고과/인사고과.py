def solution(scores):
    answer = 1
    me = scores[0]
    scores.sort(key=lambda x : (-x[0], x[1]))
    maxB = 0

    for a, b in scores:
        if me[0] < a and me[1] < b:
            return -1

        if b >= maxB:
            maxB = b
            if a + b > sum(me):
                answer += 1
    return answer