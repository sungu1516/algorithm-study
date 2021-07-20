def multiple(*params):
    total = 1
    for param in params:
        if type(param) != int:
            print("에러발생")
            return
        total *= param
    return(total)

print(multiple(1, 2, 3, 4, '5'))