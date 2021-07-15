# man1 = list.index(input()) + 1
# man2 = list.index(input()) + 1
#
# if man1 == man2:
#     print("Result: Draw")
# elif man1 -1 == man2 % 3:
#     print("Result : Man1 Win!")
# else:
#     print("Result : Man2 Win!")


def rsp():
    list = ['가위', '바위', '보']

    man1_name = input()
    man2_name = input()

    man1_select = input()
    man2_select = input()

    man1_idx = list.index(man1_select) + 1
    man2_idx = list.index(man2_select) + 1

    if man1_idx == man2_idx:
        print("비겼습니다.")
    elif man1_idx - 1 == man2_idx % 3:
        print("{0}가 이겼습니다!".format(man1_select))
    else:
        print("{0}가 이겼습니다!".format(man2_select))

rsp()