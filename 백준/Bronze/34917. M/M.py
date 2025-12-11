for _ in range(int(input())):
    N = int(input())
    print('#' + '.' * (N - 2) + '#')
    for i in range(N // 2 - 1):
        print('#' + '.' * i + '#' + '.' * (N - 4 - i * 2) + '#' + '.' * i + '#')
    print('#' + '.' * ((N - 3) // 2) + '#' + '.' * ((N - 3) // 2) + '#')
    for _ in range(N // 2):
        print('#' + '.' * (N - 2) + '#')