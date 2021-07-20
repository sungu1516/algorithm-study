## 1. 객체지향 프로그램의 특징

#### 1) 추상화

#### 2) 상속

#### 3) 다형성 - 오버라이딩과 오버로딩이 있다.

#### 4) 실습
def create(name, age):
    return {"name": name, "age": age}

def to_str(person):
    return "{0}\t{1}".format(person["name"], person["age"])

members = [
    create("홍길동", 20),
    create("이순신", 45),
    create("강감찬", 35)
]

for member in members:
    print(to_str(member))


## 2. 클래스 정의
class Person:
    pass

member = Person()

if isinstance(member, Person):
    print("member객체는 Person 클래스의 객체입니다.")

#### 1) 생성자 메서드와 소멸자 메서드
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("{0} 객체가 생성되었습니다.".format(self.name))

    def __del__(self):
        print("{0} 객체가 소멸되었습니다.".format(self.name))

member = Person("홍길동", 20)

print("{0}\t{1}".format(member.name, member.age))
print(dir(member))

## 3. 클래스와 인스턴스의 특징
#### 1) 인스턴스 메서드
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("{0} 객체가 생성되었습니다.".format(self.name))

    def __del__(self):
        print("{0} 객체가 소멸되었습니다.".format(self.name))

    def to_str(self):
        return "{0}\t{1}".format(self.name, self.age)

members = [
    Person("홍길동", 20),
    Person("이순신", 45),
    Person("강감찬", 35)
]

for member in members:
    print(member.to_str())

#### 2) 인스턴스 변수 - private field 생성

class Person:
    def __init(self, name, age):
        self.__name = name
        self.__age = age
        print("{0} 객체가 생성되었습니다.".format(self.name))

    def __del__(self):
        print("{0} 객체가 소멸되었습니다.".format(self.name))

    def to_str(self):
        return "{0}\t{1}".format(self.__name, self.__age)

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0:
            raise ValueError("나이는 0이상의 값만 허용합니다.")
        self.__age = age

members = [
    Person("홍길동", 20),
    Person("이순신", 45),
    Person("강감찬", 35)
]

members[0].set_age(-20) # 예외 발생!!

#### 3) 데코레이터 기능
class Person:
    def __init(self, name, age):
        self.__name = name
        self.__age = age
        print("{0} 객체가 생성되었습니다.".format(self.name))

    def __del__(self):
        print("{0} 객체가 소멸되었습니다.".format(self.name))

    def to_str(self):
        return "{0}\t{1}".format(self.__name, self.__age)

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("나이는 0이상의 값만 허용합니다.")
        self.__age = age

members = [
    Person("홍길동", 20),
    Person("이순신", 45),
    Person("강감찬", 35)
]

members[0].age = 22

#### 4) 클래스 변수
class Person:
    count = 0

    def __init(self, name, age):
        self.__name = name
        self.__age = age
        Person.count += 1
        print("{0} 객체가 생성되었습니다.".format(self.name))

    def __del__(self):
        print("{0} 객체가 소멸되었습니다.".format(self.name))

    def to_str(self):
        return "{0}\t{1}".format(self.__name, self.__age)

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("나이는 0이상의 값만 허용합니다.")
        self.__age = age

members = [
    Person("홍길동", 20),
    Person("이순신", 45),
    Person("강감찬", 35)
]

print("현재 Person 클래스의 인스턴스는 총 {0} 개 입니다.".format(Person.count))


#### 5) 클래스 메서드
class Person:
    count = 0

    def __init(self, name, age):
        self.__name = name
        self.__age = age
        Person.count += 1
        print("{0} 객체가 생성되었습니다.".format(self.name))

    def __del__(self):
        print("{0} 객체가 소멸되었습니다.".format(self.name))

    def to_str(self):
        return "{0}\t{1}".format(self.__name, self.__age)

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("나이는 0이상의 값만 허용합니다.")
        self.__age = age

    @classmethod
    def get_info(cls):
        return "현재 Person 클래스의 인스턴스는 총 {0} 개입니다".format(cls.count)

members = [
    Person("홍길동", 20),
    Person("이순신", 45),
    Person("강감찬", 35)
]

print(Person.get_info())

#### 6) 연산자 오버로딩
class Person:
    count = 0

    def __init(self, name, age):
        self.__name = name
        self.__age = age
        Person.count += 1
        print("{0} 객체가 생성되었습니다.".format(self.name))

    def __del__(self):
        print("{0} 객체가 소멸되었습니다.".format(self.name))

    def to_str(self):
        return "{0}\t{1}".format(self.__name, self.__age)

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("나이는 0이상의 값만 허용합니다.")
        self.__age = age

    @classmethod
    def get_info(cls):
        return "현재 Person 클래스의 인스턴스는 총 {0} 개입니다".format(cls.count)

    def __gt__(self, other):
        return self.__age > other.__age

    def __ge__(self, other):
        return self.__age >= other.__age

    def __lt__(self, other):
        return self.__age < other.__age

    def __le__(self, other):
        return self.__age <= other.__age

    def __eq__(self, other):
        return self.__age == other.__age

    def __ne__(self, other):
        return self.__age != other.__age

members = [
    Person("홍길동", 20),
    Person("이순신", 45),
    Person("강감찬", 35)
]

cnt = len(members)
i = 0
while True:
    print("members[{0}] > members[{1}] => {2}".format(i, i + 1, members[i] > members[i + 1]))
    i += 1
    if i == cnt - 1:
        print("members[{0}] > members[{1}] => {2}".format(i, 0, members[i] > members[i + 1]))
        break

#### 7) __str()__ 메서드
class Person:
    count = 0

    def __init(self, name, age):
        self.__name = name
        self.__age = age
        Person.count += 1
        print("{0} 객체가 생성되었습니다.".format(self.name))

    def __del__(self):
        print("{0} 객체가 소멸되었습니다.".format(self.name))

    def to_str(self):
        return "{0}\t{1}".format(self.__name, self.__age)

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("나이는 0이상의 값만 허용합니다.")
        self.__age = age

    @classmethod
    def get_info(cls):
        return "현재 Person 클래스의 인스턴스는 총 {0} 개입니다".format(cls.count)

    def __gt__(self, other):
        return self.__age > other.__age

    def __ge__(self, other):
        return self.__age >= other.__age

    def __lt__(self, other):
        return self.__age < other.__age

    def __le__(self, other):
        return self.__age <= other.__age

    def __eq__(self, other):
        return self.__age == other.__age

    def __ne__(self, other):
        return self.__age != other.__age

    def __str__(self):
        return "{0}\t{1}".format(self.__name, self.__age)

members = [
    Person("홍길동", 20),
    Person("이순신", 45),
    Person("강감찬", 35)
]

for member in members:
    print(str(member))


#-----------------------------------------------------------------------------------------------------

## 4. 클래스 상속
#### 1) 상속
class Parent:
    def __init__(self, family_name):
        self.__family_name = family_name
        print("Parent 클래스의 __init__() ...")

    @property
    def family_name(self):
        return self.__family_name

class Child(Parent):
    def __init__(self, first_name, last_name):
        Parent.__init__(self, last_name)
        # super().__init__(last_name) -- 위 코드와 동일
        self.__first_name = first_name
        print("Child 클래스의 __init__() ...")

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def name(self):
        return "{0} {1}".format(self.family_name, self.first_name)

child = Child("길동", "홍")

print(child.family_name)
print(child.first_name)
print(child.name)
print("======>")
child.first_name = "길순"
print(child.name)

#### 2) 메서드 오버라이딩
class Parent:
    def __init__(self, family_name):
        self.__family_name = family_name
        print("Parent 클래스의 __init__() ...")

    @property
    def family_name(self):
        return self.__family_name

    def print_info(self):
        print("Parent: {0}".format(self.family_name))

class Child(Parent):
    def __init__(self, first_name, last_name):
        Parent.__init__(self, last_name)
        # super().__init__(last_name) -- 위 코드와 동일
        self.__first_name = first_name
        print("Child 클래스의 __init__() ...")

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def name(self):
        return "{0} {1}".format(self.family_name, self.first_name)

    def print_info(self):
        Parent.print_info(self)
        # super().print_info()
        print("Child: {0}".format(self.name))

child = Child("길동", "홍")
child.print_info()