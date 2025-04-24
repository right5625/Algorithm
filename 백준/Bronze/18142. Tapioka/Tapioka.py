S = [i for i in list(input().split()) if i not in ['bubble', 'tapioka']]
print(' '.join(S) if S else 'nothing')