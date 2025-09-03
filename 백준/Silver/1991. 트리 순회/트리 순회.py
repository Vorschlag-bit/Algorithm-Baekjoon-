from sys import stdin as input
from collections import defaultdict
n = int(input.readline())
tree = defaultdict(list)
r = 0
for i in range(n):
    root,left,right = map(str,input.readline().split())
    if i == 0: r = root
    tree[root].append(left)
    tree[root].append(right)
p = ''
m = ''
l = ''
def pre(root):
    global p
    if root == '.': return
    p += root
    left,right = tree[root][0],tree[root][1]
    pre(left)
    pre(right)

def mid(root):
    global m
    if root == '.': return
    left,right = tree[root][0],tree[root][1]
    mid(left)
    m += root
    mid(right)

def post(root):
    global l
    if root == '.': return
    left,right = tree[root][0],tree[root][1]
    post(left)
    post(right)
    l += root
pre(r)
mid(r)
post(r)
print(p)
print(m)
print(l)