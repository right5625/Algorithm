dic = {i: 0 for i in 'A23456789TJQK'}
for i in list(input().split()):
    dic[i[0]] += 1
print(sorted(dic.items(), key=lambda x: -x[1])[0][1])