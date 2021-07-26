# 1. 평균 점수 구하기

test = {'q' : 80, 'w' : 90, 'd': 89, 'c':83}

def get_dict_avg(dict):
    return sum(dict.values())/len(dict)

print(get_dict_avg(test))