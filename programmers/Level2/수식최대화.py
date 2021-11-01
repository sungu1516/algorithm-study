from itertools import permutations

def calc(num1, num2, oper):
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    else:
        return num1 * num2

def solution(expression):
    # 최대상금 초기화
    max_reward = 0

    # expression > list 작업
    expression = expression.replace('+', ' + ') \
        .replace('-', ' - ') \
        .replace('*', ' * ').split()

    # permutaion - 모든 우선순위 고려
    # 모든 priority 에 대한 상금을 확인 & 최대값 갱신

    for perm in permutations(('+', '-', '*'), 3):
        priority = {}
        for i in range(3):
            priority[perm[i]] = i

        # 우선순위 바탕으로 계산결과 구하기
        stack = []  # 숫자를 임시적으로 저장
        opers = []  # 연산자를 //

        for elem in expression:
            # 해당 원소가 연산자인 경우
            if elem in priority:
                while opers and priority[elem] <= priority[opers[-1]]:
                    n2 = stack.pop()
                    n1 = stack.pop()
                    tmp = calc(n1, n2, opers.pop())
                    stack.append(tmp)
                opers.append(elem)
            # 숫자인 경우
            else:
                stack.append(int(elem))

        # 아직 남은 숫자들을 모두 연산해준다.
        while opers:
            n2 = stack.pop()
            n1 = stack.pop()
            tmp = calc(n1, n2, opers.pop())
            stack.append(tmp)

        # 최대상금 갱신
        now_reward = abs(stack[0])
        if now_reward > max_reward:
            max_reward = now_reward

    return max_reward