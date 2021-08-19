import sys
sys.stdin = open('input.txt', encoding='UTF-8')

T = int(input())
for _ in range(1, T + 1):
    word = input()
    stack = [word[0]] # word의 첫 번째 글자만 넣어서 stack 초기화

    for alp in word[1:]:
        if stack: # 스택안에 글자가 있는 경우
            if stack[-1] == alp:
                stack.pop() # 일치하는 경우 stack 의 글자를 삭제
            else:
                stack.append(alp) # 일치하지 않는 경우 stack 에 새로 넣어주기
        else:
            stack.append(alp) # 만약 stack 이 비어있다면 글자 추가

    print('#{} {}'.format(_, len(stack)))