A = [int(input()) for _ in range(int(input()))]
print('?') if A[0] not in (min(A), max(A)) else print('ez' if A[0] == min(A) else 'hard')