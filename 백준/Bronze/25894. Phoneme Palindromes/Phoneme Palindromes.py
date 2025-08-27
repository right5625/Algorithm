for n in range(int(input())):
    print(f'Test case #{n + 1}:')
    dic = {}
    for _ in range(int(input())):
        a, b = input().split()
        dic[a] = b
        dic[b] = a
    for _ in range(int(input())):
        s = input()
        t = s[::]
        for k, v in dic.items():
            t = t.replace(k, v)
        print(s, 'YES' if t == t[::-1] else 'NO')
    print()