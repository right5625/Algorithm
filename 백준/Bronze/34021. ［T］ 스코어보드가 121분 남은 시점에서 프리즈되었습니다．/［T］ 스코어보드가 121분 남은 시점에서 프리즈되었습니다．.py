for _ in range(int(input())):
    N, M, L = map(int, input().split())
    result = max([L] + list(map(lambda x: M - x, filter(lambda x: x != -1, list(map(int, input().split()))))))
    print(f'The scoreboard has been frozen with {result} {"minute" if result == 1 else "minutes"} remaining.')