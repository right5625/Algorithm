input()
A = [0] * 3
for i in list(map(int, input().split())):
    A[i - 1] += 1
print(f'{A.index(min(A)) + 1}\n{A.index(max(A)) + 1}')