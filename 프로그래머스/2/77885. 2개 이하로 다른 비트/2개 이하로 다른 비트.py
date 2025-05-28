def solution(num):
    ans = []
    for n in num:
        nl = list('0'+bin(n)[2:])
        i = ''.join(nl).rfind('0')
        nl[i] = '1'
        if n % 2 != 0: nl[i+1] = '0'
        ans.append(int(''.join(nl),2))
    return ans