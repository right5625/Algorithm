for t in range(int(input())):
    word = [input() for _ in range(int(input()))]
    print(f'Scenario #{t + 1}:')
    for _ in range(int(input())):
        s = ''
        for i in list(map(int, input().split()))[1:]:
            s += word[i]
        print(s)
    print()