def solution(n):
    # 누적합 배열의 두 원소 차가 n이 되는 (i, j) 쌍의 개수
    arr = [0]
    for i in range(1,n+1):
        arr.append(arr[-1] + i)
    l = 0
    r = 0
    ans = 0
    while r < len(arr):
        s = arr[r] - arr[l]
        if s == n:
            ans += 1
            r += 1
        elif s > n:
            l += 1
        else: r += 1
    return ans