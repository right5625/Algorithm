def travel(subTree, child, depth):
    print('--' * depth + child)
    if not subTree:
        return
    for c in sorted(subTree):
        travel(subTree[c], c, depth + 1)

tree = dict()
for _ in range(int(input())):
    K = input().split()
    cur = tree
    for i in K[1:]:
        if i not in cur.keys():
            cur[i] = dict()
        cur = cur[i]
for c in sorted(tree):
    travel(tree[c], c, 0)