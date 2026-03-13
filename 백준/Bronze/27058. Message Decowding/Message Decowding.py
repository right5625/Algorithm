s = input()
result = ''
for i in input():
    if i.isupper():
        result += s[ord(i) - ord('A')].upper()
    elif i.islower():
        result += s[ord(i) - ord('a')]
    else:
        result += ' '
print(result)