input()
min_value, max_value = float('inf'), 0
for i in list(map(int, input().split())):
    min_value = min(min_value, i)
    max_value = max(max_value, i)
print(max_value - min_value + 1)