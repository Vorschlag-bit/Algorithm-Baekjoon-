from sys import stdin as input
import sys
sys.setrecursionlimit(10**6)
# 이진 트리를 전위 순회한 걸 바탕으로 후회 순회한 걸로 return
# bst의 특징 = root보다 작은 값은 전부 왼쪽 서브 트리, 큰 건 오른쪽 서브 트리
arr = list(map(int,input.readlines()))

# 후위 순회 재귀 함수(왼,오른,루트)
# 재귀의 흐름 -> 1. 0번 인덱스는 루트이다. 루트를 기준으로 왼/오른 서브 트리를 나눈다.
# 2. 트리의 노드가 1개면 출력하고 return
def rec(arr):
    if len(arr) == 1:
        print(arr[0])
        return

    root = arr[0]
    left = []
    right = []
    for e in arr[1:]:
        if e < root : left.append(e)
        else: right.append(e)

    # left,right,root 순
    if left: rec(left)
    if right: rec(right)
    print(root)

rec(arr)