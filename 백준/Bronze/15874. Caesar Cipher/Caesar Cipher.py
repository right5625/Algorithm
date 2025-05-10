import string

k, s = map(int, input().split())
result = ''
for i in input():
    if i in string.ascii_lowercase:
        t = ord(i) + k % 26
        if 'z' < chr(t):
            t -= 26
        result += chr(t)
    elif i in string.ascii_uppercase:
        t = ord(i) + k % 26
        if 'Z' < chr(t):
            t -= 26
        result += chr(t)
    else:
        result += i
print(result)