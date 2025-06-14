N = int(input())
f1, f2, s1, s2 = 0, 1, 0, 1
result = 1
while True:
    if s1 < N <= s2:
        break
    n = f1 + f2
    f1 = f2
    f2 = n
    s1 = s2
    s2 += n
    result += 1
print(result)