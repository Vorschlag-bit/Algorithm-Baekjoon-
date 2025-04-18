def solution(s):
    ans = 0
    
    def rotate(s,x):
        for i in range(x):
            char = s[0]
            s = s[1:]
            s = s + char
        return s
    
    def check(s):
        stack = []
        dic = {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in '{([':
                stack.append(c)
            else:
                if not stack or stack[-1] != dic[c]:
                    return False
                stack.pop()
        # stack 비어있으면 True
        return not stack
    
    for l in range(len(s)):
        string = rotate(s,l)
        if check(string):
            ans += 1
             
    return ans