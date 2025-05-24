# 트리
import sys
input = lambda : sys.stdin.readline().rstrip()

def preorder(n):
    if n != '.':
        print(n, end = '')
        preorder(tree[n][0])
        preorder(tree[n][1])

def inorder(n):
    if n != '.':
        inorder(tree[n][0])
        print(n, end = '')
        inorder(tree[n][1])

def postorder(n):
    if n != '.':
        postorder(tree[n][0])
        postorder(tree[n][1])
        print(n, end = '')

N = int(input())
tree = dict()
for _ in range(N):
    n, l, r = input().split()
    tree[n] = [l, r]
preorder('A')
print()
inorder('A')
print()
postorder('A')