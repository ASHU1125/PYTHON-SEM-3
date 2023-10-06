
count = 0

for i in range(33, 127):
    count = count + 1
    print(chr(i), ":", i, ":", hex(i), end="            ")
    if count % 5 == 0:
        print()
