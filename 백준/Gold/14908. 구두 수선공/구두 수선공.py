import heapq

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lcm = lst[0][0]
for i in lst[1:]:
    lcm = lcm * i[0] // gcd(lcm, i[0])
heap = []
for i in range(N):
    lst[i][1] *= lcm // lst[i][0]
    heapq.heappush(heap, (-lst[i][1], i + 1))
result = []
while heap:
    _, n = heapq.heappop(heap)
    result.append(n)
print(*result)