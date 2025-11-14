def permutations_with_replacement(expr, op_cnt):
    if op_cnt == N - 1:
        if expr.count(' ') == N - 1:
            return
        new_expr = expr.replace(' ', '')
        op_idx = [i for i in range(len(new_expr)) if new_expr[i] in '+-']
        cal = int(new_expr[:op_idx[0]])
        for i in range(len(op_idx) - 1):
            cal += int(new_expr[op_idx[i] + 1:op_idx[i + 1]]) * (1 if new_expr[op_idx[i]] == '+' else -1)
        cal += int(new_expr[op_idx[-1] + 1:]) * (1 if new_expr[op_idx[-1]] == '+' else -1)
        if cal == 0:
            result.append(expr)
        return
    for i in range(3):
        permutations_with_replacement(expr + op[i] + str(int(expr[-1]) + 1), op_cnt + 1)

op = ['+', '-', ' ']
for _ in range(int(input())):
    N = int(input())
    result = []
    permutations_with_replacement('1', 0)
    print(*sorted(result), sep='\n')
    print()