from collections import Counter
def solution(s):
    s = s.lower()
    c = Counter(s)
    if c.get('p',0) == c.get('y',0):
        return True
    else: return False
