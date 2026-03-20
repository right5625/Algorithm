lengths = []
occupied_segments = set()
for _ in range(3):
    left, right = map(int, input().split())
    lengths.append(right - left)
    for i in range(left, right):
        occupied_segments.add(i)
if not occupied_segments:
    count = 0
else:
    sorted_segments = sorted(list(occupied_segments))
    count = 1
    for i in range(len(sorted_segments) - 1):
        if sorted_segments[i + 1] != sorted_segments[i] + 1:
            count += 1
print(count)
print(min(lengths), max(lengths))