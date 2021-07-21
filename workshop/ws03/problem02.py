# 2. Dictionary로 이루어진 List의 합 구하기

def dict_list_sum(dict_list):
    total = 0
    for a_dict in dict_list:
        total += a_dict['age']
    return total

print(dict_list_sum([{'age' : 12},
        {'age' : 4}]))
