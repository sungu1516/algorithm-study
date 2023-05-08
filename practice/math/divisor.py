# 약수
def getDivisor(num):
    result = []

    for i in range(1, int(num**(1/2)) + 1):
        if num % i == 0:
            result.append(i)

            if i != int(num**(1/2)):
                result.append(num//i)

    return result

print(getDivisor(64))