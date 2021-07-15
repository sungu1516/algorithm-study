str = "abcdef"
dic = {}

for idx, str in enumerate(list(str)):
    dic[str] = idx

for key, val in dic.items():
    print("{0}: {1}".format(key, val))