from collections import defaultdict

dic = defaultdict(int)
for k, v in {tuple([':::', ':o:', ':::']): 1, tuple(['o::', ':::', '::o']): 2, tuple(['::o', ':::', 'o::']): 2, tuple(['o::', ':o:', '::o']): 3, tuple(['::o', ':o:', 'o::']): 3, tuple(['o:o', ':::', 'o:o']): 4, tuple(['o:o', ':o:', 'o:o']): 5, tuple(['ooo', ':::', 'ooo']): 6, tuple(['o:o', 'o:o', 'o:o']): 6}.items():
    dic[k] = v
res = dic[tuple([input() for _ in range(3)])]
print(res if res else 'unknown')