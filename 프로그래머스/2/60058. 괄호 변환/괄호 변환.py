def divide(s):
    l = 0
    r = 0
    for idx,c in enumerate(s):
        if c == '(':
            l += 1
        else:
            r += 1
        if r == l:
            return s[:idx+1], s[idx+1:]

def check(s):
    stack = []
    
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                return False
            elif stack[-1] == '(':
                stack.pop()
    return True

def solution(p):    
    if p == '':
        return p
    
    cur = ''
    u,v = divide(p)
    
    if check(u):
        cur += u
        cur += solution(v)
    else:
        cur += '('
        cur += solution(v)
        cur += ')'
        cur += ''.join('(' if ch == ')' else ')' for ch in u[1:-1])
    
    return cur