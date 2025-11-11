lecture = {i: False for i in range(5)}
for _ in range(int(input())):
    lecture[int(input()) - 1] = True
print('NO' if list(lecture.values()).count(True) == 5 else 'YES')