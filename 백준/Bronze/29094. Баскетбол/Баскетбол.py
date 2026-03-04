dic = {input(): 0 for _ in range(int(input()))}
cur = [0, 0]
for _ in range(int(input())):
    a, b = input().split(':')
    b, t = b.split()
    dic[t] += (int(a) - cur[0]) + (int(b) - cur[1])
    cur[0], cur[1] = int(a), int(b)
print(*sorted(dic.items(), key=lambda x: -x[1])[0])