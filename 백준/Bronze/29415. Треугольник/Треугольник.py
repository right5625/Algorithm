S = int(input()) * 2
result = 0
for i in range(1, S + 1):
    if S % i == 0 and i <= S // i and int((i * i + (S // i) * (S // i)) ** 0.5) * int((i * i + (S // i) * (S // i)) ** 0.5) == i * i + (S // i) * (S // i):
        result += 1
print(result)