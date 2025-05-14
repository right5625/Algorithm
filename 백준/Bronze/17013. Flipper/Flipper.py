result = [[1, 2], [3, 4]]
for i in input():
    result = [result[1], result[0]] if i == 'H' else [result[0][::-1], result[1][::-1]]
for i in result:
    print(*i)