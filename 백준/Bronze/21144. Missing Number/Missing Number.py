n = int(input())
numbers = input()
idx = 0
number = 1
number_length = 1
length = len(numbers)
result = n
while idx < length:
    if int(numbers[idx:idx + number_length]) != number:
        result = number
        break
    idx += number_length
    number += 1
    if number == 10 or number == 100:
        number_length += 1
print(result)