from sys import stdin as input

# 특정 문자열 s, 특정 알파벳 a와 문자열 구간[l,r]이 주어질 때
# S의 l~r 사이에 a가 몇 번 나타나는지 구하는 프로그램 작성

# 0-based, l,r 인덱스 포함
s = input.readline().strip()
n = len(s)
q = int(input.readline())
cmd = []

for _ in range(q):
    a,l,r = input.readline().split()
    cmd.append((a,int(l),int(r)))

# q = 20만, 문자열 길이 = 20만
# a-z
char = [[0] * 26]

# idx와 char를 통해, 해당 char아 char 등장 배열의 idx에 등장했음을 + 1
for i,c in enumerate(s):
    idx = ord(c) - 97
    cur = char[-1][:]
    cur[idx] += 1
    char.append(cur)
    
# cmd 배열을 순회하면서 계산
result = []
for a,l,r in cmd:
    idx = ord(a) - 97
    result.append(str(char[r+1][idx] - char[l][idx]))

print('\n'.join(result))