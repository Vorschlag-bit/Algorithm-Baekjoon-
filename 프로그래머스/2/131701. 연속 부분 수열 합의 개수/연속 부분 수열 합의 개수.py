def solution(elements):
    n = len(elements)
    ans = set()
    for l in range(n):
        e = elements[l]
        ans.add(e)
        for i in range(l+1,l+n):
            e += elements[i%n]
            ans.add(e)
    return len(ans)