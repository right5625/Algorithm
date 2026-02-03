n = int(input())
m = 0
while n > 1:
    n >>= 1
    m += 1
result = 1
while m:
    m >>= 1
    result <<= 1
print(f'{result} {"bit" if result == 1 else "bits"}')