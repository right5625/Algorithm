S = [input() for _ in range(3)]
idx = -1
for i in range(3):
    if S[i] not in ['FizzBuzz', 'Fizz', 'Buzz']:
        idx = i
        break
N = int(S[idx]) + (3 - idx)
if N % 3 == N % 5 == 0:
    print('FizzBuzz')
elif N % 3 == 0:
    print('Fizz')
elif N % 5 == 0:
    print('Buzz')
else:
    print(N)