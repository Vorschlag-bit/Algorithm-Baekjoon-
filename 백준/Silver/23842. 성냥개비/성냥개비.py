import sys;
n = int(input())

# n을 -4(+, =)한 상태로 3등분
n -= 4
flag = False
arr = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                first = 10 * i + j
                second = 10 * k + l
                num = first + second

                if num > 99:
                    continue

                used = arr[i] + arr[j] + arr[k] + arr[l]
                result_first = num // 10
                result_second = num % 10
                needed = arr[result_first] + arr[result_second]

                if used + needed == n:
                    print(f"{first:02d}+{second:02d}={num:02d}")
                    sys.exit(0)
print("impossible")                  