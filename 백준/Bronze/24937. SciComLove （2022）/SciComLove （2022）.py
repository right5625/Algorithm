result = 'SciComLove'
for _ in range(int(input()) % 10):
    result = result[1:] + result[0]
print(result)