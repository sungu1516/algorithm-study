list = []

for i in range(100, 301):
    if ((i // 100) % 2 == 0) and (((i % 100) // 10) % 2 == 0) and ((i % 10) % 2 == 0):
        list.append(str(i))

print(','.join(list))

