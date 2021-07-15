dic = {1 : 88, 2 : 30, 3 : 61, 4 : 55, 5 : 95}

for key, value in dic.items():
    if value >= 60:
        print("{}번 학생은 {}점으로 합격입니다.".format(key, value))
    else:
        print("{}번 학생은 {}점으로 불합격입니다.".format(key, value))

