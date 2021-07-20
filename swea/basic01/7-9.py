i, k = 0, 4

while k >= 1:
    print("{0}{1}".format(" " * i, "*" * (2*k - 1)))
    i += 1
    k -= 1