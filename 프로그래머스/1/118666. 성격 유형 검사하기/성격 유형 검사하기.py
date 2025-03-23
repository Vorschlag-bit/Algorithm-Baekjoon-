def solution(survey, choices):
    ans = ''
    # 같으면 사전순으로 빠른 거
    mbti = {"A":0,"N":0,"C":0,"F":0,"M":0,"J":0,"R":0,"T":0}
    for idx,category in enumerate(survey):
        # 비동의,동의
        c1,c2 = category[0], category[1]
        choice = choices[idx]
        # 1 = 매우 비동의, 7 = 매우 동의
        if 0 < choice < 4:
            mbti[c1] += abs(choice - 4)
        if 4 < choice < 8:
            mbti[c2] += choice - 4
    ans += 'R' if mbti['R'] >= mbti['T'] else 'T'
    ans += 'C' if mbti['C'] >= mbti['F'] else 'F'
    ans += 'J' if mbti['J'] >= mbti['M'] else 'M'
    ans += 'A' if mbti['A'] >= mbti['N'] else 'N'
        
    return ans