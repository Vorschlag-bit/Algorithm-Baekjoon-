from sys import stdin as input
from collections import Counter

s = input.readline()
s = s.lower()
d = Counter(s).most_common(2)
if d[0][1] == d[1][1] and d[1][0].isalpha():
    print('?')
elif d[0][1] > d[1][1]:
    print(d[0][0].upper())
elif d[0][1] == d[1][1] and not d[1][0].isalpha():
    print(d[0][0].upper())