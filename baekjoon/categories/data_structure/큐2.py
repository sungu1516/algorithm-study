def func(command, number=0):    # 기본인자값
    global front        # front - 가장 앞에있는 수의 idx - 1
    global back         # back - 가장 뒤에있는 수의 idx
    number = int(number)

    if command == 'push':
        back += 1
        que[back] = number

    elif command == 'pop':
        if front == back:      # 큐가 비었을 때
            print(-1)
        else:
            front += 1         # 가장 앞의 원소로 이동
            print(que[front])

    elif command == 'size':
        print(back-front)       # 들어있는 원소의 개수 출력

    elif command == 'empty':
        if front == back:
            print(1)
        else:
            print(0)

    elif command == 'front':
        if front == back:
            print(-1)
        else:
            print(que[front+1])   # 원소를 직접적으로 빼는 것이 아님

    else:       # back
        if front == back:
            print(-1)
        else:
            print(que[back])  # 원소를 직접적으로 빼는 것이 아님

import sys
N = int(input())
# 빈 스택 초기화
que = [0] * N     # 수행시간 단축 위해
front = -1
back = -1

for _ in range(N):
    factor = sys.stdin.readline().split()      # 시간 단축을 위해 input() 대신 사용 (여러줄 입력받는 경우 빠름)
    func(*factor)   # 언팩 연산자 사용
