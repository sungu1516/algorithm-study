def solution(a, b):
    answer = 0

    if a > b:
        a, b = b, a

    for number in range(a, b + 1):
        answer += number

    return answer