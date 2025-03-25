h1, h2 = map(int, input().split())
s1, s2 = map(int, input().split())
v1, v2 = map(int, input().split())
R, G, B = map(int, input().split())
lst = sorted({i: j for i, j in zip('RGB', [R, G, B])}.items(), key=lambda x: -x[1])
V = lst[0][1]
S = 255 * (V - lst[-1][1]) / V
if lst[0][0] == 'R':
    H = (60 * (G - B)) / (V - lst[-1][1])
elif lst[0][0] == 'G':
    H = 120 + (60 * (B - R)) / (V - lst[-1][1])
else:
    H = 240 + (60 * (R - G)) / (V - lst[-1][1])
if H < 0:
    H += 360
print('Lumi will like it.' if h1 <= H <= h2 and s1 <= S <= s2 and v1 <= V <= v2 else 'Lumi will not like it.')