data_list = list(range(1, 21))
expr1 = input("항목 x에 적용할 표현식을 입력하세요: ")
expr2 = input("항목 x를 필터링할 조건의 표현식을 입력하세요: ")

print(list(map(lambda x: eval(expr1), data_list)))
print(list(filter(lambda x: eval(expr2), data_list)))