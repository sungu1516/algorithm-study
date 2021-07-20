c = input()

if 65<=ord(c)<=90 or 97<=ord(c)<=122:
    print("{}(ASCII: {}) => {}(ASCII: {})".format(c, ord(c), c.upper(), ord(c.upper())))
else:
    print(c)

print("c(ASCII: 99) => C(ASCII: 67)")