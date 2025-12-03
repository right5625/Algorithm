A = [input() for _ in range(int(input()))]
print('Yonsei Won!' if A.index('yonsei') < A.index('korea') else 'Yonsei Lost...')