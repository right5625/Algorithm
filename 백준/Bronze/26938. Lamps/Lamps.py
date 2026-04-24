h, P = map(int, input().split())
day_cost1 = 60 * h * P
day_cost2 = 11 * h * P
cost1 = 5 * 100000 + day_cost1
cost2 = 60 * 100000 + day_cost2
hour = h
day = 1
while cost1 <= cost2:
    cost1 += day_cost1
    cost2 += day_cost2
    hour += h
    if hour > 1000:
        cost1 += 5 * 100000
        hour -= 1000
    day += 1
print(day)