N, S = input().split()
result, move = '', 1
for i in S:
    result += chr(ord(i) + move) if chr(ord(i) + move) <= 'Z' else chr(ord(i) + move - 26)
    move = (move * 2) % 26
print(result)