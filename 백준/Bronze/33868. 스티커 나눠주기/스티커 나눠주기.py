T = []
B = []
for _ in range(int(input())):
    t, b = map(int, input().split())
    T.append(t)
    B.append(b)
print(max(T) * min(B) % 7 + 1)