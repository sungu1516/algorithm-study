import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N, password = input().split()
    stack = []

    # 비밀번호를 순회하며 stack 에 쌓아주기
    for num in password:
        if stack: # 스택에 값이 존재하는 경우
            if stack[-1] == num:
                stack.pop() # 만약 stack 에 추가할 숫자가 top 위치의 숫자와 같다면, 해당 숫자를 제거
            else:
                stack.append(num)
        else: # stack 에 값이 없다면 우선 숫자를 더해준다.
            stack.append(num)

    print('#{} {}'.format(tc, ''.join(stack)))