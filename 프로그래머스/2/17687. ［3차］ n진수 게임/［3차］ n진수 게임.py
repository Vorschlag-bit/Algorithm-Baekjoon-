dic = {"0":"0","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9", "10":"A","11":"B","12":"C","13":"D","14":"E","15":"F"}
def solution(n, t, m, p):
    answer = ''
    num = ''
    # 충분한 길이의 문자열 생성
    for i in range(0, t*m):  # 충분한 범위로 수정
        temp = i
        # n진수로 변환
        if temp == 0:
            digit = "0"
        else:
            digit = ""
            while temp > 0:
                r = temp % n
                digit = dic[str(r)] + digit
                temp //= n
        num += digit
        
        # 충분한 길이가 되면 종료
        if len(num) >= t*m:
            break
    
    # 튜브의 차례에 말해야 하는 숫자만 선택
    for i in range(p-1, t*m, m):
        if len(answer) < t:  # t개까지만 수집
            answer += num[i]
    
    return answer