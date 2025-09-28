for i in map(str, range(10, 100)):
    if int(i[::-1]) % 8 == 0 and (int(i[0]) + int(i[1])) % 6 == 0 and '8' not in i:
        print(i)
        break