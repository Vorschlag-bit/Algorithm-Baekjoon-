from re import split
from itertools import permutations
def solution(exp):
    ans = []
    for priority in permutations(['*','-','+'], 3):
        nums = list(map(int, split('[\*\-\+]', exp)))
        operators = [c for c in exp if c in '+-*']
        for p in priority:
            while p in operators:
                i = operators.index(p)
                v = 0
                if p == '*':
                    v += nums[i] * nums[i+1]
                elif p == '-':
                    v += nums[i] - nums[i+1]
                else:
                    v += nums[i] + nums[i+1]
                nums[i] = v
                nums.pop(i+1)
                operators.pop(i)
        ans.append(nums[0])
    answer = 0
    for a in ans:
        answer = max(answer, abs(a))
    return answer