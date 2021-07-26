# 정사각형만 만들기

test = [23, 32, 55, 63]
test2 = [13, 32, 40, 55]

def only_square_area(*lists):
    return ([x * y for x in lists[0] for y in lists[1] if x == y])

print(only_square_area(test, test2))