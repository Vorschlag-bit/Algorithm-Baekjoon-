n = int(input())

# 최대 1줄, 최소 2줄
nums = list(map(int, input().split()))

ansMax = -1000000001
ansMin = 10000000001
# 0부터 차례대로 '+', '-', 'x', '/'의 개수
operators = list(map(int, input().split()))

# operators는 n-1개만 들어갈 수 있다. 순서를 고려하므로 (n-1, product)
# 각 연산자는 0개부터 자신의 가진 개수만큼 들어갈 수 있다..
# (+,+...) ~ (/,/...)
# ops = [('+','-'...),()...]
ops = []

for p in range(operators[0] + 1):
    for m in range(operators[1] + 1):
        for g in range(operators[2] + 1):
            if p + m + g > n - 1: continue
            d = (n-1) - (p+m+g)
            if d > operators[3]: continue
            op_list = ['+'] * p + ['-'] * m + ['*'] * g + ['/'] * d
            visit = [0] * len(op_list)

            def permutation(new_arr):
                # 순서 o, 중복 x
                if len(new_arr) == n - 1:
                    ops.append(new_arr[:])
                    return
                used = set()
                for i in range(len(op_list)):
                    if not visit[i] and op_list[i] not in used:
                        used.add(op_list[i])
                        visit[i] = 1
                        new_arr.append(op_list[i])
                        permutation(new_arr)
                        new_arr.pop()
                        visit[i] = 0
            # 순열 생성
            permutation([])

for op_l in ops:
    value = nums[0]
    for idx in range(len(op_l)):
        op = op_l[idx]
        # 4가지 분기 (0 1 2 - 3 4 5)
        if op == '+':
            value += nums[idx+1]
        elif op == '-':
            value -= nums[idx+1]
        elif op == '*':
            value *= nums[idx+1]
        else:
            if value < 0:
                value = -((-value)//nums[idx+1])
            else: value //= nums[idx+1]
    ansMax = max(ansMax,value)
    ansMin = min(ansMin,value)
print(ansMax)
print(ansMin)