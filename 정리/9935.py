# 스택
S = input()
B = input()
length = len(B)
stack = []
for i in S:
    stack.append(i)
    while ''.join(stack[-length:]) == B:
        for _ in range(length):
            stack.pop()
print(''.join(stack) if stack else 'FRULA')