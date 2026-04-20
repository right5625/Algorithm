s = input()
t = input()
count_s = [0] * 26
count_t = [0] * 26
for i in range(1, len(s)):
    count_s[ord(s[i]) - ord('a')] += 1
for i in range(len(t) - 1):
    count_t[ord(t[i]) - ord('a')] += 1
result = len(s) * len(t)
for i in range(26):
    result -= count_s[i] * count_t[i]
print(result)