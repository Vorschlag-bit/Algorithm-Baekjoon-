from sys import stdin as input
from collections import defaultdict,deque
n,m = map(int,input.readline().split())
graph = defaultdict(set)
# 1,6이 들어감
# 1 뒤에는 4, 6 뒤에는 2가 들어감
# 4의 tp는 2[2,5]

tp = defaultdict(set)

for _ in range(m):
    arr = list(map(int,input.readline().split()))
    if len(arr) == 2: continue
    for i in range(1,len(arr)-1):
        num = arr[i]
        nxt = arr[i+1]
        graph[num].add(nxt)
        # num의 set에 지금까지 쌓은 걸 union
        tp[nxt].add(num)
    # 마지막 원소
    last = arr[-1]
    last_ex = arr[-2]
    tp[last].add(last_ex)

q = deque()
ans = []
for num in range(1,n+1):
    if len(tp[num]) == 0:
        q.append(num)

while q:
    num = q.popleft()
    ans.append(num)
    for nxt in graph[num]:
        tp[nxt].discard(num)
        if len(tp[nxt]) == 0:
            q.append(nxt)

if len(ans) != n: print(0)
else:
    print('\n'.join(map(str,ans)))