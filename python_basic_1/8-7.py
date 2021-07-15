num = int(input())

def get_factorial(n):
    total = 1
    while n >= 1:
        total *= n
        n -= 1

    return total

result = get_factorial(num)
print(result)