import sys
input = sys.stdin.readline

def check(num):
    l = len(num)
    if num[0] != "1" or num[l - 1] != "2":
        return "NOT"
    for i in range(l - 1):
        a = int(num[i])
        b = int(num[i + 1])
        if b not in graph[a]:
            return "NOT"
    else:
        return "VALID"

graph = [[] for i in range(9)]
graph[1] = [4, 5]
graph[2] = []
graph[3] = [4, 5]
graph[4] = [2, 3]
graph[5] = [8]
graph[6] = [2, 3]
graph[7] = [8]
graph[8] = [7, 6]
no = 1
while True:
    num = input().strip()
    if num == "0":
        break
    ans = check(num)
    print(f"{no}. {ans}")
    no += 1

