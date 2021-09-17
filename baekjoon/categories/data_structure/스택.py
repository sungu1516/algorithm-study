import sys
N = int(input())
# 빈 스택 초기화
stack = [0] * N     # 수행시간 단축 위해
top = -1             # top = 가장 위에 있는 정수의 위치

for _ in range(N):
    arr = sys.stdin.readline().split()      # 시간 단축을 위해 input() 대신 사용 (여러줄 입력받는 경우 빠름)
    command = arr[0]
    if len(arr) > 1:
        number = int(arr[1])

    if command == 'push':
        top += 1
        stack[top] = number
    elif command == 'pop':
        if top > -1:  # 만약 스택안에 정수가 존재하는 경우
            print(stack[top])
            top -= 1  # top 위치를 이동 > 마지막 값을 뺀다.
        else:  # 스택안에 정수가 없는 경우
            print(-1)
    elif command == 'size':
        print(top+1)  #
    elif command == 'empty':
        if top > -1:
            print(0)
        else:  # 스택이 비어있는 경우
            print(1)
    else:
        if top > -1:
            print(stack[top])  # 가장 위에 있는 정수를 출력
        else:
            print(-1)
