import sys
input = lambda: sys.stdin.readline().rstrip()

S1 = input()
flag = True
for i in range(int(input())):
    S2 = input()
    if flag and len(S1) == len(S2):
        cnt = 0
        for j, k in zip(S1, S2):
            if j != k:
                cnt += 1
        if cnt <= 1:
            result = i + 1
            flag = False
print(result)