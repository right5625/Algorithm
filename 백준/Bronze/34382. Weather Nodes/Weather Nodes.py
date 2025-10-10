A = [float(input()) for _ in range(int(input()))]
print(len(list(filter(lambda x: x > sum(A) / len(A) + 10 or x < sum(A) / len(A) - 10, A))))