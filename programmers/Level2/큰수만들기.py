def solution(number, k):
    # 제거한 횟수
    stack = [number[0]]

    for i in range(1, len(number)):
        while stack and stack[-1] < number[i] and k > 0:
            stack.pop()
            k -= 1
        stack.append(number[i])

    result = ''.join(stack)

    if k > 0:
        return result[:-k]

    return result