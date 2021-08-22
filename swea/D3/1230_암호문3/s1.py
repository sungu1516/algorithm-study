import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# 함수 정의
def processer(func, args):
    if func == 'I':
        x, y = args[0]-1, args[1]
        for i in range(y):
            password.insert(x+1+i, args[2+i])
    elif func == 'D':
        x, y = args[0]-1, args[1]
        for _ in range(y):
            password.pop(x+1)
    else:
        y = args[0]
        for i in range(y):
            password.append(args[i+1])

T = 10
for tc in range(1, T + 1):
    N = int(input()) # 원본 암호문의 길이
    password = list(map(int, input().split())) # 원본 암호문
    M = int(input()) # 명령어의 개수
    command = list(input().split()) # 명령어
    operator = ['I', 'D', 'A']

    # stack 1이용, 명령어 실행
    stack = [command[0]]
    for i in range(1, len(command)-1):
        if command[i] in operator:
            processer(stack[0], list(map(int, stack[1:])))
            stack = [command[i]]
        else:
            stack.append(command[i])
            if i == len(command)-1:
                processer(stack[0], list(map(int, stack[1:])))

    print('#{}'.format(tc), *password[:10])