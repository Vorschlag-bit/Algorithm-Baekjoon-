def solution(sizes):
    maxh = 0
    maxw = 0
    
    for w,h in sizes:
        curw = max(w, h)
        curh = min(w, h)
        
        maxh = max(maxh, curh)
        maxw = max(maxw, curw)
    return maxh * maxw