from sys import stdin as input
# 1. 중위 표기식을 연산자 우선순위에 따라 괄호로 묶기
# 2. 괄호 안의 연산자를 괄호의 오른쪽으로 이동

exp = input.readline().strip()
# 우선순위
p = {'*': 2, '/': 2, '-': 1, '+': 1, '(': 0, ')': 0}
# stack
stack = []
ans = ''
for char in exp:
    if char not in p.keys():
        ans += char
    else:
        if char == '(': stack.append(char)
        elif char == ')':
            # 해당 닫힌 괄호의 짝이 되는 여는 괄호까지 다 pop
            while stack and p[stack[-1]] > p[char]:
                ans += stack.pop()
            # 여는 괄호 제거
            stack.pop()
        else:
            # 여는 괄호를 제외한 char 이상의 우선순위 제거(오름차순 유지)
            while stack and stack[-1] != '(' and p[stack[-1]] >= p[char]:
                ans += stack.pop()
            stack.append(char)

while stack:
    char = stack.pop()
    if char not in ['(',')']:
        ans += char

print(ans)