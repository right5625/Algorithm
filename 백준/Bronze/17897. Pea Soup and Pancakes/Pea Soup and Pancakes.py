result = 'Anywhere is fine I guess'
found = False
for _ in range(int(input())):
    k = int(input())
    name = input()
    has_pea_soup = has_pancakes = False
    for _ in range(k):
        s = input()
        if s == 'pea soup':
            has_pea_soup = True
        if s == 'pancakes':
            has_pancakes = True
    if has_pea_soup and has_pancakes and not found:
        result = name
        found = True
print(result)