N = int(input())
result = length = 0
for i in input():
    if i == 'a':
        length += 1
    else:
        if length >= 2:
            result += length
        length = 0
if length >= 2:
    result += length
print(result)