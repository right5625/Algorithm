input()
result = 0
for i in input().split():
    if i == i[::-1]:
        result += int(i)
print(result)