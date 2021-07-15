class Student:
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def get_total(self):
        return self.kor + self.eng + self.math

input_score = list(map(lambda x: int(x.strip()), input().split(",")))
student1 = Student(input_score[0], input_score[1], input_score[2])

total = student1.get_total()
print("국어, 영어, 수학의 총점: {0}".format(total))