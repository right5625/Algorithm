dic = {'U': False, 'A': False, 'P': False, 'C': False}
for i in input():
    dic[i] = True
print(''.join(k for k in dic.keys() if not dic[k]))