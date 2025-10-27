N, Y = map(int, input().split())
dic = {i: True for i in range(N)}
for _ in range(Y):
    dic[int(input())] = False
for i in range(N):
    if dic[i]:
        print(i)
print(f'Mario got {list(dic.values()).count(False)} of the dangerous obstacles.')