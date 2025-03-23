Fs, Cs, Es, Bs = map(int, input().split())
Fn, Cn, En, Bn = map(int, input().split())
cur = 0
for _ in range(int(input())):
    n, i = map(int, input().split())
    if n == 1:
        if Fs >= Fn * i and Cs >= Cn * i and Es >= En * i and Bs >= Bn * i:
            Fs -= Fn * i
            Cs -= Cn * i
            Es -= En * i
            Bs -= Bn * i
            cur += i
            print(cur)
        else:
            print('Hello, siumii')
    elif n == 2:
        Fs += i
        print(Fs)
    elif n == 3:
        Cs += i
        print(Cs)
    elif n == 4:
        Es += i
        print(Es)
    else:
        Bs += i
        print(Bs)