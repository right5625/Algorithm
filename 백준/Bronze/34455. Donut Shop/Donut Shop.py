D = int(input())
for _ in range(int(input())):
    if input() == '+':
        D += int(input())
    else:
        D -= int(input())
print(D)