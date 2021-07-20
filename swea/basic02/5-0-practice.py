class Student:
    def __init__(self, name, gender, height):
        self.__name = name
        self.__gender = gender
        self.height = height

    @property
    def name(self):
        return self.__name

    @property
    def gender(self):
        return self.__gender

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def __repr__(self):
        return "{0}(name: {1}, gender: {2}, height: {3})".format(self.__class__.__name__, self.name, self.gender, self.height)

students = [
    Student("홍길동", "남", 176.5),
    Student("이순신", "남", 188.5),
    Student("유관순", "여", 161.5),
    Student("강감찬", "남", 182.5)
]

for student in students:
    print(student)

# 정렬

print("name으로 오름차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.name, reverse=False):
    print(student)

print("name으로 내림차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.name, reverse=True):
    print(student)

print("height로 오름차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.height, reverse=False):
    print(student)

print("height로 내림차순 정렬 후 ===>")
for student in sorted(students, key=lambda x: x.height, reverse=True):
    print(student)