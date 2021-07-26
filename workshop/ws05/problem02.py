# 2. 혈액형 분류하기

blood_list = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

def count_blood(blood_types):
    # 빈 딕셔너리 생성
    dict = {}
    # key에 해당하는 개수를 count 메서드를 활용하여 value 로 넣어줌
    dict['A'] = blood_types.count('A')
    dict['B'] = blood_types.count('B')
    dict['O'] = blood_types.count('O')
    dict['AB'] = blood_types.count('AB')

    return dict

print(count_blood(blood_list))