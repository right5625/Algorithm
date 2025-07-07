result = ''
for i in range(1, int(input()) + 1):
    if str(i) not in result:
        result += str(i)
print(result)