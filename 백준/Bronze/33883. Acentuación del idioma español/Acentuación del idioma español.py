S = input()
result = -1
if S[-1] in 'nsaeiou':
    flag = False
    for i in range(len(S) - 1, -1, -1):
        if S[i] in 'aeiou':
            if flag:
                result = i + 1
                break
            else:
                flag = True
else:
    for i in range(len(S) - 1, -1, -1):
        if S[i] in 'aeiou':
            result = i + 1
            break
print(result)