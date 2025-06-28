S = input()
result = 0
for i in range(26):
    if 'i' not in [chr(ord(j) + i if ord(j) + i <= 122 else ord(j) + i - 26) for j in S]:
        result += 1
print(result if result else 'impossible')