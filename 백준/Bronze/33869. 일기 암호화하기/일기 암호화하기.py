lst = []
for i in input():
    if i not in lst:
        lst.append(i)
for i in range(ord('A'), ord('Z') + 1):
    if chr(i) not in lst:
        lst.append(chr(i))
print(''.join([lst[ord(i) - ord('A')] for i in input()]))