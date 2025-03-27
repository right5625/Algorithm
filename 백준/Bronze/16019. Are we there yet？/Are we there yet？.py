A = list(map(int, input().split()))
for i in range(5):
    s = sum(A[:i])
    lst = [s]
    inc = False
    for j in range(4):
        if s == 0:
            inc = True
        if not inc:
            s -= A[j]
        else:
            s += A[j]
        lst.append(s)
    print(*lst)