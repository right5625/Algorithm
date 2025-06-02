import sys, heapq
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    M = int(input())
    A = []
    for _ in range(M // 10 + 1):
        A.extend(list(map(int, input().split())))
    heap1 = []
    heap2 = []
    mid = A[0]
    result = [mid]
    for i in range(1, M, 2):
        left = right = 0
        for j in range(i, i + 2):
            if mid < A[j]:
                right += 1
                heapq.heappush(heap2, A[j])
            else:
                left += 1
                heapq.heappush(heap1, -A[j])
        if left == 2:
            heapq.heappush(heap2, mid)
            mid = -heapq.heappop(heap1)
        elif right == 2:
            heapq.heappush(heap1, -mid)
            mid = heapq.heappop(heap2)
        result.append(mid)
    print(M // 2 + 1)
    for i in range((M // 2 + 1) // 10 + 1):
        print(*result[i * 10:i * 10 + 10])