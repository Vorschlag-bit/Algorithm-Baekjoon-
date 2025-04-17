def solution(cap, n, deliveries, pickups):
    answer = 0
    for i in range(n-2,-1,-1):
        deliveries[i] += deliveries[i+1]
        pickups[i] += pickups[i+1]
        
    t = 0
    for i in range(n-1,-1,-1):
        while t * cap < deliveries[i] or t * cap < pickups[i]:
            answer += (i+1)*2
            t += 1
    return answer