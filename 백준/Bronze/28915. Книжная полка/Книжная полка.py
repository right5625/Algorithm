import math

h = int(input())
r = int(input())
print(math.ceil(r / int(math.sqrt(h * h * 0.75))) - 1)