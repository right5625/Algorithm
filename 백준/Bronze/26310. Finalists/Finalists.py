n = int(input())
tuples = []
for _ in range(6):
    s, pt, pu, rt, ru, f = input().split()
    score = 0.56 * int(pt) + 0.24 * int(pu) + 0.14 * int(rt) + 0.06 * int(ru) + 0.3 * int(f)
    tuples.append((score, s))
tuples.sort(key=lambda x: -x[0])
slot = [0] * 6
for i in range(n):
    slot[i % 6] += 1
for i in range(6):
    if tuples[i][1] == "Taiwan":
        print(slot[i])
        break