def solution(s):
    if len(s) == 4 or len(s) == 6:
        if all(c.isdigit() for c in s): return True
        else: return False
    else: return False
        