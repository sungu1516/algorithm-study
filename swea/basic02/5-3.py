class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

class GraduateStudent(Student):
    def __init__(self, name, major):
        Student.__init__(self, name)
        self.__major = major

    @property
    def major(self):
        return self.__major

student1 = Student("홍길동")
gr_student1 = GraduateStudent("이순신", "컴퓨터")

print("이름: {0}".format(student1.name))
print("이름: {0}, 전공: {1}".format(gr_student1.name, gr_student1.major))