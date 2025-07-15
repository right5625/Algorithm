result, maxNum = '', 0
for _ in range(int(input())):
    s = input()
    n = int(input())
    if n > maxNum:
        result = s
        maxNum = n
print(result)