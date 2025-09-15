x, y, z = map(int, input().split())
score = x * 0.25 + y * 0.25 + z * 0.5
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')