cnt1 = cnt2 = 0
for i in input():
    cnt1 += 'kangaroo'.count(i) + 'KANGAROO'.count(i)
    cnt2 += 'kiwibird'.count(i) + 'KIWIBIRD'.count(i)
print('Feud continues' if cnt1 == cnt2 else ('Kangaroos' if cnt1 > cnt2 else 'Kiwis'))