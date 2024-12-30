import sys;
n = int(input())

# n을 -4(+, =)한 상태로 3등분
n -= 4
flag = False
arr = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
for i in range(10):
    for j in range(10):
        first = 10 * i + j
        used = arr[i] + arr[j]
        if used > n:  # 이미 초과했다면 더 진행할 필요 없음
            continue
        for k in range(10):
            for l in range(10):
                second = 10 * k + l
                num = first + second

                if num > 99:
                    continue

                used = arr[i] + arr[j] + arr[k] + arr[l]
                if used > n: # 사용한 성냥개비 양 초과
                    continue
                
                result_first = num // 10
                result_second = num % 10
                needed = arr[result_first] + arr[result_second]

                if used + needed == n:
                    print(f"{first:02d}+{second:02d}={num:02d}")
                    sys.exit(0)
print("impossible")                  