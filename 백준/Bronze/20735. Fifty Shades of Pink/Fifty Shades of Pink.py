result = 0
for _ in range(int(input())):
    S = input().lower()
    if 'pink' in S or 'rose' in S:
        result += 1
print(result if result else 'I must watch Star Wars with my daughter')