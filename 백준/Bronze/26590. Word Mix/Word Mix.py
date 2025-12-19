s1, s2 = input().split()
result = ''
for i in range(min(len(s1), len(s2))):
    result += s1[i] if i % 2 == 0 else s2[i]
print(result)