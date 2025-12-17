from sys import stdin as input

s = input.readline().rstrip()

t = list(input.readline().rstrip())

# 문자열이 폭자열을 포함하면 문자열 내 모든 폭자열은 사라지고 남은 거 이어붙이기.
# 폭자열이 사라질 때까지 반복

# 매번 100만을 체크할 순 없음
# stack
# stack의 길이가 len(t) 이상이고, stack[-1] == t[-1]일 때
# -1부터 -1 + len(t)만큼 체크 후, 존재하면 pop() 아니면 다음 문자열로 이동
# 시간 복잡도는? n * m?

stack = []
for char in s:
    stack.append(char)
    if len(stack) >= len(t) and stack[-1] == t[-1]:
        if stack[-len(t):] == t:
            del stack[-len(t):]

if stack: print(''.join(stack))
else: print('FRULA')