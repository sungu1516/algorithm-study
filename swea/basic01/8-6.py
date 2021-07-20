list = [2, 4, 6, 8, 10]

def find_num(number):
    for i in list:
        if i == number:
            return True
    return False

print(list)
print("{0} => {1}".format(5, find_num(5)))
print("{0} => {1}".format(10, find_num(10)))