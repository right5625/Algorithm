import string

s1, s2 = [], []
for i in input():
    if i in string.ascii_uppercase:
        s1.append(i)
    else:
        s2.append(i)
s1.sort()
s2.sort(reverse=True)
print(s1[0] + s2[0] + s1[1] + s2[1] + s1[2] + s2[2])