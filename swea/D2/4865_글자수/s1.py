import sys
sys.stdin = open('input.txt', encoding='UTF-8')

T = int(input())

for _ in range(1, T + 1):
    str1 = input()
    str2 = input()

    # str1 에 대한 딕셔너리 생성
    str_dict = {key: 0 for key in str1} # dictionary comprehension

    # 반복문을 이용해 개수를 세고 딕셔너리에 추가
    for chr in str2:
        if chr in str_dict: # 딕셔너리에 해당 key 가 존재한다면
            str_dict[chr] += 1 # 개수 증가

    # 최댓값 구하기
    max_val = 0
    for value in str_dict.values():
        if max_val < value:
            max_val = value

    print('#{} {}'.format(_, max_val))



