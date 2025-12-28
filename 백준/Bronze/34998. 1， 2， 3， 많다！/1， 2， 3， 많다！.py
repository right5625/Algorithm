for _ in range(int(input())):
    input()
    s = sum([10 if i == '!' else int(i) for i in input().split(' + ')])
    print(s if s < 10 else '!')