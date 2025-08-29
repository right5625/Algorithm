for _ in range(int(input())):
    k = int(input()) + 1
    while '0' in str(k):
        k += 1
    print(k)