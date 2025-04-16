from sys import stdin as input

t = int(input.readline())
for _ in range(t):
    n,m,k = map(int, input.readline().split())

    home = list(map(int, input.readline().split()))

    # 순환 배열이므로 2배로 확장
    home = home + home

    for i in range(1,2*n):
        home[i] += home[i-1]
    
    if m == n:
        total = home[n-1]  # 누적합 배열에서 마지막 값: 원래 배열 전체 합
        cnt = 1 if total < k else 0
    else:
        cnt = 0
        for i in range(m-1, n+m-1):
            money = home[i] - (home[i-m] if i-m >= 0 else 0)
            if money < k:
                cnt += 1
    
    print(cnt)