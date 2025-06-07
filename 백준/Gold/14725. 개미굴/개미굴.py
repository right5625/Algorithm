def travel(cur, n, depth):
    print('--' * depth + n)
    if not cur:
        return
    for i in sorted(cur):
        travel(cur[i], i, depth + 1)

tree = dict()
for _ in range(int(input())):
    K = input().split()
    cur = tree
    for i in range(1, int(K[0])):
        if K[i] not in cur.keys():
            cur[K[i]] = dict()
        cur = cur[K[i]]
    if K[-1] not in cur.keys():
        cur[K[-1]] = dict()
for i in sorted(tree):
    travel(tree[i], i, 0)