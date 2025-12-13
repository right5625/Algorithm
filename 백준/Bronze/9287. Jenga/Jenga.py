for case in range(1, int(input()) + 1):
    result = 'Standing'
    for _ in range(int(input())):
        if input().find('00') >= 0:
            result = 'Fallen'
    print(f'Case {case}: {result}')