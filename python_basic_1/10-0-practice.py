data_list = list(range(1, 11))

def input_index():
    num = 0
    try:
        num = int(input("인덱스로 사용할 숫자를 입력하세요: "))
    except ValueError as exception:
        raise exception
    else:
        return num

def print_in_bounds(list, index):
    value = 0
    try:
        value = list[index]
    except IndexError as exception:
        print("{0}, {1}".format(type(exception), exception))
        index = len(list) - 1
        print("인덱스는 0에서 {0}까지 사용할 수 있습니다.".format(index))
        value = list[index]
    finally:
        print("[{0}]: {1}".format(index, value))

try:
    idx = input_index()
    print_in_bounds(data_list, idx)
except ValueError as ve:
    print("{0}, {1}".format(type(ve), ve))
else:
    print("정상 출력")