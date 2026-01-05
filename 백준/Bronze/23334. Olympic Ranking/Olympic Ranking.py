dic = {}
for _ in range(int(input())):
    lst = input().split()
    g, s, b = map(int, lst[:3])
    dic[' '.join(lst[3:])] = [g, s, b]
print(sorted(dic.items(), key=lambda x: x[1])[-1][0])