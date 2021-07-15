list = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
dic = {'A': 0, 'O': 0, 'B': 0, 'AB': 0}

for key in dic.keys():
    for el in list:
        if key == el:
            dic[key] += 1

print(dic)
