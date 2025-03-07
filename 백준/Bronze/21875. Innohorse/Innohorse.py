s1 = input()
s2 = input()
print(*sorted([abs('abcdefgh'.index(s1[0]) - 'abcdefgh'.index(s2[0])), abs(int(s1[1]) - int(s2[1]))]))