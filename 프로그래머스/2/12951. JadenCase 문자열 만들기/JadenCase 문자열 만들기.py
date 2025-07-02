def solution(s):
    ans = ''
    flag = True
    for c in s:
        if flag:
            ans += c.upper()
        else: ans += c.lower()
        # 이전 문자가 공백이면 upper
        # c가 공백인지 확인(공백일 경우 upper해도 "")
        flag = c == " "
    return ans