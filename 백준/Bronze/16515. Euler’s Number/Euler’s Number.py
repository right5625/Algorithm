inc = res = 1
for i in range(1, int(input()) + 1):
    inc *= i
    res += 1 / inc
print(res)