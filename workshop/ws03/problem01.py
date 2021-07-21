# 1. List의 합 구하기

def list_sum(int_list):
    total = 0
    for number in int_list:
        total += number
    return total

print(list_sum(list(range(1, 6))))