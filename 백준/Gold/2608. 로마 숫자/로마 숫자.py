def convert(roman):
    arabic = idx = 0
    while idx < len(roman):
        if roman[idx:idx + 2] in dic.keys():
            arabic += dic[roman[idx:idx + 2]]
            idx += 2
        else:
            arabic += dic[roman[idx]]
            idx += 1
    return arabic

dic = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
A = input()
B = input()
arabic_sum = convert(A) + convert(B)
print(arabic_sum)
roman_sum = ''
while arabic_sum:
    if arabic_sum >= 1000:
        roman_sum += 'M'
        arabic_sum -= 1000
    elif arabic_sum >= 900:
        roman_sum += 'CM'
        arabic_sum -= 900
    elif arabic_sum >= 500:
        roman_sum += 'D'
        arabic_sum -= 500
    elif arabic_sum >= 400:
        roman_sum += 'CD'
        arabic_sum -= 400
    elif arabic_sum >= 100:
        roman_sum += 'C'
        arabic_sum -= 100
    elif arabic_sum >= 90:
        roman_sum += 'XC'
        arabic_sum -= 90
    elif arabic_sum >= 50:
        roman_sum += 'L'
        arabic_sum -= 50
    elif arabic_sum >= 40:
        roman_sum += 'XL'
        arabic_sum -= 40
    elif arabic_sum >= 10:
        roman_sum += 'X'
        arabic_sum -= 10
    elif arabic_sum >= 9:
        roman_sum += 'IX'
        arabic_sum -= 9
    elif arabic_sum >= 5:
        roman_sum += 'V'
        arabic_sum -= 5
    elif arabic_sum >= 4:
        roman_sum += 'IV'
        arabic_sum -= 4
    else:
        roman_sum += 'I'
        arabic_sum -= 1
print(roman_sum)