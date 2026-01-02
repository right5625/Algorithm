for _ in range(int(input())):
    A = [chr(i).lower() if ord('A') <= i <= ord('Z') or ord('a') <= i <= ord('z') else '-' for i in list(map(int, input().split()))]
    print(''.join(A[1:] + [A[0]]) + 'ay')