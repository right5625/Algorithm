l, w = map(int, input().split())
s = [w // l] * l
for i in range(w % l):
    s[i] += 1
flag = False
for i in range(l):
    if s[i] == 0 or s[i] > 26:
        flag = True
print('impossible' if flag else ''.join(chr(ord('a') + i - 1) for i in s))