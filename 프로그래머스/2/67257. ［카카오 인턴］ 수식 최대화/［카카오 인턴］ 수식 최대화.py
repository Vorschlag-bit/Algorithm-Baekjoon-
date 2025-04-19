from itertools import permutations
def solution(exp):
    ans = []
    for priority in permutations(['*','-','+'],3):
        nums = exp
        for p in priority:
            nums = nums.replace(p, ' ')
        nums = list(map(int, nums.split()))
        ops = [op for op in exp if op in '*-+']
        for p in priority:
            while p in ops:
                i = ops.index(p)
                v = 0
                
                if p == '*':
                    v = nums[i] * nums[i+1]
                elif p == '+':
                    v = nums[i] + nums[i+1]
                else:
                    v = nums[i] - nums[i+1]
                nums[i] = v
                nums.pop(i+1)
                ops.pop(i)
        ans.append(abs(nums[0]))
        a = 0
        for i in ans:
            a = max(a,i)
    return a