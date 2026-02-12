for _ in range(int(input())):
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))
    result = 'NO'
    for i in range(5):
        for j in range(5):
            if i != j and a1[i] == a2[j]:
                result = 'YES'
    print(result)