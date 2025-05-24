# 순열
N = int(input())
lst = list(map(int, input().split()))
F = [1] * (N + 1)
for i in range(2, N + 1):
    F[i] = F[i - 1] * i
if lst[0] == 1:
    K = lst[1]
    lst = [i for i in range(N + 1)]
    idx = N - 1
    while idx > 0:
        cnt = 1
        while K > F[idx] * cnt:
            cnt += 1
        K -= F[idx] * (cnt - 1)
        print(lst.pop(cnt), end = ' ')
        idx -= 1
    print(lst.pop(1))
else:
    K = 1
    vst = [False] * (N + 1)
    for i in range(1, N + 1):
        cnt = 0
        for j in range(1, lst[i]):
            if not vst[j]:
                cnt += 1
        K += F[N - i] * cnt
        vst[lst[i]] = True
    print(K)