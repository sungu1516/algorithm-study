# 3. 2차원 List의 전체 함 구하기

def all_list_sum(twod_list):
    total = 0
    for a_list in twod_list:
        for number in a_list:
            total += number

    return total

print(all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]))