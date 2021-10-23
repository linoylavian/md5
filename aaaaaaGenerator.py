def generator(s, place):
    for f in range(25):
        tmp = chr(ord(s[place]) + 1)
        s = s[:place] + tmp + s[place + 1:]
        print(s)
        for x in range(5 - place):
            generator(s, 5 - x)


s = "aaaaaa"
print(s)
for i in range(6):
    generator(s, 5 - i)
