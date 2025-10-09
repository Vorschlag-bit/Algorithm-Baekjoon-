from itertools import permutations as perm

def cal(x,y,t):
    if t == '*': return x * y
    elif t == '-': return x - y
    else: return x + y

def solution(exp):
    ans = 0
    
    for p in perm(['*','+','-'],3):
        # 우선 순위 결정
        total = 0
        copy = exp
        for char in p:
            copy = copy.replace(char,' ')
        copy = copy.split(' ')
        ops = [o for o in exp if o in ['*','-','+']]
        for char in p:
            while char in ops:
                i = ops.index(char)
                ex = int(copy[i])
                nxt = int(copy[i+1])
                value = cal(ex,nxt,char)
                copy[i] = value
                copy.pop(i+1)
                ops.pop(i)
        ans = max(ans,abs(copy[0]))
    return ans