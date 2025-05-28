def solution(a):
    ans = 0
    n = len(a)
    # 특정 인덱스 i 기준으로 0~i-1과 i+1~n 두 범위의 최솟값을 찾고
    # 하나는 i보다 크고, 하나는 i보다 작다면 살아남기 가능
    s = a[0]
    l = a[-1]
    # i보다 작은 인덱스 중 최솟값
    minv = [s]
    # i보다 큰 인덱스 중 최솟값
    maxv = [l]
    for num in range(1,n):
        if a[num] < s:
            s = a[num]
        minv.append(s)
    for num in range(n-2,-1,-1):
        if a[num] < l:
            l = a[num]
        maxv.append(l)
    for i,num in enumerate(a):
        if i == 0 or i == n-1:
            ans += 1
            continue
        else:
            lv = minv[i]
            rv = maxv[n-1-i]
            if (lv >= num and rv <= num) or (lv <= num and rv >= num):
                ans += 1
    return ans