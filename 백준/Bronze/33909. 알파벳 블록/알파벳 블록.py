S, C, O, N = map(int, input().split())
print(min((S + N) // 3, (C + O * 2) // 6))