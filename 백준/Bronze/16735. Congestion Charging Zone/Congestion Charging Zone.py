start, end = 24 * 60, 0
for _ in range(int(input())):
    h, m = map(int, input().strip().split(':'))
    time = h * 60 + m
    if 6 * 60 + 30 <= time <= 19 * 60:
        start = min(start, time)
        end = max(end, time)
result = 0
if 6 * 60 + 30 <= start <= 10 * 60:
    if 6 * 60 + 30 <= end <= 16 * 60:
        result = 24000
    elif 16 * 60 + 1 <= end <= 19 * 60:
        result = 36000
elif 10 * 60 + 1 <= start <= 16 * 60:
    if 10 * 60 + 1 <= end <= 16 * 60:
        result = 16800
    elif 16 * 60 + 1 <= end <= 19 * 60:
        result = 24000
print(result)