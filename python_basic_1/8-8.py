def square(n):
    return n ** 2

x, y = input().split(",")
x, y = int(x), int(y)

print("square({0}) => {1}".format(x, square(x)))
print("square({0}) => {1}".format(y, square(y)))