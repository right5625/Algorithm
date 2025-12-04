dic = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'E': 0, '1': 0.05, '2': 0.025, '3': 0}
n = int(input())
m1 = m2 = 0
for _ in range(n):
    s = input()
    m1 += dic[s[0]]
    if s[0] in 'ABC':
        m2 += dic[s[1]]
print(m1 / n + m2)