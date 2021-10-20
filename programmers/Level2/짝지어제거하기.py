def solution(s):
    stack = [0] * len(s)
    top = -1

    for alpha in s:
        # empty stack
        if top == -1:
            # stack 에 알파벳을 넣어준다.
            top += 1
            stack[top] = alpha

        # not empty
        else:
            # stack의 top에 위치한 알파벳과 현재 순회하는 알파벳 비교
            # 같다면
            if alpha == stack[top]:
                top -= 1

            # 다를 때
            else:
                top += 1
                stack[top] = alpha

    # 모든 알파벳에 대해 순회가 끝남
    # empty
    if top == -1:
        answer = 1
    else:
        answer = 0

    return answer