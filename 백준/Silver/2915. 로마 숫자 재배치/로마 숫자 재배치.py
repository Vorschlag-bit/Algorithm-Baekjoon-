from collections import Counter
num = input()

# 1부터 num까지 로마자로 만들고, 그 로마자가 num의 완벽한 에너그램이면 최소 숫자
dic = [''] * 100
dic[1] = 'I'
dic[2] = 'II'
dic[3] = 'III'
dic[4] = 'IV'
dic[5] = 'V'
dic[6] = 'VI'
dic[7] = 'VII'
dic[8] = 'VIII'
dic[9] = 'IX'
dic[10] = 'X'
dic[20] = 'XX'
dic[30] = 'XXX'
dic[40] = 'XL'
dic[50] = 'L'
dic[60] = 'LX'
dic[70] = 'LXX'
dic[80] = 'LXXX'
dic[90] = 'XC'

for i in range(1, 100):
    roman = ''
    # 십의 자리 수 먼저
    roman += dic[i//10*10]
    # 일의 자리 수
    roman += dic[i%10]
    if Counter(roman) == Counter(num):
        print(roman)
        break