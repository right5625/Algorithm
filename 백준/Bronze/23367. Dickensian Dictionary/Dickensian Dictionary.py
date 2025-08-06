S = input()
l, r = 'qwertasdfgzxcvb', 'yuiophjklnm'
flag = True if S[0] in l else False
result = 'yes'
for i in S[1:]:
    if not ((flag and i in r) or (not flag and i in l)):
        result = 'no'
        break
    flag = not flag
print(result)